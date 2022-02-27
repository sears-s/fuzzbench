#!/usr/bin/env python3

# Run make build-standalone_build-all first

import os
import re
import shutil
import subprocess

from common import benchmark_utils
from experiment import runner

# Clean and create out directory
OUT_DIR = os.path.abspath("./benchmarks_bin/")
if os.path.isdir(OUT_DIR):
    shutil.rmtree(OUT_DIR)
os.makedirs(OUT_DIR)

# Get built benchmark names
r = subprocess.run(
    ["docker", "image", "ls"], check=True, capture_output=True
).stdout.decode()
image_names = re.findall(r"(gcr.io/fuzzbench/builders/standalone_build/\S+) ", r)
for image_name in image_names:
    if "intermediate" in image_name:
        continue
    benchmark = image_name.split("/")[-1]
    benchmark_dir = os.path.join(OUT_DIR, benchmark)
    print(f"Getting files from {benchmark}")

    # Get the target name and path
    target_name = benchmark_utils.get_fuzz_target(benchmark)
    target_path = os.path.join("/out/", target_name)

    # Get paths for libraries and linker
    r = subprocess.run(
        ["docker", "run", "--rm", image_name, "/bin/bash", "-c", f"ldd {target_path}"],
        check=True,
        capture_output=True,
    ).stdout.decode()
    lib_paths = re.findall(r"=> (/.+) \(", r)
    linker_path = re.findall(r"(/.+ld-linux.+) \(", r)
    linker_path = linker_path[0] if len(linker_path) > 0 else None

    # Copy the files out
    subprocess.run(
        [
            "docker",
            "run",
            "-v",
            f"{benchmark_dir}:/b",
            "--rm",
            image_name,
            "/bin/bash",
            "-c",
            f"cp -Lr /out/* {linker_path} /b/; echo {target_name} > /b/target.txt; mkdir -p /b/lib/; cp {' '.join(lib_paths)} /b/lib/;",
        ],
        check=True,
    )
    subprocess.run(
        f"sudo chown -R $(id -u):$(id -g) {benchmark_dir}", check=True, shell=True
    )

    # Standardize seeds directory
    seeds_path = os.path.join(benchmark_dir, "seeds/")
    os.makedirs(seeds_path, exist_ok=True)
    runner._unpack_clusterfuzz_seed_corpus(
        os.path.join(benchmark_dir, target_name), seeds_path
    )
    runner._clean_seed_corpus(seeds_path)

    # Remove extra files
    for name in os.listdir(seeds_path):
        path = os.path.join(seeds_path, name)
        if os.path.isdir(path):
            shutil.rmtree(path)
    subprocess.run(
        f"rm -f {os.path.join(benchmark_dir, '*.zip')}", shell=True, check=True
    )

# Ensure all files are executable
subprocess.run(["chmod", "-R", "+x", OUT_DIR], check=True)

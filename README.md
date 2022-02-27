### all: 48
['arrow_parquet-arrow-fuzz', 'aspell_aspell_fuzzer', 'bloaty_fuzz_target', 'curl_curl_fuzzer_http', 'file_magic_fuzzer', 'freetype2-2017', 'grok_grk_decompress_fuzzer', 'harfbuzz-1.3.2', 'jsoncpp_jsoncpp_fuzzer', 'lcms-2017-03-21', 'libarchive_libarchive_fuzzer', 'libgit2_objects_fuzzer', 'libhevc_hevc_dec_fuzzer', 'libhtp_fuzz_htp', 'libjpeg-turbo-07-2017', 'libpcap_fuzz_both', 'libpng-1.2.56', 'libxml2-v2.9.2', 'libxml2_libxml2_xml_reader_for_file_fuzzer', 'libxslt_xpath', 'matio_matio_fuzzer', 'mbedtls_fuzz_dtlsclient', 'mruby-2018-05-23', 'muparser_set_eval_fuzzer', 'ndpi_fuzz_ndpi_reader', 'njs_njs_process_script_fuzzer', 'openh264_decoder_fuzzer', 'openssl_x509', 'openthread-2019-12-23', 'php_php-fuzz-execute', 'php_php-fuzz-parser', 'php_php-fuzz-parser-2020-07-25', 'poppler_pdf_fuzzer', 'proj4-2017-08-14', 'proj4_standard_fuzzer', 'quickjs_eval-2020-01-05', 're2-2014-12-09', 'sqlite3_ossfuzz', 'stb_stbi_read_fuzzer', 'systemd_fuzz-link-parser', 'systemd_fuzz-varlink', 'tpm2_tpm2_execute_command_fuzzer', 'usrsctp_fuzzer_connect', 'vorbis-2017-12-11', 'wireshark_fuzzshark_ip', 'woff2-2016-05-06', 'zlib_zlib_uncompress_fuzzer', 'zstd_stream_decompress']
### coverage: 22
['bloaty_fuzz_target', 'curl_curl_fuzzer_http', 'jsoncpp_jsoncpp_fuzzer', 'libpcap_fuzz_both', 'libxslt_xpath', 'mbedtls_fuzz_dtlsclient', 'openssl_x509', 'php_php-fuzz-parser', 'sqlite3_ossfuzz', 'systemd_fuzz-link-parser', 'zlib_zlib_uncompress_fuzzer', 'freetype2-2017', 'harfbuzz-1.3.2', 'lcms-2017-03-21', 'libjpeg-turbo-07-2017', 'libpng-1.2.56', 'libxml2-v2.9.2', 'openthread-2019-12-23', 'proj4-2017-08-14', 're2-2014-12-09', 'vorbis-2017-12-11', 'woff2-2016-05-06']
### oss_fuzz_coverage: 11
['bloaty_fuzz_target', 'curl_curl_fuzzer_http', 'jsoncpp_jsoncpp_fuzzer', 'libpcap_fuzz_both', 'libxslt_xpath', 'mbedtls_fuzz_dtlsclient', 'openssl_x509', 'php_php-fuzz-parser', 'sqlite3_ossfuzz', 'systemd_fuzz-link-parser', 'zlib_zlib_uncompress_fuzzer']
standard_coverage: 11
['freetype2-2017', 'harfbuzz-1.3.2', 'lcms-2017-03-21', 'libjpeg-turbo-07-2017', 'libpng-1.2.56', 'libxml2-v2.9.2', 'openthread-2019-12-23', 'proj4-2017-08-14', 're2-2014-12-09', 'vorbis-2017-12-11', 'woff2-2016-05-06']
### bug: 26
['arrow_parquet-arrow-fuzz', 'aspell_aspell_fuzzer', 'file_magic_fuzzer', 'grok_grk_decompress_fuzzer', 'libarchive_libarchive_fuzzer', 'libgit2_objects_fuzzer', 'libhevc_hevc_dec_fuzzer', 'libhtp_fuzz_htp', 'libxml2_libxml2_xml_reader_for_file_fuzzer', 'matio_matio_fuzzer', 'mruby-2018-05-23', 'muparser_set_eval_fuzzer', 'ndpi_fuzz_ndpi_reader', 'njs_njs_process_script_fuzzer', 'openh264_decoder_fuzzer', 'php_php-fuzz-execute', 'php_php-fuzz-parser-2020-07-25', 'poppler_pdf_fuzzer', 'proj4_standard_fuzzer', 'quickjs_eval-2020-01-05', 'stb_stbi_read_fuzzer', 'systemd_fuzz-varlink', 'tpm2_tpm2_execute_command_fuzzer', 'usrsctp_fuzzer_connect', 'wireshark_fuzzshark_ip', 'zstd_stream_decompress']

# FuzzBench: Fuzzer Benchmarking As a Service

FuzzBench is a free service that evaluates fuzzers on a wide variety of
real-world benchmarks, at Google scale. The goal of FuzzBench is to make it
painless to rigorously evaluate fuzzing research and make fuzzing research
easier for the community to adopt. We invite members of the research community
to contribute their fuzzers and give us feedback on improving our evaluation
techniques.

FuzzBench provides:

* An easy API for integrating fuzzers.
* Benchmarks from real-world projects. FuzzBench can use any
  [OSS-Fuzz](https://github.com/google/oss-fuzz) project as a benchmark.
* A reporting library that produces reports with graphs and statistical tests
  to help you understand the significance of results.

To participate, submit your fuzzer to run on the FuzzBench platform by following
[our simple guide](
https://google.github.io/fuzzbench/getting-started/).
After your integration is accepted, we will run a large-scale experiment using
your fuzzer and generate a report comparing your fuzzer to others.
See [a sample report](https://www.fuzzbench.com/reports/sample/index.html).

## Overview
![FuzzBench Service diagram](docs/images/FuzzBench-service.png)

## Sample Report

You can view our sample report
[here](https://www.fuzzbench.com/reports/sample/index.html) and
our periodically generated reports
[here](https://www.fuzzbench.com/reports/index.html).
The sample report is generated using 10 fuzzers against 24 real-world
benchmarks, with 20 trials each and over a duration of 24 hours.
The raw data in compressed CSV format can be found at the end of the report.

When analyzing reports, we recommend:
* Checking the strengths and weaknesses of a fuzzer against various benchmarks.
* Looking at aggregate results to understand the overall significance of the
  result.

Please provide feedback on any inaccuracies and potential improvements (such as
integration changes, new benchmarks, etc.) by opening a GitHub issue
[here](https://github.com/google/fuzzbench/issues/new).

## Documentation

Read our [detailed documentation](https://google.github.io/fuzzbench/) to learn
how to use FuzzBench.

## Contacts

Join our [mailing list](https://groups.google.com/forum/#!forum/fuzzbench-users)
for discussions and announcements, or send us a private email at
[fuzzbench@google.com](mailto:fuzzbench@google.com).

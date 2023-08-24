cc_library(
  name = "capicxx_core_runtime",
  hdrs = glob(["include/CommonAPI/**/*.hpp"]),
  srcs = glob(["src/CommonAPI/*.cpp"]),
  copts = [
    "-Wall",
    "-Wextra",
    "-Wformat",
    "-Wformat-security",
    "-Wconversion",
    "-fexceptions",
    "-fstrict-aliasing",
    "-fstack-protector",
    "-fasynchronous-unwind-tables",
    "-fno-omit-frame-pointer",
    "-Werror",
    "-fvisibility=hidden",
    "-Wno-deprecated",
  ],
  includes = ["include"],
  defines = [
    "COMMONAPI_INTERNAL_COMPILATION",
    "COMMONAPI_LOGLEVEL=COMMONAPI_LOGLEVEL_DEBUG",
  ],
  visibility = ["//visibility:public"],
)

cc_shared_library(
  name = "shared_lib",
  deps = [
    ":capicxx_core_runtime",
  ],
  visibility = ["//visibility:public"]
)
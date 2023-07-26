cc_library(
  name = "capicxx_someip_runtime",
  hdrs = glob(["include/CommonAPI/SomeIP/*.hpp"]),
  srcs = glob(["src/CommonAPI/SomeIP/*.cpp"]),
  includes = [ 
    "include"
  ],
  defines = [
    "COMMONAPI_INTERNAL_COMPILATION",
    "COMMONAPI_SOMEIP_VERSION_MAJOR=3",
    "COMMONAPI_SOMEIP_VERSION_MINOR=2",
    "COMMONAPI_LOGLEVEL=COMMONAPI_LOGLEVEL_DEBUG"
  ],
  deps = [
    "@com_github_covesa_capicxx_core_runtime//:capicxx_core_runtime",
    "@com_github_covesa_vsomeip//:vsomeip",
  ],
  visibility = ["//visibility:public"],
)
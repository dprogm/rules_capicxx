load("@com_github_dprogm_rules_capicxx//tools:configure.bzl", "configure")

configure(
  name = "internal_config_header",
  input = "implementation/configuration/include/internal.hpp.in",
  configs = [
    "@com_github_dprogm_rules_capicxx//third_party/vsomeip:vsomeip.conf",
  ],
  output = "internal.hpp",
)

cc_library(
  name = "internal_config",
  hdrs = [
    ":internal_config_header",
  ],
)

cc_library(
  name = "vsomeip",
  hdrs = glob([
    "interface/vsomeip/**/*.hpp",
    "interface/vsomeip/**/*.h",
  ]),
  srcs = glob([
    "implementation/configuration/include/*.hpp",
    "implementation/e2e_protection/include/**/*.hpp",
    "implementation/service_discovery/include/**/*.hpp",
    "implementation/endpoints/src/*.cpp",
    "implementation/endpoints/include/*.hpp",
    "implementation/logger/src/*.cpp",
    "implementation/logger/include/*.hpp",
    "implementation/tracing/src/*.cpp",
    "implementation/tracing/include/*.hpp",
    "implementation/message/src/*.cpp",
    "implementation/message/include/*.hpp",
    "implementation/plugin/src/*.cpp",
    "implementation/plugin/include/*.hpp",
    "implementation/protocol/src/*.cpp",
    "implementation/protocol/include/*.hpp",
    "implementation/routing/src/*.cpp",
    "implementation/routing/include/*.hpp",
    "implementation/runtime/src/*.cpp",
    "implementation/runtime/include/*.hpp",
    "implementation/security/src/*.cpp",
    "implementation/security/include/*.hpp",
    "implementation/utility/src/*.cpp",
    "implementation/utility/include/*.hpp",
  ]),
  includes = [
    "interface"
  ],
  deps = [
    ":internal_config",
    "@boost//:property_tree",
    "@boost//:filesystem",
    "@boost//:algorithm",
    "@boost//:optional",
    "@boost//:utility",
    "@boost//:foreach",
    "@boost//:array",
    "@boost//:thread",
    "@boost//:asio",
    "@boost//:icl"
  ],
  defines = [
    "VSOMEIP_BOOST_VERSION=108200",
    "WITHOUT_SYSTEMD",
    "VSOMEIP_INTERNAL_SUPPRESS_DEPRECATED",
    "VSOMEIP_VERSION=\\\"3.3.8\\\""
  ],
  visibility = ["//visibility:public"],
)

cc_library(
  name = "vsomeip_sd",
  srcs = glob([
    "implementation/service_discovery/include/*.hpp",
    "implementation/service_discovery/src/*.cpp"
  ]),
  deps = [
    ":vsomeip",
  ],
  visibility = ["//visibility:public"],
)

cc_shared_library(
  name = "vsomeip_sd_shared_lib",
  deps = [
    ":vsomeip_sd",
  ],
  visibility = ["//visibility:public"]
)

genrule(
   name = "vsomeip_sd_shared_lib_patched",
   srcs = ["vsomeip_sd_shared_lib"],
   outs = ["libvsomeip3-sd.so.3"],
   cmd = "cp $(location vsomeip_sd_shared_lib) $(location libvsomeip3-sd.so.3)",
   visibility = ["//visibility:public"]

)

cc_library(
  name = "vsomeip_e2e",
  srcs = glob([
    "implementation/e2e_protection/include/**/*.hpp",
    "implementation/e2e_protection/src/**/*.cpp",
  ]),
  deps = [
    ":vsomeip",
  ],
  visibility = ["//visibility:public"],
)

cc_library(
  name = "vsomeip_cfg",
  srcs = glob([
    #"implementation/e2e_protection/include/**/*.hpp",
    "implementation/configuration/src/*.cpp",
  ]),
  deps = [
    ":vsomeip",
  ],
  visibility = ["//visibility:public"],
)

cc_shared_library(
  name = "vsomeip_cfg_shared_lib",
  deps = [
    ":vsomeip_cfg",
  ],
  visibility = ["//visibility:public"]
)

genrule(
   name = "vsomeip_cfg_shared_lib_patched",
   srcs = ["vsomeip_cfg_shared_lib"],
   outs = ["libvsomeip3-cfg.so.3"],
   cmd = "cp $(location vsomeip_cfg_shared_lib) $(location libvsomeip3-cfg.so.3)",
   visibility = ["//visibility:public"]

)
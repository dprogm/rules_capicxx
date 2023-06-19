# Bazel build rules for CommonAPI

Contains bazel build rules for building the CommonAPI core runtime as well as the commonly used binding runtimes for `dbus` and `vsomeip`.

# Usage

Put the following content into your bazel workspace:

```Starlark
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "com_github_dprogm_rules_capicxx",
    url = "https://github.com/dprogm/rules_capicxx/archive/refs/heads/main.zip",
    # strip_prefix = "",
)

load("@com_github_dprogm_rules_capicxx//:deps.bzl", "deps")
deps()
```

This brings the following labels into scope:

| Library                  | Label                                                              |
|--------------------------|--------------------------------------------------------------------|
| CommonAPI Core Runtime   | @com_github_covesa_capicxx_core_runtime//:capicxx_core_runtime     |
| CommonAPI DBus Runtime   | @com_github_covesa_capicxx_dbus_runtime//:capicxx_dbus_runtime     |
| CommonAPI SomeIP Runtime | @com_github_covesa_capicxx_someip_runtime//:capicxx_someip_runtime |

# Supported Platforms

The goal is to support MacOS, Linux and Windows.

# Next Steps

- [ ] Complete the build files for the binding libraries
- [ ] Add build file for `dbus`
- [ ] Add build file for `vsomeip`
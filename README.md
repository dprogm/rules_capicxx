# Bazel build rules for CommonAPI

Contains bazel build rules for building the CommonAPI core runtime as well as the commonly used binding runtimes for `dbus` and `vsomeip`.

# Usage

Put the following content into your bazel workspace:

```Starlark
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
  name = "com_github_dprogm_rules_capicxx",
  url = "https://github.com/dprogm/rules_capicxx/archive/refs/heads/main.zip",
  # Update the hash value accordingly
  # sha256 = "e8a1dcdd6dd7bb0982756dbe4d2896639f5844ab436c9296b86748c05e018139",
  strip_prefix = "rules_capicxx-main",
)

load("@com_github_dprogm_rules_capicxx//:deps.bzl", "deps")
deps()

load("@com_github_nelhage_rules_boost//:boost/boost.bzl", "boost_deps")
boost_deps()
```

This brings the following labels into scope:

| Library                  | Label                                                              | Version |
|--------------------------|--------------------------------------------------------------------|---------|
| CommonAPI Core Runtime   | @com_github_covesa_capicxx_core_runtime//:capicxx_core_runtime     | 3.2.0   |
| CommonAPI DBus Runtime   | @com_github_covesa_capicxx_dbus_runtime//:capicxx_dbus_runtime     | 3.2.0   |
| CommonAPI SomeIP Runtime | @com_github_covesa_capicxx_someip_runtime//:capicxx_someip_runtime | 3.2.0   |

The following third party library versions are currently used:

| Library | Version |
|---------|---------|
| dbus    | 1.15.6  |
| vsomeip | 3.3.8   |
| boost   | 1.82    |

# Supported Platforms

The goal is to support MacOS, Linux and Windows.

| Library | MacOS              | Linux              | Windows |
|---------|--------------------|--------------------|---------|
| dbus    | :heavy_check_mark: | :heavy_check_mark: | :x:     |
| vsomeip | :x:                | :heavy_check_mark: | :x:     |

# Next Steps

- [ ] Complete the build files for the binding libraries
- [x] Add build file for `dbus`
- [x] Add build file for `vsomeip`
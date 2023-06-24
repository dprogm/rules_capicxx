load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

def deps():
  http_archive(
    name = "com_github_covesa_capicxx_core_runtime",
    build_file = "@com_github_dprogm_rules_capicxx//:capicxx_core_runtime.BUILD",
    url = "https://github.com/COVESA/capicxx-core-runtime/archive/refs/tags/3.2.0.tar.gz",
    sha256 = "e2e7921a0e0c0d42f8a57028ab020566ee2c717b045b5e87513e1d4a91f16669",
    strip_prefix = "capicxx-core-runtime-3.2.0",
  )

  http_archive(
    name = "com_github_covesa_capicxx_dbus_runtime",
    build_file = "@com_github_dprogm_rules_capicxx//binding:capicxx_dbus_runtime.BUILD",
    url = "https://github.com/COVESA/capicxx-dbus-runtime/archive/refs/tags/3.2.0.tar.gz",
    sha256 = "7adbd5b262984b96815a5afa49d132ff2d8e7aea722c281231c84861a6b9de2e",
    strip_prefix = "capicxx-dbus-runtime-3.2.0",
  )

  http_archive(
    name = "com_github_covesa_capicxx_someip_runtime",
    build_file = "@com_github_dprogm_rules_capicxx//binding:capicxx_someip_runtime.BUILD",
    url = "https://github.com/COVESA/capicxx-someip-runtime/archive/refs/tags/3.2.0.tar.gz",
    sha256 = "bd50eac54970dfb2f16b77fa4955b28208a9a3d894787b7e3f8cfcb72fed1856",
    strip_prefix = "capicxx-someip-runtime-3.2.0",
  )

  http_archive(
    name = "org_freedesktop_gitlab_dbus",
    build_file = "@com_github_dprogm_rules_capicxx//third_party/dbus:dbus.BUILD",
    patch_args = ["-p1"],
    patches = [
      "@com_github_covesa_capicxx_dbus_runtime//:src/dbus-patches/capi-dbus-add-send-with-reply-set-notify.patch",
      "@com_github_covesa_capicxx_dbus_runtime//:src/dbus-patches/capi-dbus-add-support-for-custom-marshalling.patch",
      "@com_github_covesa_capicxx_dbus_runtime//:src/dbus-patches/capi-dbus-block-acquire-io-path-on-send.patch",
      # The following patch doesn't work. However compilation succeeds nevertheless
      # TODO Further investigate the importance
      #"@com_github_covesa_capicxx_dbus_runtime//:src/dbus-patches/capi-dbus-correct-dbus-connection-block-pending-call.patch",
      "@com_github_covesa_capicxx_dbus_runtime//:src/dbus-patches/capi-dbus-send-with-reply-and-block-delete-reply-on-error.patch",
    ],
    url = "https://gitlab.freedesktop.org/dbus/dbus/-/archive/dbus-1.15.6/dbus-dbus-1.15.6.tar.gz",
    sha256 = "614d61cda795280065f743ed05bbec0ff7ac036a9eb828cb5fb865465fc2d61a",
    strip_prefix = "dbus-dbus-1.15.6",
  )
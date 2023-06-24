load("@com_github_dprogm_rules_capicxx//tools:configure.bzl", "configure")

configure(
  name = "header_config",
  input = "@com_github_dprogm_rules_capicxx//third_party/dbus:header.tpl",
  configs = [
    "@com_github_dprogm_rules_capicxx//third_party/dbus:header.conf",
  ],
  output = "AUTOPACKAGE_CONFIG_H_TEMPLATE",
)

configure(
  name = "dbus_config",
  input = "cmake/config.h.cmake",
  configs = [
    ":header_config",
    "@com_github_dprogm_rules_capicxx//third_party/dbus:dbus.conf",
  ],
  output = "config.h",
)

configure(
  name = "dbus_arch_deps",
  input = "dbus/dbus-arch-deps.h.in",
  configs = [
    "@com_github_dprogm_rules_capicxx//third_party/dbus:arch.conf",
  ],
  output = "dbus/dbus-arch-deps.h",
)

cc_library(
  name = "arch_deps",
  hdrs = [
    ":dbus_arch_deps",
  ],
  # This is required because the arch-deps
  # header is included with <dbus/dbus-arch-deps.h>
  # (system header include)
  includes = ["."]
)

cc_library(
  name = "config",
  hdrs = [
    ":dbus_config"
  ],
  # This is required because the config
  # header is included with <config.h>
  # (system header include)
  includes = ["."]
)

LIB_SRCS_UNIX = [
  "dbus/dbus-uuidgen.c",
  "dbus/dbus-transport-unix.c",
  "dbus/dbus-server-unix.c",
]

LIB_SRCS = [
  "dbus/dbus-address.c",
  "dbus/dbus-auth.c",
  "dbus/dbus-bus.c",
  "dbus/dbus-connection.c",
  "dbus/dbus-credentials.c",
  "dbus/dbus-errors.c",
  "dbus/dbus-keyring.c",
  "dbus/dbus-marshal-header.c",
  "dbus/dbus-marshal-byteswap.c",
  "dbus/dbus-marshal-recursive.c",
  "dbus/dbus-marshal-validate.c",
  "dbus/dbus-message.c",
  "dbus/dbus-misc.c",
  "dbus/dbus-nonce.c",
  "dbus/dbus-object-tree.c",
  "dbus/dbus-pending-call.c",
  "dbus/dbus-resources.c",
  "dbus/dbus-server.c",
  "dbus/dbus-server-socket.c",
  "dbus/dbus-server-debug-pipe.c",
  "dbus/dbus-sha.c",
  "dbus/dbus-signature.c",
  "dbus/dbus-syntax.c",
  "dbus/dbus-timeout.c",
  "dbus/dbus-threads.c",
  "dbus/dbus-transport.c",
  "dbus/dbus-transport-socket.c",
  "dbus/dbus-watch.c",
] + LIB_SRCS_UNIX

LIB_SHARED_SRCS_UNIX = [
  "dbus/dbus-file-unix.c",
  "dbus/dbus-pipe-unix.c",
  "dbus/dbus-sysdeps-unix.c",
  "dbus/dbus-sysdeps-pthread.c",
  "dbus/dbus-userdb.c",
]

LIB_SHARED_SRCS = [
  "dbus/dbus-dataslot.c",
  "dbus/dbus-file.c",
  "dbus/dbus-hash.c",
  "dbus/dbus-internals.c",
  "dbus/dbus-list.c",
  "dbus/dbus-marshal-basic.c",
  "dbus/dbus-memory.c",
  "dbus/dbus-mempool.c",
  "dbus/dbus-string.c",
  "dbus/dbus-sysdeps.c",
  "dbus/dbus-pipe.c",
] + LIB_SHARED_SRCS_UNIX

LIB_HDRS_UNIX = [
  "dbus/dbus-server-launchd.h",
]

LIB_HDRS = [
  "dbus/dbus-auth.h",
  "dbus/dbus-connection-internal.h",
  "dbus/dbus-credentials.h",
  "dbus/dbus-keyring.h",
  "dbus/dbus-marshal-header.h",
  "dbus/dbus-marshal-byteswap.h",
  "dbus/dbus-marshal-recursive.h",
  "dbus/dbus-marshal-validate.h",
  "dbus/dbus-message-internal.h",
  "dbus/dbus-message-private.h",
  "dbus/dbus-misc.h",
  "dbus/dbus-nonce.h",
  "dbus/dbus-object-tree.h",
  "dbus/dbus-protocol.h",
  "dbus/dbus-pending-call-internal.h",
  "dbus/dbus-resources.h",
  "dbus/dbus-server-socket.h",
  "dbus/dbus-server-debug-pipe.h",
  "dbus/dbus-server-protected.h",
  "dbus/dbus-sha.h",
  "dbus/dbus-timeout.h",
  "dbus/dbus-threads.h",
  "dbus/dbus-threads-internal.h",
  "dbus/dbus-transport.h",
  "dbus/dbus-transport-protected.h",
  "dbus/dbus-transport-socket.h",
  "dbus/dbus-uuidgen.h",
  "dbus/dbus-watch.h",
] + LIB_HDRS_UNIX

LIB_SHARED_HDRS_UNIX = [
  "dbus/dbus-transport-unix.h",
  "dbus/dbus-sysdeps-unix.h",
  "dbus/dbus-userdb.h",
]

LIB_SHARED_HDRS_EMBEDDED_TESTS = [
  "dbus/dbus-test-tap.h",
]

LIB_SHARED_HDRS = [
  "dbus/dbus-dataslot.h",
  "dbus/dbus-file.h",
  "dbus/dbus-hash.h",
  "dbus/dbus-internals.h",
  "dbus/dbus-list.h",
  "dbus/dbus-macros-internal.h",
  "dbus/dbus-marshal-basic.h",
  "dbus/dbus-mempool.h",
  "dbus/dbus-string.h",
  "dbus/dbus-string-private.h",
  "dbus/dbus-pipe.h",
  "dbus/dbus-sysdeps.h",
  "dbus/dbus-valgrind-internal.h",
  # Actually LIB_SHARED_HDRS_EMBEDDED_TESTS are only required
  # if DBUS_ENABLE_EMBEDDED_TESTS is set.
] + LIB_SHARED_HDRS_UNIX + LIB_SHARED_HDRS_EMBEDDED_TESTS

# These headers are required but it is unclear
# why, because the native build system doesn't
# list them explicitly. See also the variable
# DBUS_UTIL_HEADERS
REQUIRED_HEADERS = [
  "dbus/dbus-test.h",
  "dbus/dbus-mainloop.h",
]

cc_library(
  name = "dbus",
  hdrs = [
    "dbus/dbus.h",
    "dbus/dbus-address.h",
    "dbus/dbus-bus.h",
    "dbus/dbus-connection.h",
    "dbus/dbus-errors.h",
    "dbus/dbus-macros.h",
    "dbus/dbus-memory.h",
    "dbus/dbus-message.h",
    "dbus/dbus-misc.h",
    "dbus/dbus-pending-call.h",
    "dbus/dbus-protocol.h",
    "dbus/dbus-server.h",
    "dbus/dbus-shared.h",
    "dbus/dbus-signature.h",
    "dbus/dbus-syntax.h",
    "dbus/dbus-threads.h",
    "dbus/dbus-types.h",
  ],
  srcs =
      LIB_SRCS
    + LIB_SHARED_SRCS
    + LIB_HDRS
    + LIB_SHARED_HDRS
    + REQUIRED_HEADERS,
  deps = [
    ":config",
    ":arch_deps",
  ],
  defines = [
    "DBUS_COMPILATION",
  ],
  includes = ["."],
  visibility = [ "//visibility:public" ],
)
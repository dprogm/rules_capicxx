exports_files([
  "src/dbus-patches/capi-dbus-add-send-with-reply-set-notify.patch",
  "src/dbus-patches/capi-dbus-add-support-for-custom-marshalling.patch",
  "src/dbus-patches/capi-dbus-block-acquire-io-path-on-send.patch",
  "src/dbus-patches/capi-dbus-correct-dbus-connection-block-pending-call.patch",
  "src/dbus-patches/capi-dbus-send-with-reply-and-block-delete-reply-on-error.patch",
])

cc_library(
  name = "capicxx_dbus_runtime",
  hdrs = glob([
    "include/CommonAPI/DBus/*.hpp",
  ]) + [
    "include/murmurhash/MurmurHash3.h",
    "include/pugixml/pugiconfig.hpp",
    "include/pugixml/pugixml.hpp",
  ],
  srcs = glob([
    "src/CommonAPI/DBus/*.cpp",
    "src/pugixml/*.cpp",
    "src/murmurhash/*.cpp",
  ], exclude = [
    # Don't compile the main loop related files.
    # They are not macOS compatible because the
    # implementation uses <sys/eventfd.h> which
    # is linux specific. This needs to be fixed
    # first. Compilation succeeds but won't link.
    # TODO Create a patch.
    "src/CommonAPI/DBus/DBusMainLoopContext.cpp",
    "src/CommonAPI/DBus/DBusMainLoop.cpp",
  ]),
  deps = [
    "@com_github_covesa_capicxx_core_runtime//:capicxx_core_runtime",
    "@org_freedesktop_gitlab_dbus//:dbus",
  ],
  includes = [ "include" ],
  visibility = [ "//visibility:public" ],
)

configure = rule(
  implementation = _configure_impl,
  attrs = {
    "_config_generator": attr.label(
      default = Label("//tools:config_generator"),
      allow_single_file = True,
      executable = True,
      cfg = "exec",
    ),
  },
)
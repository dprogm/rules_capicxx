def _configure_impl(ctx):

  args = ctx.actions.args()
  args.add("--input", ctx.file.input.path)
  args.add("--output", ctx.outputs.output.path)
  args.add_all(ctx.files.configs)

  ctx.actions.run(
    executable = ctx.executable._config_generator,
    arguments = [args],
    inputs = ctx.files.configs + ctx.files.input,
    outputs = [ctx.outputs.output],
    progress_message = "Generating file for %s" % ctx.file.input.short_path,
  )

configure = rule(
  implementation = _configure_impl,
  attrs = {
    "_config_generator": attr.label(
      default = Label("//tools:config_generator"),
      allow_files = True,
      executable = True,
      cfg = "exec",
    ),
    "input": attr.label(
      allow_single_file = True,
      mandatory = True,
    ),
    "configs": attr.label_list(
      allow_files = True,
    ),
    "output": attr.output(
      mandatory = True,
    ),
  },
)
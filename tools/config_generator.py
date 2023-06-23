import configparser
import argparse
import json
import re
from typing import Dict, List
from pathlib import Path
from textwrap import dedent

try:
  # Only available in versions 3.11 upwards
  import tomllib
except ImportError:
  has_tomllib = False
  print(dedent('''
        Warning: Your platform doesn't support *.toml natively.
        Please consider using an alternative for providing
        variable substitutions.''').strip('\n'))
else:
  has_tomllib = True

def parse_vars_from_toml(toml_file_path : Path) -> Dict[str,str]:
  with open(toml_file_path, 'rb') as toml_file:
    try:
      return tomllib.load(toml_file)
    except tomllib.TOMLDecodeError:
      return { }

def parse_vars_from_json(json_file_path : Path) -> Dict[str,str]:
  with open(json_file_path) as json_file:
    try:
      return json.load(json_file)
    except json.decoder.JSONDecodeError:
      return { }

def parse_vars_from_config(config_file_path : Path) -> Dict[str,str]:
  # Allow duplicate sections. This ensures no error is
  # thrown if the config file additionally contains the
  # '_hidden_' section.
  config = configparser.ConfigParser(strict = False)
  with open(config_file_path) as config_file:
    # There should be at least one section present in
    # the config file in order to parse successfully.
    # Insert an arbitrary section name.
    try:
      config.read_string("[_hidden_]\n" + config_file.read())
    except configparser.ParsingError:
      return { }
  key_val_pairs : Dict[str,str] = { }
  for sec in config.sections():
    for key, val in config.items(sec):
      # Check if the user provides a case-sensitive name
      # with an associated value.
      # TODO Extend the regex to support a wider range.
      m = re.match('([a-zA-Z0-9_]+)=([a-zA-Z0-9_=]+)', val)
      if m:
        key_val_pairs.update({m.group(1) : m.group(2)})
      else:
        key_val_pairs.update({key.upper() : val})
  return key_val_pairs

def parse_vars(vars_file_path : Path) -> Dict[str,str]:
  if not vars_file_path.exists():
    return { }
  as_str = lambda from_dict : {k : str(v) for (k,v) in from_dict.items()}
  if vars_file_path.suffix == '.toml':
    if not has_tomllib:
      return { }
    return as_str(parse_vars_from_toml(vars_file_path))
  if vars_file_path.suffix == '.json':
    return as_str(parse_vars_from_json(vars_file_path))
  if vars_file_path.suffix == '.conf':
    return parse_vars_from_config(vars_file_path)
  if not vars_file_path.suffix:
    with open(vars_file_path) as vars_file:
      return {vars_file_path.name : vars_file.read()}
  # Other formats are not supported
  return { }

def get_vars(var_file_paths : List[str]) -> Dict[str,str]:
  merged_vars : Dict[str,str] = { }
  for var_file_path in var_file_paths:
    merged_vars.update(parse_vars(Path(var_file_path)))
  return merged_vars

def replace_cmake_defines(line : str, variables : Dict[str,str]) -> str:
  ''' Implements exactly the same logic as CMake 'configure_file' does.
  The algorithm is roughly identical to the CMake one. Please refer to
  the official CMake documentation for further information.
  '''
  m = re.search('#([ \t]*)cmakedefine([ \t]+)([A-Za-z_0-9]*)', line)
  if m:
    var_name = m.group(3)
    if variables.get(var_name):
      return '#' + m.group(1) + 'define' + m.group(2) + var_name + line[m.end():]
    return '/* #undef ' + var_name + ' */' + '\n' if line.endswith('\n') else ''
  m = re.search('#([ \t]*)cmakedefine01([ \t]+)([A-Za-z_0-9]*)', line)
  if m:
    var_name = m.group(3)
    out = '#' + m.group(1) + 'define' + m.group(2) + var_name
    if variables.get(var_name):
      out += ' 1'
    else:
      out += ' 0'
    out += '\n' if line.endswith('\n') else ''
    return out
  return line

def replace_variables(line : str, variables : Dict[str,str]) -> str:
  ''' Replace all variable occurrences by its associated value.
  The implemented logic shall comply with the CMake implementation.
  However there is no additional meaning of $CACHE{VAR} and $ENV{VAR}
  in this context, which means they are treated as normal variables.
  '''
  var_patterns = [
    '\$\{([A-Za-z_0-9]*)\}',
    '@([A-Za-z_0-9]*)@',
    '\$CACHE\{([A-Za-z_0-9]*)\}',
    '\$ENV\{([A-Za-z_0-9]*)\}']
  out = line
  for var_pattern in var_patterns:
    m = re.search(var_pattern, out)
    cur = ''
    idx = 0
    while m:
      cur += out[idx:idx+m.start()]
      idx = idx + m.end()
      var = m.group(1)
      val = variables.get(var)
      if val:
        cur += val
      else:
        cur += ''
      m = re.search(var_pattern, out[idx:])
    out = cur + out[idx:]
  return out

def main():
  parser = argparse.ArgumentParser(
    description = '''Substitutes variables defined in the input file by its values defined in the passed
                     variables file. It has the same semantics as the CMake function 'configure_file' and
                     supports the variables @VAR@, ${VAR}, $CACHE{VAR} or $ENV{VAR}. The handling of
                     CMake defines like '#cmakedefine VAR ...' is identical to the CMake implementation.
                  ''')

  parser.add_argument('--input', required = True,
    help = 'The input file path which contains the variables that should be substituted, e.g. config.h.in')
  parser.add_argument('--output', required = True,
    help = 'The output file path. Here the resulting output file will be stored, e.g. config.h')
  parser.add_argument('vars', nargs = '*',
    help = '''The variables file paths. This can either be a *.json, *.toml or *.conf (INI) file.
              It contains key/value pairs where the key corresponds to the variable which should
              be substituted and the value that replaces the variable. Note that keys in INI files
              are case-insensitive. They are automatically converted into an uppercase string by
              convention. If you want to prefer a case-sensitive variable name write the key/value
              pair like this 'var_name:new_var_name=value' or 'var_name=new_var_name=value. Using
              an '=' in the value requires the latter syntax. Sections are not required. The json
              should consist of a flat object. Values are stored as strings. This also applies to
              toml files. If the given file doesn't have a file extension it is treated as a single
              variable where the file name is the variables name and the value is the file content.
           ''')

  args = parser.parse_args()

  variables = get_vars(args.vars)
  if not variables:
    print(dedent(f'''
          No variables found in file {args.vars}.
          * Does the file exist?
          * Maybe you did not provide a valid configuration file?
          -> Check whether there is a warning emitted.''').strip('\n'))
    return

  input_file_path = Path(args.input)
  if not input_file_path.exists():
    print(f'Input file at {input_file_path} does not exist!')
    return

  with open(input_file_path) as input_file:
    out = ''
    for line in input_file.readlines():
      replaced = replace_cmake_defines(line, variables)
      if replaced:
        out += replace_variables(replaced, variables)
    if out:
      with open(args.output, 'w') as output_file:
        output_file.write(out)

if __name__ == '__main__':
  main()
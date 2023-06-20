import configparser
import argparse
import json
from typing import Dict
from pathlib import Path

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
    except  configparser.ParsingError:
      return { }
  key_val_pairs : Dict[str,str] = { }
  for sec in config.sections():
    for key, val in config.items(sec):
      key_val_pairs.update({key.upper() : val})
  return key_val_pairs

def parse_vars(vars_file_path : Path) -> Dict[str,str]:
  if not vars_file_path.exists():
    return { }
  if vars_file_path.suffix == '.json':
    return parse_vars_from_json(vars_file_path)
  else:
    return parse_vars_from_config(vars_file_path)

def main():
  parser = argparse.ArgumentParser(
    description = '''Substitutes variables defined in the input file by its values defined in the passed
                     variables file. It has the same semantics as the CMake function 'configure_file' and
                     supports the variables @VAR@, ${VAR}, $CACHE{VAR} or $ENV{VAR}. The handling of
                     CMake defines like '#cmakedefine VAR ...' is identical to the CMake implementation.
                  ''')

  parser.add_argument('--in', required = True,
    help = 'The input file path which contains the variables that should be substituted, e.g. config.h.in')
  parser.add_argument('--out', required = True,
    help = 'The output file path. Here the resulting output file will be stored, e.g. config.h')
  parser.add_argument('--vars', required = True,
    help = '''The variables file path. This should be a python-like config file (INI file syntax).
              It contains key/value pairs where the key corresponds to the variable which should
              be substituted and the value that replaces the variable. Because keys are case-insensitive
              they are automatically converted into an uppercase string. If you want to prefer a
              case-sensitive variable name write the key/value pair like this 'var:var=value'.
              EASY WAY: Another option is to pass a *.json that consists of a single object that
              contains the key/value pairs.
           ''')

  args = parser.parse_args()

if __name__ == '__main__':
  main()
#!/bin/python3
import sys

def retab_code(filepath, indent_level='  '):
  with open(filepath, 'r') as file:
    lines = file.readlines()

  retabbed_lines = []
  for line in lines:
    stripped_line = line.lstrip()
    indent = line[:len(line) - len(stripped_line)]
    retabbed_line = indent_level * (len(indent) // len(indent_level)) + stripped_line
    retabbed_lines.append(retabbed_line)

  with open(filepath, 'w') as file:
    file.writelines(retabbed_lines)

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print('Usage: python retab_code.py <filepath> [indent_level]')
    sys.exit(1)

  filepath = sys.argv[1]
  indent_level = sys.argv[2] if len(sys.argv) > 2 else '  '
  retab_code(filepath, indent_level)

#!/usr/bin/env python3
import sys

def search_strings(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open('lineno.txt', 'w') as output_file:
        strings = [line.strip() for line in f1.readlines()]
        for line_num, line in enumerate(f2, start=1):
            for string in strings:
                if string in line:
                    output_file.write(f'{line_num}\n')
                    break

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python search_strings.py <file1> <file2>')
        sys.exit(1)
    
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    search_strings(file1, file2)

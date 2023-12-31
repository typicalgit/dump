#!/usr/bin/env python3
import subprocess

def read_specific_line(file_path, line_number):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            while True:
                if 1 <= line_number <= len(lines):
                    line_to_read = lines[line_number - 1].strip()
                    subprocess.run(['espeak', line_to_read])
                else:
                    print("Invalid line number. Please enter a number within the range of the file's lines.")
                    line_number = int(input("Enter a new line number (or 'q' to quit): "))
                    continue

                new_line_number = input("Enter a new line number (or 'q' to quit): ")
                if new_line_number.lower() == 'q':
                    break
                else:
                    try:
                        line_number = int(new_line_number)
                    except ValueError:
                        print("Invalid input. Please enter a valid line number.")
                        continue

    except FileNotFoundError:
        print("File not found. Please enter a valid file path.")

if __name__ == "__main__":
    file_path = input("Enter the file path: ")
    line_number = input("Enter the line number: ")

    try:
        line_number = int(line_number)
        if line_number <= 0:
            print("Invalid input. Please enter a positive integer for the line number.")
        else:
            read_specific_line(file_path, line_number)
    except ValueError:
        print("Invalid input. Please enter a valid line number.")

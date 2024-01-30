#!/usr/bin/env python3
import sys
import subprocess

def convert_special_char(char):
    special_chars = {
        "'": "single quote",
        '"': "double quote",
        "`": "backtick",
        "!": "exclamation mark",
        "@": "at sign",
        "#": "hash",
        "$": "dollar sign",
        "%": "percent",
        "^": "caret",
        "&": "ampersand",
        "*": "asterisk",
        "(": "left parenthesis",
        ")": "right parenthesis",
        "-": "dash",
        "_": "underscore",
        "=": "equals",
        "+": "plus",
        "[": "left bracket",
        "]": "right bracket",
        "{": "left brace",
        "}": "right brace",
        "|": "pipe",
        "\\": "backslash",
        ";": "semicolon",
        ":": "colon",
        ",": "comma",
        ".": "dot",
        "<": "less than",
        ">": "greater than",
        "/": "slash",
        "?": "question mark",
        " ": "space"
    }
    return special_chars.get(char, char)

def speak_text(text):
    subprocess.call(["espeak", text])

def process_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        for char in text:
            word = convert_special_char(char)
            speak_text(word)

def process_string(input_string):
    for char in input_string:
        word = convert_special_char(char)
        speak_text(word)

# Check if a file or string is provided as an argument
if len(sys.argv) > 1:
    arg = sys.argv[1]
    if arg.endswith('.txt'):
        process_file(arg)
    else:
        process_string(arg)
else:
    print("Please provide a file or string as an argument.")

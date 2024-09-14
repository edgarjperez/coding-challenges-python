#!/usr/bin/env python3
from io import BufferedReader
import sys

def main(buffer:BufferedReader, option:str='default'):

    if option == '-c':
       return get_bytes(buffer)
    elif option == '-l':
       return get_lines(buffer)
    elif option == '-w':
       return get_words(buffer)
    elif option == '-m':
       return get_characters(buffer)
    else:
       return get_default(buffer)

def get_bytes(buffer:BufferedReader) -> str:
    return f" {len(buffer)} "

def get_lines(buffer:BufferedReader) -> str:
    return f" {len(buffer.splitlines())} "

def get_words(buffer:BufferedReader) -> str:
    return f" {len(buffer.split())} "

def get_characters(buffer:BufferedReader) -> str:
    decoded = buffer.decode('utf-8')
    chars = len(decoded)
    return f" {chars} "

def get_default(buffer:str) -> str:
    return f"{get_bytes(buffer)}{get_lines(buffer)}{get_words(buffer)}{get_characters(buffer)}"
        

if __name__ == "__main__":
    if len(sys.argv) > 2:
        with open(sys.argv[2], 'rb') as file:
            print(f"{main(file.read(), sys.argv[1])} {sys.argv[2]}")
    else:
        if len(sys.argv) > 1:
            print(f"{main(sys.stdin.buffer.read(), sys.argv[1])}")
        else:
            print(f"{main(sys.stdin.buffer.read())}")
    

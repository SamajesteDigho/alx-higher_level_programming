#!/usr/bin/python3
import hidden_4 as file
if __name__ == "__main__":
    for name in dir(file):
        if name[:2] != '__':
            print(name)

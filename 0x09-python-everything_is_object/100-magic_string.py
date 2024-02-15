#!/usr/bin/python3
def magic_string():
    magic_string.nb = magic_string.nb + 1 if hasattr(magic_string, "nb") else 1
    return ", ".join(["BestSchool" for _ in range(magic_string.nb)])

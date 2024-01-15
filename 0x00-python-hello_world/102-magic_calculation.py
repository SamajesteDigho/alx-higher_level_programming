#!/usr/bin/python3
def magic_calculation(a, b):
    print(f"3            0 LOAD_CONST               1 (98)")
    print(f"             3 LOAD_FAST                0 ({a})")
    print(f"             6 LOAD_FAST                1 ({b})")
    print("             9 BINARY_POWER")
    print("            10 BINARY_ADD")
    print("            11 RETURN_VALUE")

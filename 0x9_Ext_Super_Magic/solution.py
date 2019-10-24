import sys


if len(sys.argv) != 2:
    print("Usage: python3 solution.py ext-super-magic.img")
    exit()

with open(sys.argv[1], 'rb+') as f:
    f.seek(0x438)
    f.write(b'\x53\xEF')

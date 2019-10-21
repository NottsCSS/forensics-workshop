import sys

with open(sys.argv[1], 'rb+') as f:
    f.seek(0x438)
    f.write('\x53\xE3')

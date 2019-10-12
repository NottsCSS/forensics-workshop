import sys

with open(sys.argv[1], 'rb') as f:
    data = f.read()

for n in range(8):
    data_offset = data[n:]

    # get all least significant bits
    lsbs = []
    for d in data_offset:
        lsbs.append(d & 1)

    # group lsbs in groups of 8
    chars = [lsbs[i:i+8] for i in range(0, len(lsbs), 8)]


    # join chars and print it
    flag = [''.join([str(a) for a in c]) for c in chars]
    flag = [chr(int(f, 2)) for f in flag]
    flag = ''.join(flag)

    if 'picoCTF' in flag:
        print(flag)
        break

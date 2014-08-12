import sys

__author__ = 'Eric'


def move(packets):
    avg = sum(packets) / len(packets)

    if avg != sum(packets) // len(packets):
        return -1

    dist = 0
    for i in range(len(packets)):
        dist += abs(packets[i] - avg)

    return int(dist / 2)

def main():
    while True:
        n = int(sys.stdin.readline())
        if n == -1:
            sys.exit(0)

        packs = []
        for i in range(n):
            packs.append(int(sys.stdin.readline()))
        print(move(packs))

if __name__ == '__main__':
    main()
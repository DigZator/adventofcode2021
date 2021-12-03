def most_common_bit(lines, bit):
    ones = sum(int(line[bit]) for line in lines)
    zeros = len(line) - ones
    mcb = ''
    if (ones == zeros):
        mcb

#https://github.com/kodsnack/advent_of_code_2021/blob/main/cernael-python/3b.py

if __name__ == '__main__':
    lines = []
    with open('input.txt') as f:
        for line in f.readlines():
            print(line)
            lines.append(line.strip())
    print(lines)

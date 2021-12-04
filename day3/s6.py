def most_common_bit(lines, bit):
    ones = sum(int(line[bit]) for line in lines)
    zeros = len(lines) - ones
    mcb = ''
    if (ones == zeros):
        mcb = 'b'
    elif (ones > zeros):
        mcb = '1'
    elif (zeros > ones):
        mcb = '0'
    return mcb

def oxy(lines):
    for bit in range(len(lines[0])):
        mcb = most_common_bit(lines, bit)
        lines = list(filter((lambda l: (l[bit] == mcb) or (l[bit] == '1' and mcb == 'b')) ,lines))
        #print(bit, lines,mcb)
        if (len(lines) == 1):
            return int(lines[0],2)

def car(lines):
    for bit in range(len(lines[0])):
        mcb = most_common_bit(lines, bit)
        lines = list(filter((lambda l: (l[bit] != mcb and mcb != 'b') or (l[bit] == '0' and mcb == 'b')) ,lines))
        #print(bit, lines, mcb)
        if (len(lines) == 1):
            return int(lines[0],2)

if __name__ == '__main__':
    lines = []
    with open('input.txt') as f:
        for line in f.readlines():
            lines.append(line.strip())
    oxy_num = oxy(lines)
    car_num = car(lines)
    power = oxy_num*car_num
    print("Oxygen Generator - ", oxy_num)
    print("CO2 Scrubber     - ", car_num)
    print("Power            - ", power)
    #933 3622 3379326
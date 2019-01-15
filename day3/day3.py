with open('day3.txt', 'r') as fp:
    read_file = fp.read()
houses = set()
x, y = 0, 0

houses.add((0, 0))
for c in read_file:
    if c == '^':
        x+=1
    elif c == 'v':
        x-=1
    elif c == '>':
        y-=1
    elif c == '<':
        y+=1
    houses.add((x, y))



print(len(houses))
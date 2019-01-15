def move(x, y):
    if c == '^':
        x += 1
    elif c == 'v':
        x -= 1
    elif c == '>':
        y -= 1
    elif c == '<':
        y += 1
    return x, y

with open('day3.txt', 'r') as fp:
    read_file = fp.read()
houses = set()
xs, ys = 0, 0
xr, yr =0, 0
houses.add((0, 0))
i = 0
for c in read_file:
    if i == 0:
        xs, ys = move(xs, ys)
        i = 1
        houses.add((xs, ys))
    else:
        xr, yr = move(xr, yr)
        i = 0
        houses.add((xr, yr))



print(len(houses))
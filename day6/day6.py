# set with lights
lights = set()
with open('day6.txt', "r") as fp:
    for line in fp:
        # split line, sizes
        line_split = line.split()
        if len(line_split) > 4:
            x1,y1 = [int(x) for x in line_split[2].split(',')]
            x2, y2 = [int(x) for x in line_split[4].split(',')]

            # add lights to set
            if line_split[1] == 'on':
                for x in range(x1,x2+1):
                    for y in range(y1, y2+1):
                        lights.add((x,y))
            # remove lights from set
            elif line_split[1] == 'off':
                for x in range(x1,x2+1):
                    for y in range(y1, y2+1):
                        if (x,y) in lights:
                            lights.remove((x,y))
        # toogle lights in set
        elif line_split[0] == 'toggle':
            x1,y1 = [int(x) for x in line_split[1].split(',')]
            x2, y2 = [int(x) for x in line_split[3].split(',')]
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    if (x, y) in lights:
                        lights.remove((x, y))
                    else:
                        lights.add((x,y))


print(len(lights))
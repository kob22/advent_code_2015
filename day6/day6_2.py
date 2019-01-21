import re
import numpy as np
import time


def count_dict(fp):
    """count lights with dict"""
    lights = dict()
    for line in fp:
        # line split
        line_split = line.split()
        # check is it turn off/on or toggle
        if len(line_split) > 4:
            # split sizes
            x1,y1 = [int(x) for x in line_split[2].split(',')]
            x2, y2 = [int(x) for x in line_split[4].split(',')]
            # lights on
            if line_split[1] == 'on':
                for x in range(x1,x2+1):
                    for y in range(y1, y2+1):

                        lights[(x,y)] = lights.get((x,y), 0) +1
            # ligts off
            elif line_split[1] == 'off':
                for x in range(x1,x2+1):
                    for y in range(y1, y2+1):
                        if (x,y) in lights:
                            if lights[(x,y)] >1:
                                lights[(x,y)] -=1
                            else:
                                lights[(x,y)] =0
        # toggle
        elif line_split[0] == 'toggle':
            x1,y1 = [int(x) for x in line_split[1].split(',')]
            x2, y2 = [int(x) for x in line_split[3].split(',')]
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    lights[(x, y)] = lights.get((x, y), 0) + 2
    return sum(lights.values())


def count_np(fp):
    """Cunt lights with numpy"""
    # tab 1000 x 1000 with 0
    tab = np.zeros((1000, 1000,), 'int32')
    for line in fp:
        # split sizes
        line_split = line.split()
        if len(line_split) > 4:
            x1,y1 = [int(x) for x in line_split[2].split(',')]
            x2, y2 = [int(x) for x in line_split[4].split(',')]
            # on
            if line_split[1] == 'on':
                tab[x1:x2+1, y1:y2+1]+=1
            # off
            elif line_split[1] == 'off':
                tab[x1:x2 + 1, y1:y2 + 1] -= 1
                tab[tab < 0 ] = 0
        # toogle
        elif line_split[0] == 'toggle':
            x1,y1 = [int(x) for x in line_split[1].split(',')]
            x2, y2 = [int(x) for x in line_split[3].split(',')]
            tab[x1:x2 + 1, y1:y2 + 1] += 2
    return np.sum(tab)


# count lights and measuring time
with open('day6.txt', "r") as fp:
    start = time.time()
    print(count_dict(fp))
    end = time.time()
    print(end - start)
with open('day6.txt', "r") as fp:
    start = time.time()
    print(count_np(fp))
    end = time.time()
    print(end - start)



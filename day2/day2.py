def calc(l, w ,h):
    a = [l*w, w*h, h*l]
    c = [x*2 for x in a]
    return sum([x*2 for x in a]) + min(a)

def ribbon(l, w, h):

    return 2*l + 2*w + 2*h - 2*max([l,w,h]) + (l*w*h)

sum_total = 0
total_ribbon = 0
with open('day2.txt', 'r') as fp:
    for line in fp:
        l, w, h = map(int, line.split('x'))
        gift = calc(l, w, h)
        sum_total+=gift
        total_ribbon+= ribbon(l, w, h)
print(sum_total)
print(total_ribbon)

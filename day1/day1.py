with open('day1.txt', 'r') as fp:
    read_file = fp.read()

basement = 0
floor = 0
i=0
while i < len(read_file) and floor > -1:
    if read_file[i] == '(':
        floor += 1
    elif read_file[i] == ')':
        floor -= 1
    i += 1

print(i)

print(read_file.count('(') - read_file.count(')'))
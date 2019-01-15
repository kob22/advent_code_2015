import re


def is_nice_string(word):
    not_nice = ['ab', 'cd', 'pq', 'xy']
    for xy in not_nice:
        if xy in word:
            return False

    if len(re.split(r'[aeiou]', word)) < 4:
        return False

    if not re.search(r"([a-z])\1", word):
        return False

    return True


def is_nice_string2(word):

    if not re.search(r'([a-z][a-z]).*\1', word):
        return False
    if not re.search((r'([a-z])[a-z]\1'), word):
        return False

    return True


num_nice = 0
num_nice2 = 0
with open('day5.txt', 'r') as fp:
    for line in fp:
        if is_nice_string(line):
            num_nice+=1

        if is_nice_string2(line):
            num_nice2+=1

print(num_nice)
print(num_nice2)
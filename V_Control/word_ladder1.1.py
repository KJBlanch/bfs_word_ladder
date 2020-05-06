import re


def same(item, target):
    return len([c for (c, t) in zip(item, target) if c == t])


def build(pattern, words, seen, list):
    return [word for word in words
            if re.search(pattern, word) and word not in seen.keys() and word not in list]


def find(word, words, seen, target, path, finalpath, count):
    list = []
    for i in range(len(word)):
        list += build(word[:i] + "." + word[i + 1:], words, seen, list)
    if len(list) == 0:
        return False
    list = sorted([(same(w, target), w) for w in list])



fname = input("Enter dictionary name: ")
file = open(fname)
lines = file.readlines()
while True:
    start = input("Enter start word:")
    words = []
    for line in lines:
        word = line.rstrip()
        if len(word) == len(start):
            words.append(word)
    target = input("Enter target word:")
    break

count = len(lines)
path = [start]
seen = {start: True}
finalpath = []
if find(start, words, seen, target, path, finalpath, count):
    path.append(target)
    print(len(path) - 1, path)
else:
    print("No path found")
print(finalpath)

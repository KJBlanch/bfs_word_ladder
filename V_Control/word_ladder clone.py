import re
def same(item, target):
  return len([c for (c, t) in zip(item, target) if c == t])

def build(pattern, words, seen, list):
  return [word for word in words
                 if re.search(pattern, word) and word not in seen and word not in list]

def find(word, words, seen, target, path):
  list = []
  for i in range(len(word)):
    list += build(word[:i] + "." + word[i + 1:], words, seen, list)
  if len(list) == 0:
    return
  list = sorted([(same(w, target), w) for w in list])
  for (match, item) in list:
    if match == len(target) - 1:
      currentPath = path[:]
      currentPath.append(target)
      paths.setdefault(len(currentPath)-1, []).append(currentPath)
  for (match, item) in list:
    seen.add(item)
    path.append(item)
    find(item, words, seen, target, path)
    seen.remove(item)
    path.pop()

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

count = 0
path = [start]
seen = set(start)
if find(start, words, seen, target, path):
  path.append(target)
  print(len(path) - 1, path)
else:
  print("No path found")


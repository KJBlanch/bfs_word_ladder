import re
def same(item, target):
  return len([c for (c, t) in zip(item, target) if c == t])

def build(pattern, words, seen, list):
  return [word for word in words
                 if re.search(pattern, word) and word not in seen.keys() and word not in list]

def shortfind(word, words, seen, target, path, pathhit):
  list = []
  for i in range(len(word)):
    list += build(word[:i] + "." + word[i + 1:], words, seen, list)
  if len(list) == 0:
    return False
  list = sorted([(same(w, target), w) for w in list])
  for (match, item) in list:
    if len(pathhit) > len(path):
      if match == len(target):
        print(path)
        path.append(item)
        pathhit = path
        seen[item] = True
        path.pop()
        seen.pop(item)
        print("listmatch")
        print (len(pathhit))

      elif match == len(target) - 1:
        print(path)
        path.append(item)
        path.append(target)
        pathhit = path
        seen[item] = True
        path.pop()
        seen.pop(item)
        print("match")
        print (len(pathhit))
  else:
      seen[item]=True

  for (match, item) in list:
    print("Pathlength: ",len(path))
    print("Pathhitlength: ",len(pathhit))
    if match != 0:
      if len(pathhit) > len(path):
        seen[item] = True
        path.append(item)
        if shortfind(item, words, seen, target, path, pathhit):
          return True
      else:
        seen[item]=True
        seen.pop(item)
    else:
      if len(path) >= 1:


#Okay. Because you're getting tired. Here's where you're at.
#You've got it cylcing through every iteration possible. You need to make it more efficient for the short path. If it lucks onto a short one, stay there. Try again.

def allfind(word, words, seen, target, path):
  list = []
  batchlist = []
  for i in range(len(word)):
    list += build(word[:i] + "." + word[i + 1:], words, seen, list)
  if len(list) == 0:
    return False
  list = sorted([(same(w, target), w) for w in list])
  for (match, item) in list:

    if match == len(target):
      path.append(item)
      print(path, target)
      batchlist.append((path))
      seen[item] = True
      path.pop()
      print("List Hit")
      seen.pop(item)

    elif match == len(target) - 1:
      path.append(item)
      print(path, target)
      batchlist.append((path))
      seen[item] = True
      path.pop()
      print("Hit")
      seen.pop(item)

  for (match, item) in list:
    seen[item] = True
    path.append(item)
    if allfind(item, words, seen, target, path, path):
      return True
    print(path)
    path.pop()
    seen.pop(item)


#Afname = input("Enter dictionary name: ")
file = open('dictionary.txt')
lines = file.readlines()
while True:
  start = input("Enter start word:")
  words = []
  pathhit = words
  for line in lines:
    word = line.rstrip()
    if len(word) == len(start):
      words.append(word)
  target = input("Enter target word:")
  break

count = 0
path = [start]

seen = {start : True}
if shortfind(start, words, seen, target, path, pathhit):
  print(len(pathhit) - 1, pathhit)
else:
  print("No path found")

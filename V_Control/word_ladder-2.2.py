import re



#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



class buildsame:

    def __init__(self, item, target, words,):
        self.item = item
        self.target = target
        self.words = words
#initialises the variables used.

    def get_item(self):
        return self.item

#returns the current search item

    def hit_target(self, target):
        return self.target == target


#returns true if target found.

    def get_successors(self, current_item):
        successors = set()
        for i in range(len(current_item)):
            pattern = current_item[:i] + "." + current_item[i + 1:]
            successors |= set([words for words in self.words if re.search(pattern, words)])
#creates a series of possible items if they match the search corriculum (I.e, lead = _ead, l_ead, le_d, lea_.)
#returns this as a set, if they match the pattern and are in the words list.

        return_list = list(successors)
        return_list.remove(current_item)
        return return_list

#This class tidies up the same and build functions by keeping it contained within a single class.
#get_successors works exactly the same as the list build function, except it works only on the current list item.
#See documentation (Class 'Shortfind') for more information.

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



def bfs_shortfind(buildsame):
#This variable is the first in, first out query.
    open_set = []

# an empty set to maintain the visited pathways.
    visited_path = set()

# a dictionary to maintain current_path information ->(parent, action to reach successor)
    current_path = dict()

# initialize
    item = buildsame.get_item()
    current_path[item] = None
    open_set.append(item)
    visited_path.add(item)

# For each node on the current level expand and process, if no succesors, then unwind
# If no successors, end the program.
    while open_set.count != []:
        try:
            current_item = open_set.pop(0)
        except:
            break

# Target found - return path (use current_path_rebuild to reverse the current_path)
        if buildsame.hit_target(current_item):
            return current_path_rebuild(current_item, current_path)

# For each successor of the current item;
        for next in buildsame.get_successors(current_item):

# The successor has been visited, so continue.
            if next in visited_path:
                continue

# And if it hasn't been visited, then we move to the next successor
            if next not in open_set:
                current_path[next] = current_item# add the next item to the current_path
                open_set.append(next)  # Adds it to the query variable

# The current item has been processed, so add to the visited path
        visited_path.add(current_item)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


def bfs_allfind(buildsame):

# This variable is the first in, first out queue.
    open_set = []
# Maintains all visited paths.
    visited_path = set()
# a dictionary to maintain current_path information -> (parent, action to reach successor)
    current_path = dict()

# initialize
    item = buildsame.get_item()
    current_path[item] = None
    open_set.append(item)
    visited_path.add(item)

# For each node on the current level expand and process, if no succesors, then unwind
# If no successors, end the program.
    while open_set.count != []:
        try:
            current_item = open_set.pop(0)
        except:
            break

# For each successor of the current item;

        for next in buildsame.get_successors(current_item):

# For each successor of the current tree process (this uses the lookforward method,
# based of the match function in the original ladder)
# If target hit, then print the path as viable (rebuild the path, plus the current successor that has hit the target,
# and the target)
# Move onto the next
# Do not end the program

            if next == target:
                return_path = []
                return_path = current_path_rebuild(current_item, current_path)
                return_path += current_item, target
                print(return_path)

# The successor has been visited, so continue.
            if next in visited_path:
                continue

# And if it hasn't been visited, then we move to the next successor
            if next not in open_set:
                current_path[next] = current_item # adds the next item to the current path
                open_set.append(next)  # adds it to the query variable as well


# The current item has been processed, so add to the visited path
        visited_path.add(current_item)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



def current_path_rebuild(state, current_path):
    rebuild = list()
# reverse the current_path dictionary all the way back to the start word (which should have the state 'None')
# any current_item which has None will not be added. This prevents all non-used items being added to the rebuild.
    while current_path[state] is not None:
        state = current_path[state]
        rebuild.append(state)
    rebuild.reverse()
    return rebuild
#** For allpath function, the path has to be ammended with the successor that has the match (n-1),
# as it has not been added to the current_path.


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


#Inputselection goes here (1/2 for Shortest/All)



    #fname = input("Enter dictionary name: ")
print("Enter Dictionary Name")
file = open("dictionary.txt")

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

#This starts the shortfind, returns the result
print("Processing Shortest Pathway...")
stw = buildsame(start, target, words)
result = bfs_shortfind(stw)
try:
    result.append(target)
    print("Shortest")
    pathlength = len(result)-1
    print(pathlength, "Steps.", result)
except:
    print("No Path Found")



#This starts the allfind. Currently, results are printed from the function as it comes across the correct paths.


print("Processing All Pathways...")
stw = buildsame(start, target, words)
bfs_allfind(stw)
print("All Paths Found")


#2.1 Comments
#Known issues -
#All paths has bugs
#Needs input selection and sanitation (almost finished)
#Haven't fixed the overbuffer.

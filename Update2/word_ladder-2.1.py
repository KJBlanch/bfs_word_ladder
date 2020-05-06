import re

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

    def get_successors(self, next_item):
        successors = set()
        for i in range(len(next_item)):
            pattern = next_item[:i] + "." + next_item[i + 1:]
            successors |= set([words for words in self.words if re.search(pattern, words)])
#creates a series of possible items if they match the search corriculum (I.e, lead = _ead, l_ead, le_d, lea_.
#returns this as a set, if they match the pattern and are in the words list.

        return_list = list(successors)
        return_list.remove(next_item)
        return return_list

#This class tidies up the same and build functions by keeping it contained within a single class.
#get_successors works exactly the same as the list build function, except it works only on the current list item.
#See documentation (Class 'Shortfind') for more information.

#//////////////////////////////////////////////////////////////////////////


def bfs_shortfind(buildsame):
#This variable is the first in, first out query.
    open_set = []

# an empty set to maintain the visited pathways.
    visited_path = set()

# a dictionary to maintain meta information (used for path formation)
# **
# key -> (parent state, action to reach child)
    meta = dict()

# initialize
    item = buildsame.get_item()
    meta[item] = None
    open_set.append(item)
    visited_path.add(item)

# For each node on the current level expand and process, if no children
# (leaf) then unwind
    while open_set.count != []:
        next_item = open_set.pop(0)

# We found the node we wanted so stop and emit a path.
        if buildsame.hit_target(next_item):
            return construct_path(next_item, meta)

# For each child of the current tree process
        for next in buildsame.get_successors(next_item):

# The node has already been processed, so skip over it
            if next in visited_path:
                continue

# The child is not enqueued to be processed, so enqueue this level of
# children to be expanded
            if next not in open_set:
                meta[next] = next_item# create metadata for these nodes
                open_set.append(next)  # enqueue these nodes

# We finished processing the root of this subtree, so add it to the closed
# set
        visited_path.add(next_item)

#//////////////////////////////////////////////////////////////////////////////////////

#def bfs_allfind(buildsame):

def bfs_allfind(buildsame, pathlist):

    pathlist = []
#This value holds all available paths.

    open_set = []
# This variable is the first in, first out query.

    visited_path = set()
#Maintains all visited paths.
    meta = dict()
# a dictionary to maintain meta information (used for path formation)
# **
# key -> (parent state, action to reach child)

# initialize
    item = buildsame.get_item()
    meta[item] = None
    open_set.append(item)
    visited_path.add(item)


    while open_set.count != []:
        next_item = open_set.pop(0)
# For each node on the current level expand and process, if no children
# (leaf) then unwind


        if buildsame.hit_target(next_item):
            pathlist += construct_path(next_item, meta)
            print(pathlist)
# We found the node we wanted so add the path to the pathlist (need to work out continue).



        for next in buildsame.get_successors(next_item):
# For each child of the current tree process


            if next in visited_path:
                continue
# The node has already been processed, so skip over it

            if next not in open_set:
                meta[next] = next_item # create metadata for these nodes
                open_set.append(next)  # enqueue these nodes
# The child is not enqueued to be processed, so enqueue this level of
# children to be expanded

        visited_path.add(next_item)
# We finished processing the root of this subtree, so add it to the closed
# set





def construct_path(state, meta):
    action_list = list()
# Produce a backtrace of the actions taken to find the goal node, using the
# recorded meta dictionary

# Continue until you reach root meta data (i.e. (None, None))
    while meta[state] is not None:
        state = meta[state]
        action_list.append(state)

    action_list.reverse()
    return action_list



#Inputselection goes here (1/2 for Shortest/All)



#fname = input("Enter dictionary name: ")
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
tsp = buildsame(start, target, words)
result = bfs_shortfind(tsp)
result.append(target)
print("Shortest")
print(f"{len(result) - 1} steps.  {result}")

#This starts the allfind. Currently, results are printed from the function as it comes across the correct paths.

pathlist = []
print("Processing All Pathways...")
tsp = buildsame(start, target, words)
result = bfs_allfind(tsp, pathlist)
result.append(target)
print("BAM! Gottim")
for path in pathlist:
    print(path, target)


#2.1 Comments
#Known issues - Allfind doesn't progress past the last node of the branch. This is because no rollback is enabled
#in the 'once found' function.
#Needs input selection and sanitation
#Haven't fixed the overbuffer.
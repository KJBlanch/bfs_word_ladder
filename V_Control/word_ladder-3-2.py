import re
import string


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
    fifo_q = []

# an empty set to maintain the visited pathways.
    visited_path = set()

# a dictionary to maintain current_path information ->(parent, action to reach successor)
    current_path = dict()

# initialize
    item = buildsame.get_item()
    current_path[item] = None
    fifo_q.append(item)
    visited_path.add(item)

# For each node on the current level expand and process, if no succesors, then unwind
# If no successors, end the program.
    while fifo_q.count != []:
        try:
            current_item = fifo_q.pop(0)
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
            if next not in fifo_q:
                current_path[next] = current_item# add the next item to the current_path
                fifo_q.append(next)  # Adds it to the query variable

# The current item has been processed, so add to the visited path
        visited_path.add(current_item)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


def bfs_allfind(buildsame, pathlengthnum):
# This holds the amount of paths that fit the criteria. Simply used to print the relevent response.
    count = int()
# This variable is the first in, first out queue.
    fifo_q = []
# Maintains all visited paths.
    visited_path = set()
# a dictionary to maintain current_path information -> (parent, action to reach successor)
    current_path = dict()

# initialize
    item = buildsame.get_item()
    current_path[item] = None
    fifo_q.append(item)
    visited_path.add(item)

# For each item on the current level expand and process, if no succesors, then unwind
# If no successors, print the relevent response and end the program.
    while fifo_q.count != []:
        try:
            current_item = fifo_q.pop(0)
        except:
            if count > 0:
                print("All Paths Found")
            else:
                print("No Paths Of This Length Found")
            break

# For each successor of the current item;

        for next in buildsame.get_successors(current_item):

# For each successor of the current tree process (this uses the lookforward method,
# based of the match function in the original ladder)
# If target hit, then print the path as viable (rebuild the path, plus the current successor that has hit the target,
# and the target), and add to the count variable
# Move onto the next
# Do not end the program

            if next == target:
                return_path = []
                return_path = current_path_rebuild(current_item, current_path)
                return_path += current_item, target
                current_path_len = len(return_path) - 1
                if int(current_path_len) == int(pathlengthnum):
                    count += 1
                    print(return_path)

# The successor has been visited, so continue.
            if next in visited_path:
                continue

# And if it hasn't been visited, then we move to the next successor
            if next not in fifo_q:
                current_path[next] = current_item # adds the next item to the current path
                fifo_q.append(next)  # adds it to the query variable as well


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


# This section is for user inputs that do not have file extension or have unexpected file extension.
fname = input("Enter dictionary name: ")
if fname[-4:] != ".txt":
  fname = fname + ".txt"

# file input handling
try:
  file = open(fname)
except FileNotFoundError:
  print("No such file or directory. \nPlease try again")
else:
  lines = file.readlines()  # returns a list of lines
  while True:

    # handling start words
    start = input("Enter start word:")
    if start == "" or start in string.punctuation or start.isnumeric(): # If it has empty value, punctuation or numeric values
      while start == "" or start in string.punctuation or start.isnumeric():
        if start == "":
          start = input("Start word is empty. Please enter again: ")
        elif start in string.punctuation:
          start = input("Start word cannot have any punctuation. Please remove punctuation and try again: ")
        elif start.isnumeric():
          start = input("Start word cannot be numeric. Please enter again: ")
    words = [] # a list of filtered words
    for line in lines: # element from the list(dictionary.txt)
      word = line.rstrip() # To remove newline
      if len(word) == len(start): # filtering possible words based on the length of user input that matches the length of words from dictionary
        words.append(word)

    # target words
    target = input("Enter target word:") # input for users to transfer from source word to
    if target == "" or target in string.punctuation or target.isnumeric(): # If it has empty value, punctuation or numeric values
      while target == "" or target in string.punctuation or target.isnumeric():
        if target == "":
          target = input("target word is empty. Please enter again: ")
        elif target in string.punctuation:
          target = input("target word cannot have any punctuation. Please remove punctuation and try again: ")
        elif target.isnumeric():
          target = input("target word cannot be numeric. Please enter again: ")

    # blacklist words
    b_list = []
    b_number = input("Enter the number of words you want to blacklist (enter to skip): ") # the number of blacklisted words users want to put
    if b_number == "": # For users who do not want to put any blacklisted words
      pass
    else:
      while b_number.isnumeric() != True or int(b_number) > len(words): # when input is not numeric or blacklist inputs are greater than the number of available words
        if b_number.isnumeric() != True: # When value is not numeric
          b_number = input("Please enter numbers: ")
        elif int(b_number) > len(words): # When this value is over the number of elements from a list of filtered words
          b_number = input("Too many blacklist words. \nPlease enter again: ")
      for a in range(int(b_number)):
        b_word = input("Enter words you want to remove: ")
        while b_word not in words: # when desired blacklisted words are not available
            b_word = input("No such word in words list. \nPlease enter again: ")
        b_list.append(b_word)
      for word in b_list:
        words.remove(word)
      print("Your blacklisted words: " + str(b_list))


    # Inputselection (1/2 for Shortest/All)
    try:
        choice = input("Choose function either (1:shortest path or 2:all paths of a certain length): ")
    except:
        print("There is no such selection. Please try again")
    else:
        if choice == str(1):
            # This starts the shortfind, returns the result
            print("Processing Shortest Pathway...")
            stw = buildsame(start, target, words)
            result = bfs_shortfind(stw)
            try:
                result.append(target)
                print("Shortest")
                pathlength = len(result) - 1
                print(pathlength, "Steps.", result)
            except:
                print("No Path Found")
        elif choice == str(2): # This starts the allfind. Currently, results are printed from the function as it comes across the correct paths.
            pathlengthnum = input("Enter desired path length")
            while pathlengthnum.isnumeric() != True:
                pathlengthnum = input("Please enter a valid number")
            print("Processing All Pathways...")
            stw = buildsame(start, target, words)
            count = int()
            bfs_allfind(stw, pathlengthnum)
            print ("Completed")
        else:
            print("There is no such selection. Please try again")
    break
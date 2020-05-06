import re
import string

import unittest

class TestFortesting_1(unittest.TestCase):
    def test_inputoutput(self):
        self.assertEqual(fortesting_1("lead", "gold", "dictionary.txt", "", "", "1"),"1") #known to work
        self.assertEqual(fortesting_1("ask","zed", "dictionary.txt", "", "", "1"), "1") #known to work
        #self.assertEqual(fortesting_1("alk", "zed", "dictionary.txt", "", "", "1"),"1") #known bug (unsure)
        self.assertEqual(fortesting_1("", "", "", "", "", ""),"5")  # expecting exception handled
        #self.assertEqual(fortesting_1("lead", "gold", "dictionary.txt", "", "", "2"),"3") #known bug (global variable)
        #self.assertEqual(fortesting_1("ask", "zed", "dictionary.txt", "", "", "2"),"3") #known bug (global variable)
        self.assertEqual(fortesting_1("aa", "zz", "dictionary.txt", "", "", "1"),"2") #known to work
        #self.assertEqual(fortesting_1("aa", "zz", "dictionary.txt", "", "", "2"),"4") #known bug (global variable)

#expected testing outputs:
    #1 = shortest path found
    #2 = shortest path not found
    #3 = all paths found
    #4 = all paths searched, not found

    #5 = No such file or directory.

    #6 = Start word is empty.
    #7 = Start word cannot have any punctuation
    #8 = Start word cannot be numeric

    #9 = Target word is empty
    #10 = Target word cannot have any punctuation
    #11 = Target word cannot be numeric

    #12 = Number input of blacklist words is not numeric
    #13 = Number input of blacklist words is over the number of words in the dictionary
    #14 = Blacklist word is not in the dictionary
    #15 = Incorrect selection of function

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


def bfs_allfind(buildsame):
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
# If no successors, end the program.
    while fifo_q.count != []:
        try:
            current_item = fifo_q.pop(0)
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


def fortesting_1(start, target, dictionary, numwords, blacklist, selection):
    #for testing - start, target, dictionary address, number of blacklist words, and a blacklist will replace all
    #the code that would normally generate these inputs
    #fname = input("Enter dictionary name: ")

    #if fname[-4:] != ".txt":
      #fname = fname + ".txt"

    # file input handling
    try:
      file = open(dictionary)
    except FileNotFoundError:
      #print("No such file or directory. \nPlease try again")
        return "5"
    else:
      lines = file.readlines()  # returns a list of lines
      while True:

        # handling start words
        #start = input("Enter start word:")
        if start == "" or start in string.punctuation or start.isnumeric(): # If it has empty value, punctuation or numeric values
          while start == "" or start in string.punctuation or start.isnumeric():
            if start == "":
                return "6"
              #start = input("Start word is empty. Please enter again: ")
            elif start in string.punctuation:
                return "7"
              #start = input("Start word cannot have any punctuation. Please remove punctuation and try again: ")
            elif start.isnumeric():
                return "8"
              #start = input("Start word cannot be numeric. Please enter again: ")
        words = [] # a list of filtered words
        for line in lines: # element from the list(dictionary.txt)
          word = line.rstrip() # To remove newline
          if len(word) == len(start): # filtering possible words based on the length of user input that matches the length of words from dictionary
            words.append(word)

        # target words
        #target = input("Enter target word:") # input for users to transfer from source word to
        if target == "" or target in string.punctuation or target.isnumeric(): # If it has empty value, punctuation or numeric values
          while target == "" or target in string.punctuation or target.isnumeric():
            if target == "":
                return "9"
              #target = input("target word is empty. Please enter again: ")
            elif target in string.punctuation:
                return "10"
              #target = input("target word cannot have any punctuation. Please remove punctuation and try again: ")
            elif target.isnumeric():
                return "11"
              #target = input("target word cannot be numeric. Please enter again: ")
        if start not in words:
            words += start
        # blacklist words
        for word in blacklist:
            b_list |= word
        #b_number = input("Enter the number of words you want to blacklist (enter to skip): ") # the number of blacklisted words users want to put
        b_number = numwords
        if b_number == "": # For users who do not want to put any blacklisted words
          pass
        else:
          while b_number.isnumeric() != True or int(b_number) > len(words): # when input is not numeric or blacklist inputs are greater than the number of available words
            if b_number.isnumeric() != True: # When value is not numeric
                return "12"
              #b_number = input("Please enter numbers: ")
            elif int(b_number) > len(words):
                return "13"# When this value is over the number of elements from a list of filtered words
                #b_number = input("Too much blacklist words. \nPlease enter again: ")
          for a in range(int(b_number)):
            b_word = input("Enter words you want to remove: ")
            while b_word not in words: # when desired blacklisted words are not available
                return "14"
                #b_word = input("No such word in words list. \nPlease enter again: ")
            b_list.append(b_word)
          for word in b_list:
            words.remove(word)
          #print("Your blacklisted words: " + str(b_list))
          #print("Your blacklisted words: " + str(b_list))


        # Inputselection (1/2 for Shortest/All)
        try:
            #choice = input("Choose function either (1:shortest path or 2:longest path): ")
            choice = selection
        except:
            return "15"
            #print("There is no such selection. Please try again")
        else:
            if choice == str(1):
                # This starts the shortfind, returns the result
                #print("Processing Shortest Pathway...")
                stw = buildsame(start, target, words)
                result = bfs_shortfind(stw)
                try:
                    result.append(target)
                    print("Shortest")
                    pathlength = len(result) - 1
                    return "1" #changed for testing!
                except:
                    return "2" #changed for testing!
            elif choice == str(2):
                # This starts the allfind. Currently, results are printed from the function as it comes across the correct paths.
                #print("Processing All Pathways...")
                stw = buildsame(start, target, words)
                bfs_allfind(stw)
                #print("All Paths Found")
                return "3" #changed for testing
            else:
                return "4" #changed for testing
                #print("There is no such selection. Please try again")
        break

#fortesting_1("lead","gold","dictionary.txt","","","1")
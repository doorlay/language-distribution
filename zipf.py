from hash_table import *
import string
import sys

def create_frequency_table(filename):
    """
    Creates a Hash Table that stores all words from the input file, along with that words number of appearences.
    This data is stored in a tuple within the hash table, the word itself acting as the key for hashing.
    Example: '("test", 13)' would represent the word 'test' appearing 13 times in the input file.

    Parameters:
    filename - the name of the input file for which the frequency table will be created for

    Returns:
    hsh - a hash table object that will hold all of the words and their cooresponding frequencies

    """

    hsh = HashTable(100) 
    line_count = 0
    try:
        with open(filename, 'r') as f:
            for line in f:
                line_count += 1
            f.close()
    except:
        raise FileNotFoundError
    f = open(filename, "r")
    line_number = 0
    for line in f:      # iterates through every line in the input file
        line_number += 1
        new_word = ""
        character_count = len(line)
        character_number = 0
        for character in line:      # iterates through every character in each line of input file
            character_number += 1
            # Ensure the character is a valid character for a word, not a number or puctuation
            if (ord(character) >= 65 and ord(character) <= 90) or (ord(character) >= 97 and ord(character) <= 122):
                new_word += character
                # Ensure to end the word and add to hash table if at the last character of the last line
                if line_number == line_count:
                    if character_count == character_number:
                        new_word = new_word.lower()
                        if new_word != "":
                            hsh.insert(new_word)
                        new_word = ""
            # Checks if the character is not an apostrophy 
            elif ord(character) != 39:
                new_word = new_word.lower()
                if new_word != "":
                    hsh.insert(new_word)
                new_word = ""
    return hsh

def order_words(hash_table):
    """
    Takes all words from the hash table and puts them in a list, sorted by their frequencies

    Parameters:
    hash_table - hash table object that contains tuples of all words and frequencies from input file

    Returns:
    lst_of_words - a list of all words from the input file, sorted by their frequency

    """

    lst_of_words = []
    for item in hash_table.hash_table:
        if item != None:
            lst_of_words.append(item)
    lst_of_words.sort(key = lambda x: x[1],reverse=True)
    return lst_of_words

def check_zipf(lst,output_file):
    """ 

    """
    output_file = open(output_file, "w")
    most_freq_word = lst[0]
    for word in lst:
        if word != most_freq_word: # to ensure that most frequent word is not compared to itself
            pass

def main():
    if len(sys.argv) != 3:
        print("Expected usage: zipf.py [inputfile.txt] [outputfile.txt]")
    else:
        input_file = open(sys.argv[1], "r")
        output_file = open(sys.argv[2], "w")
        lst_of_words = order_words(create_frequency_table(input_file))
        check_zipf(lst_of_words,output_file)


# the end goal will be to use something like BeautifulSoup with python to scrape a bunch of data off of the web and then process it into an output here, checking
# to see if Zipf's law applies. That would be a pretty cool project to finish.
# I can implement this with flask and have it become a website. That would be pretty cool.

"""
How do I want to output all of my data? An output file may be nice.

How do I want to account for punctuation?
What characters could be within a word that do not make it seperate. I suppose a dash can count something as one word.

"""
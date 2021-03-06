from hash_table import *

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

def mapN(in_file,out_file):
    """
    Given the frequency list, checks if the words map against zipf's law
    
    Parameters:
    file_name - the name of the file to map

    Returns:

    """
    word_data = order_words(create_frequency_table(in_file))
    counter = 1
    most_freq = word_data[0][1]
    for tup in word_data:
        expected = (most_freq / counter) // 1
        percent_error = abs(expected - tup[1]) / most_freq * 100
        out_file.write("{}\n - Expected: {}\n - Actual: {}\n - Percent Error: {}%\n".format(tup[0].capitalize(),int(expected),tup[1],round(percent_error,2)))
        counter += 1

def main():
    input_file = input("File name: ")
    f = open("out.txt", "w")
    mapN(input_file,f)
    f.close()

main()

# End goal will be to use BeautifulSoup to scrape web data
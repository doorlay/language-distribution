from hash_table import *
import string

def get_word_frequencies(filename):
    """ Read words from input text file (filename) and insert them into the concordance hash table, 
    after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
    Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
    Starting size of hash table should be 191: self.concordance_table = HashTable(191)
    Process of adding new line numbers for a word (key) in the concordance:
    If word is in table, get current value (list of line numbers), append new line number, insert (key, value)
    If word is not in table, insert (key, value), where value is a Python List with the line number
    If file does not exist, raise FileNotFoundError"""

    hsh = HashTable(191)
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
    for line in f:
        line_number += 1
        new_word = ""
        character_count = len(line)
        character_number = 0
        for character in line:
            character_number += 1
            if (ord(character) >= 65 and ord(character) <= 90) or (ord(character) >= 97 and ord(character) <= 122):
                new_word += character
                if line_number == line_count:
                    if character_count == character_number:
                        new_word = new_word.lower()
                        if new_word != "":
                            # i need to check here if the words are already in the table. Do I though?
                            hsh.insert(new_word)
                        new_word = ""
            elif ord(character) == 39:
                pass
            else:
                new_word = new_word.lower()
                if new_word != "":
                    # i need to check here if the words are already in the table. Do I though?
                    hsh.insert(new_word)
                new_word = ""
    return hsh



h = get_word_frequencies("preamble.txt")
lst = h.hash_table
for item in lst:
    if item != None:
        print(item)


"""
1. It appears that there are currently a lot of duplicate words in the table, so yes, I do need to be checking for dups before I add.
2. Additionally, a lot of random single letters are being added, such as "t", "d", "s", and so on.
3. Make sure I am accounting for punctuation correctly with this implementation.

"""


# the end goal will be to use something like BeautifulSoup with python to scrape a bunch of data off of the web and then process it into an output here, checking
# to see if Zipf's law applies. That would be a pretty cool project to finish.
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
    try:
        f = open(filename, "r")
    except:
        raise FileNotFoundError
    for line in f:
        new_word = ""
        for character in line:
            if (ord(character) >= 65 and ord(character) <= 90) or (ord(character) >= 97 and ord(character) <= 122):
                new_word += character
            elif ord(character) == 39:
                pass
            else:
                new_word = new_word.lower()
                if new_word != "":
                    # i need to check here if the words are already in the table. Do I though?
                    hsh.insert(new_word)
                new_word = ""
    return hsh

h = get_word_frequencies("lotr.txt")
print('test')


"""
1. It appears that there are currently a lot of duplicate words in the table, so yes, I do need to be checking for dups before I add.
2. Additionally, a lot of random single letters are being added, such as "t", "d", "s", and so on.
3. Make sure I am accounting for punctuation correctly with this implementation.

"""

# I'm going to keep a hash table of every word that appears, and using that hash table I'm going to map everything out and plot word frequency and such.

# hash table has a key and a value. 

# the key will be the word, the value will be the frequency of that word. They will be stored in tuple? Is that efficient? not really.
# ex. ('cat', 14)
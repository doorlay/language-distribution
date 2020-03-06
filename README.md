# language-distribution
Checks frequency of word appearances in a text document, maps against Zipf's law

Zipf's law states that a logarithmic distribution appears in many things in life, one of these being language.
According to Zipf's law, the most used word in any language shows up twice as frequently as the second most used. 
It also shows up three times as much as the third most used word, continuing said Zipfian pattern. 

This program is going to be designed to count the frequency of words to check this in .txt documents.

Will be implemented using a HashTable
the key will be the word, the value will be the frequency of that word. They will be stored in tuple
ex. ('cat', 14)
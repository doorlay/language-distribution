# Zipf's law mapper
Checks frequency of word appearances in a text document, maps against Zipf's law

Zipf's law states that a logarithmic distribution appears in many things in life, one of these being language.
According to Zipf's law, the most used word in any language shows up twice as frequently as the second most used. 
It also shows up three times as much as the third most used word, continuing said Zipfian pattern. 

This program is going to be designed to count the frequency of words to check this in .txt documents.

The word frequency storage is implemented with a HashTable in Python.

This Data is then fed into an R program that plots this data onto a Logarithmic Graph, checking how tightly the words map.
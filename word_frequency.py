from collections import Counter
import string
import re
import unicodedata

def getOnlyWords(originalWords):
    actualWords = []
    for word in originalWords:
        print(word.translate(str.maketrans('', '', string.punctuation)))
    return actualWords

def convert_accents(text):
    accepted_accents = {u'\N{COMBINING TILDE}',}
    return ''.join(c for c in unicodedata.normalize('NFKD', text) 
                    if unicodedata.category(c) != 'Mn' or c in accepted_accents)

def splitToAcceptedWords(fileText):
    # sub -> quita los caracteres que no sean letras ni digitos
    # lower -> uppercase to lowercase
    # split -> separa cuando hay espacios
    return convert_accents(re.sub(pattern="[^\w\s]", repl=" " ,string=fileText).lower()).split()

def word_count(fname):
        with open(fname) as f:
                #print(sorted(splitToAcceptedWords(f.read())))
                return Counter(splitToAcceptedWords(f.read()))

def print_results(wordsDic):
    sortedWords = sorted(wordsDic)
    totalFrequency = 0

    print('- - - - - - - - - - - - - - - - - - - - - - -')
    for word in sortedWords:
        totalFrequency += wordsDic[word]
        print(word, '\t\t', wordsDic[word])
    print('')
    print('- - - - - - - - - - - - - - - - - - - - - - -')
    print('')
    print("Número de palabras distintas: ", len(sortedWords))
    print("Suma total de frecuencias: ", totalFrequency)
    print('')

#print("Number of words in the file :", word_count("D:\joaqu\Documents\Joaquin Uni\TEC\Semestre 2021 - 2\RIT\mkdir.1"))

print('')
path = input("Ingresar dirección del archivo: ")
print_results(word_count(path))




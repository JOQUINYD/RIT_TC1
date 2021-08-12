from collections import Counter
import string
import re
import unicodedata
import os

def getOnlyWords(originalWords):
    actualWords = []
    for word in originalWords:
        print(word.translate(str.maketrans('', '', string.punctuation)))
    return actualWords

def convertAccents(text):
    accepted_accents = {u'\N{COMBINING TILDE}',}
    return ''.join(c for c in unicodedata.normalize('NFKD', text) 
                    if unicodedata.category(c) != 'Mn' or c in accepted_accents)

def splitToAcceptedWords(fileText):
    # sub -> quita los caracteres que no sean letras ni digitos
    # lower -> uppercase to lowercase
    # split -> separa cuando hay espacios
    return convertAccents(re.sub(pattern="[^\w\s]", repl=" " ,string=fileText).lower()).split()

def wordCount(fname):
    try:
        with open(fname, encoding='utf-8') as f:
                #print(splitToAcceptedWords(f.read()))
                return Counter(splitToAcceptedWords(f.read()))
    except:
        #if not utf-8 text file
        with open(fname) as f:
                #print(splitToAcceptedWords(f.read()))
                return Counter(splitToAcceptedWords(f.read()))

def printResults(wordsDic):
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

def saveResults(wordsDic):
    sortedWords = sorted(wordsDic)
    totalFrequency = 0

    textToSave = "- - - - - - - - - - - - - - - - - - - - - - -\n"
    for word in sortedWords:
        totalFrequency += wordsDic[word]
        textToSave += word + '\t\t' + str(wordsDic[word]) + '\n'
    textToSave += '\n'
    textToSave += "- - - - - - - - - - - - - - - - - - - - - - -\n"
    textToSave += '\n'
    textToSave += "Número de palabras distintas: " + str(len(sortedWords)) + '\n'
    textToSave += "Suma total de frecuencias: " + str(totalFrequency) + '\n'

    with open("results.txt", "w", encoding='utf-8') as f:
        f.write(textToSave)

#print("Number of words in the file :", word_count("D:\joaqu\Documents\Joaquin Uni\TEC\Semestre 2021 - 2\RIT\mkdir.1"))

def menu():
    print('')
    contProgram = input("Analizar frecuencias de archivos (Y/N): ")
    while(contProgram != 'N'):
        print('')
        path = input("Ingresar dirección del archivo: ")
        wordsDictionary = wordCount(path)
        printResults(wordsDictionary)
        saveResults(wordsDictionary)
        print("Resultados en archivo results.txt")
        print('')
        contProgram = input("Analizar frecuencias de archivos (Y/N): ")


menu()
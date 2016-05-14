import os
from os import walk

class OpenAndSearch:

    # open given file
    def openFile(self,path):
        f = open(path,"r")
        return f

    # seach given file
    def searchFile(self,givenWord,f):
        wordFoundInFile = False

        for line in f:
            for word in line.split():

                # strip all whitespaces and newlines from word
                word = word.lstrip()
                word = word.rstrip()

                # for some reason word comparison does not work
                # so need to do letter comparison
                letterInWord = 0

                for char in word:
                    # If all letters match we have found the word in the file
                    if(char == givenWord[letterInWord]):
                        letterInWord += 1
                        if(letterInWord >= len(givenWord)-1):
                            wordFoundInFile = True
                            break
                    else:
                        letterInWord = 0

        return wordFoundInFile

    # close given file
    def closeFile(self,f):
        f.close()

    # return all folder paths from working directory
    def getAllFolderPaths(self):
        f = []
        for (dirpath, dirnames, filenames) in walk(os.getcwd()):
            f.append(dirpath)
        return f
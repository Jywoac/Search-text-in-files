from Tools.scripts.treesync import raw_input
from OpenAndSearch import OpenAndSearch
from os import listdir
from os.path import isfile, join
import os
import mimetypes
import webbrowser

# program menus
class Menus(object):

    pathsToFilesWithFoundWords = []

    # ask for word to be searched in files
    def mainMenu(self):

        answer = False

        # while answer is not true (ex. no answer was given) get word from user
        while answer == False:
            wordToSearch = raw_input("Please write the word you want to search: ")

            if wordToSearch.isspace() == True:
                answer = False
                print("The word seems to be empty. Did you actually write something?")
            else:
                answer = True
                self.goThroughFilesInFolder(wordToSearch)

    # go through all files and find the word
    def goThroughFilesInFolder(self,word):

        searching = OpenAndSearch()

        # get all folder paths
        folderPaths = OpenAndSearch().getAllFolderPaths()

        # for each folder path in folderpaths get all files in folder
        # then open the files one by one and check for the word
        for fPath in folderPaths:
            onlyfiles = [f for f in listdir(fPath) if isfile(join(fPath, f))]
            for file in onlyfiles:

                path = fPath+"\\"+file

                fileToBeSearched = searching.openFile(fPath+"\\"+file)

                #check if type has text in it, if it does it can be searched
                mimeTypeTextTest = mimetypes.guess_type(path)[0]

                # check first if mimetype return value is text so it can be compared to "text"
                if(isinstance(mimeTypeTextTest, str)):
                    if("text" in mimeTypeTextTest):
                        if(searching.searchFile(word,fileToBeSearched) == True):
                            Menus.pathsToFilesWithFoundWords.append(path)
                    else:
                        pass
                else:
                    pass
                searching.closeFile(fileToBeSearched) # close file

        if not Menus.pathsToFilesWithFoundWords:
            # list is empty, no words were found
            print("That word was not found in any of the files.")
            raw_input("Press Enter to exit.")
        else:
            print("%d files have the word you are looking for." % Menus.pathsToFilesWithFoundWords.__len__())
            self.askAboutFileOpening()

    def askAboutFileOpening(self):

        print("Do you want to open just the first file or all files with that word?")

        ans = False
        chosenAnswer = 0

        while ans == False:

            chosenAnswer = raw_input("Write 1 for just first file, 2 for all files: ")

            try:
                chosenAnswer = int(chosenAnswer)
            except ValueError:
                print("Answer was not a number")

            # first check if answer is integer then check the other answer possibilities
            if(isinstance( chosenAnswer, int ) == True):
                if(chosenAnswer == 1):
                    # open notepad with the file
                    ans = True
                    osCommandString = "notepad.exe " + Menus.pathsToFilesWithFoundWords[0]
                    os.system(osCommandString)
                elif(chosenAnswer == 2):
                    # open all files with notepad
                    ans = True
                    for path in Menus.pathsToFilesWithFoundWords:
                        osCommandString = "notepad.exe " + path
                        os.system(osCommandString)

                elif(chosenAnswer > 2 or chosenAnswer < 1):
                    print("Answer was not 1 or 2")

            else:
                print("Answer was not 1 or 2")


#!/usr/bin/env python3

import bookentry
import os

class bookstoring(bookentry.entry):
    def __init__(self):
        super().__init__()
        self._path = "../storing/"

    def dataStore(self):
        # Get pandas dataframe
        df = self.dfGenerate()

        # Check path existance. If not, create a new path
        path = self._path
        isExist = os.path.exists(path)
        if not isExist:
            os.makedirs(path)
            print("storing directory is created!")

        filename = str(self._year) + ".xlsx"
        print(filename)
        fileExist = os.path.exists(path+filename)
        print(fileExist)
        self.dfView()



# Test script
if __name__ == '__main__':
    testData = bookstoring()
    dataIn = '''SAMS CLUB membership: $35
CVS sunscreekn spray: $15.49
Sam's Club daily necessities: $126.77
Target living necessities: $211.38
Rent: $851
Total: $1239.64'''
    testData.dataStore()

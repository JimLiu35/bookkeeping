import pandas as pd
import numpy as np
import sys
from datetime import date
import re

class entry:
    def __init__(self):
        '''Input: string
           Output: pandas dataframe'''
        self._df = pd.DataFrame()
        self._date = None
        self._year = date.today().year
        self._month = date.today().month

    def getEntry(self):
        msg = "Please Copy the ChatGPT Output Here (Press Ctrl+d to end):"
        print(msg)
        self._dataIn = sys.stdin.read()
        msg = "\nPlease Enter Date (YY-MM-DD), default to today's date by pressing D or d: "
        self._date = input(msg)
        if self._date == 'D' or self._date == 'd':
            self._date = date.today()

    def formatting(self):
        dataSplit = re.split(r'[:\n]', self._dataIn)
        items = []
        cost = []
        for element in dataSplit:
            itemsMatch = re.match('^[^\$]+', element)[0]
            costMatch = re.match('^[^A-Z]*', element)[0]
            if itemsMatch != ' ':
                items.append(itemsMatch)
            if costMatch != '':
                costMatch = re.sub('(\s\$)', '$', costMatch)
                cost.append(costMatch)

        d = {'date': self._date, 'items': items, 'costs': cost}
        dataframe = pd.DataFrame(data = d)
        self._df = dataframe
        return dataframe

    def dfGenerate(self):
        self.getEntry()
        self._df = self.formatting()
        return self._df

    def dfView(self):
        print(self._df)


## Test script
# if __name__ == '__main__':
#     testData = entry()
#     dataIn = '''SAMS CLUB membership: $35
# CVS sunscreekn spray: $15.49
# Sam's Club daily necessities: $126.77
# Target living necessities: $211.38
# Rent: $851
# Total: $1239.64'''
#     # today = "2023-07-08"    # Get today's date
#     testData.dfGenerate()

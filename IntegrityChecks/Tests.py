import csv

import pandas as pd
import xlrd

class ObjectTest:
    def __init__(self,bolean,area):
        self.bolean = bolean
        self.area = area # example:(1,1) found(1,2)
def convert_exel_csv(exelFile):
    read_file = pd.read_excel(exelFile)
    read_file.to_csv("Test.csv",index=None,header=True)
    df = pd.DataFrame(pd.read_csv("Test.csv"))
    print(df)


class Tests:
    def __init__(self):
        self.listObject = []
        with open("Test.csv",'r') as infile:
            csv_writer= csv.DictReader(infile)
            for row in csv_writer:
                self.listObject.append(ObjectTest(False, (row['X'],row['Y'])))

    def check_contain(self,listAlgoritm):
        #open file to read point
        for i in listAlgoritm:
            if i in listAlgoritm:
                self.listObject.append(0,1) #if point that algoritem found in area so bolean=true
            else:
                self.listObject.append(1,0) # bolean= false
    def Checking_successes(self):
        print("")
if __name__ == "__main__":
    a = Tests()
    #convert_exel_csv("15982 table.xlsx")



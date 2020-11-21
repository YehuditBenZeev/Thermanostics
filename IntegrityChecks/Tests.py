
class ObjectTest:
    def __init__(self, boolean, area):
        self.boolean = boolean
        self.area = area  # example:(1,1) found(1,2)


class Tests:
    def __init__(self):
        self.list = []
        # appending instances to list
        #read from file exel x,y
        #list.append(ObjectTest(false, 1))

    def check_contain(self, listAlgoritm):
        # open file to read point
        for i in listAlgoritm:
            if i in listAlgoritm:
                self.list.append(0, 1)  # if point that algoritem found in area so bolean=true
            else:
                self.list.append(1, 0)  # boolean= false

    def Checking_successes(self):
        print("")



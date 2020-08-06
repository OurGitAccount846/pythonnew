#multiple inheritance
class first(object):
    def __init__(self):
        self.str1="riya"
        print ("first")
class second(object):
    def __init__(self):
        self.str2="riya mary"
        print ("second")
class derived(first,second):
    def __init__(self):
        first.__init__(self)
        second.__init__(self)
        print("derived")
    def printStrings(self):
        print(self.str1, self.str2)
def main():
    a=derived()
    a.printStrings()
main()


        

   
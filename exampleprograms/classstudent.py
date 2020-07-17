class Student:
    def getDetails(self, name,rollno,std,section):
        self.name=name
        self.rollno=rollno
        self.std=std
        self.section=section
        return
    def printDetails(self):
        print(self.name)
        print(self.rollno)
        print(self.std)
        print(self.section)
        return
def main():
    a=Student()
    a.getDetails('riyamary','25','3rd std','E')
    a.printDetails()
main()


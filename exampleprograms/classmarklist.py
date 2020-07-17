class Studentmarklist:
    def getDetails(self,name,mark1,mark2,mark3,total,average):
        self.name=name
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
        self.total=total
        self.average=average
        self.total=self.mark1 +self.mark2 + self.mark3
        self.average=self.total / 3
    def printDetails(self):
        print(self.name)
        print(self.mark1)
        print(self.mark2)
        print(self.mark3)
        print("total is",self.total)
        print("average is",self.average)
        if(self.average>=50):
            print("student is pass")
        else:
            print("student is fail")
        return
def main():
    a=Studentmarklist()
    a.getDetails('riyamary',60,70,80,'', '' )
    a.printDetails()
main()


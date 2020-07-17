#dictionary get output in form of (x,x*x)
class value:
    
    def calculateValue(self,num):
        self.num=num
        return
    def showValue(self):
        self.num=int(input("enter number"))
        d=dict()
        for x in range(1,self.num+1):
            d[x]=x*x
        print(d)
   
def main():
    a=value()
    a.showValue()
    
main()

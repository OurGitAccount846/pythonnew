class supermarket:
    
    def getDetails(self,name,item,price):
        self.name=name
        self.item=item
        self.price=price
        return
    
    def printDetails(self):
        print(self.name)
        print(self.item)
        print(self.price)
        return
    
def main():
    a=supermarket()
    a.getDetails('reliance supermarket','apple','200')
    a.printDetails()
    
main()
             
             
             
          
               

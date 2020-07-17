class List:
    def getListname(self, names):
        self.names=names
        return
    def printListname(self):
        self.names=['nethra','sonakshi','lakshitha']
        for name in self.names:
            print('the name is {}'.format(name))
        
def main():
        a=List()
        a.printListname()
main()

class Dictionary:
    
    def getDictname(self, names):
        self.names=names
        return
    def printDictname(self):
        counts=dict()
        self.names=['nethra','sonakshi','lakshitha','nethra']
        for name in self.names:
            if name not in counts:
                counts[name]=1
            else:
                counts[name]=counts[name]+1
                print(counts)
    
def main():
        a=Dictionary()
        a.printDictname()
main()


class base(object):
    def __init__(self,a):
        self.a=a
class derived(base):
    def __init__(self,a,b):
        base.a=a
        self.b=b
    def print(self):
        print(base.a,self.b)
def main():
    X=derived(30,40)
    X.print()
main()
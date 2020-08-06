class base(object):
    def __init__(self,a):
        self.num=a
    def double(self):
        self.num*=2
class derived(base):
    def __init__(self,a):
        base.num=a
    def triple(self):
        self.num*=3
def main():
    X=derived(4)
    print(X.num)
    X.double()
    print(X.num)
    X.triple()
    print(X.num)
main()
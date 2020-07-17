#dictionary get output in form of (x,x*x)
def getResult(n):
    d=dict()
    for x in range(1,n+1):
        d[x]=x*x
    return d
    
def main():
    n=int(input("enter number"))
    value=getResult(n)
    print("number{} is {}".format(n,value))
main()


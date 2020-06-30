# while loop


def addingnumbers(*args):
    sum=0
    for var in args:
        sum=sum+var
    return sum
def bootstrap():
    sum =addingnumbers(1,2,3,5,6,7)
    print(sum)
    bootstrap()

  


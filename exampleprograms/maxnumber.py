#find maximum number among 3 numbers
def maxNum(x,y,z):
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    else:
        return z
def main():
    x=int(input("first number"))
    y=int(input("second number"))
    z=int(input("third number"))
    result=maxNum(x,y,z)
    print("maxNum of {} {} {} is {}".format(x,y,z,result))

main()

    
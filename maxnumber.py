def maxOfTwoNumbers(first,second):
    if(first>second):
        return first
    else:
        return second
def main():
    first=2
    second=9 
    third=4
    x=maxOfTwoNumbers(first,second)
    y=maxOfTwoNumbers(x,third)
    print("maxOfTwoNumbers {}{}{} is {}".format(first,second,third,y))
main()

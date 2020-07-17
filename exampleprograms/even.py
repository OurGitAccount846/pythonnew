#print the number is odd or even
def findNumber(num):
    if(num%2==0):
        return 'even no' 
    else:
        return 'odd no'
def main():
    num=int(input("enter number"))
    result=findNumber(num)
    print("findNumber of {} is {}".format(num,result))
main()
    
     
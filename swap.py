def swapNubersAdvance(num1,num2):
    num2=num1+num2
    num1=num2-num1
    num2=num2-num1
    print("befor swap a{} b{}".format(num1,num2))
    return
def main():
    num1=30
    num2=20
    print("befor swap a{} b{}".format(num1,num2))
    num1,num2=swap(num1,num2)
    print("befor swap a{} b{}".format(num1,num2))
main()    

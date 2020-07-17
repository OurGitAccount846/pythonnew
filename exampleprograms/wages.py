#get user wages and find happy or sad
def getSalary(salary):
    if(salary>=80):
        return 'I am happy' 
    else:
        return 'I am sad'
def main():
    salary=int(input("enter week wages"))
    result=getSalary(salary)
    print("getSalary of {} is {}".format(salary,result))
main()
     
def sumOfNumbers(numbers):
    total=0
    for number in numbers:
        total=total+number
        return total

def main():
    numbers=(1,2,3)
    result=sumOfNumbers(numbers)
    print("sumOfNumbers {}={}".format(numbers,result))
main()



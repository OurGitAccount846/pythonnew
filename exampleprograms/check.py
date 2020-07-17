#check a given key is in dictionary or not
def is_key_present(num):
    d={1:10,2:20,3:30,4:40} 
    if num in d:
        return 'key is present'
    else:
        return 'key is not present'
def main():
    num=int(input("enter number"))
    check=is_key_present(num)
    print("checking {} is {}".format(num,check))
main()


try:
    getNumber=int(input("enter number:"))
    reminder= getNumber % 2
    if(reminder==0):
     print('even number')
    else:
     print('odd')5
except:
    print('error')

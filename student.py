name=str(input("enter name of student"))
std=int(input("enter class"))
sec=str(input("enter section")
sub1=int(input("enter mark of first subject"))
sub2=int(input("enter mark of second subject"))
sub3=int(input("enter mark of third subject"))
sub4=int(input("enter mark of fourth subject"))
sub5=int(input("enter mark of fifth subject"))
average=(sub1+sub2+sub3+sub4+sub5)/5
if(average>=90):
    print("Result is GradeA")
elif(average>=80 and average<90):
    print("Result is GradeB")
else:
    print("Result is GradeC")
print("\t Student marklist \n **********************\n name\t\t:{}\n std\t\t:{}\n sec\t\t:{}\n ***********************\n sub1\t\t:{}\n sub2\t\t:{}\n sub3\t\t:{}\n sub4\t\t:{}\n sub5\t\t:{}\n ***************** \n average\t\t:{}\n ".format(name,std,
sec,sub1,sub2,sub3,sub4,sub5,average))


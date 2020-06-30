#takes 2 list and returns True if they have atleast one common letter

 commondata(list1,list2):
    result=False
    for x in list1:
        for y in list2:
            if x==y:
                result=True
                return result
    print(commondata[1,2,3],[3,4,5])
    print(commondata[1,2,3],[4,5,6])


num=[7,8,9,10,22]
num=[x for x in num if x%2!=0]
print(num)

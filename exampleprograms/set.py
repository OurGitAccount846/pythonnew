# find common vales in 3 sets

def IntersecOfSets(arr1,arr2,arr3):
    #converting arrays into sets
    s1=set(arr1)
    s2=set(arr2)
    s3=set(arr3)
    #calculate intersetion of s1 and s2
    set1=s1.intersection(s2)
    #calculate intersetion of set1 and s3
    result_set=set1.intersection(s3)
    #converting result set into list
    final_list=list(result_set)
    return final_list

def main():
    arr1=[1,5,10,20,40,80,100]
    arr2=[6,7,20,80,100]
    arr3=[3,4,15,20,30,70,80,120]
    result=IntersecOfSets(arr1,arr2,arr3)
    print("intersection is:",result)

main()




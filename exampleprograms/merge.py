def merge_Dict(dict1,dict2):
    result=dict2.update(dict1)
    return result 
def main():
    dict1={1:10,2:20}
    dict2={3:30,4:40}
    dict3=merge_Dict(dict1,dict2)
    print("after merging two dictionary is :",dict3)

main()





    
     
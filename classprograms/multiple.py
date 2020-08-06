class person(object):
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
class employee(object):
    def __init__(self,post,salary):
        self.post=post
        self.salary=salary
class leader(person,employee):
    def __init__(self,name,idnumber,post,salary):
        person.__init__(self,name,idnumber)
        employee.__init__(self,post,salary)
        print(" name:{}\n idnumber:{}\n post:{}\n salary:{}\n".format(self.name,self.idnumber,self.post,self.salary))
          
def main():
    a=leader('binu',34521,'manager',40000)
main()

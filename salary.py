name=str(input("enter name"))
basic=int(input("enter basic salary"))
if(basic<=3500):
    print('hra is 5%',(basic*0.05))
elif(basic<=10000):
    print('hra is 10%',(basic*0.10))
else:
    print('hra is 12%',(basic*0.12))
hra=float(basic*0.05 or basic*0.10 or basic*0.12)
ta=float(basic*0.12)
pf=float(basic*0.05)
crosssalary=float(pf+hra+ta)
deduction=float(pf+200)
netsalary=float(crosssalary-deduction)
print('ta',ta)
print('pf',pf)
print('crosssalary',crosssalary)
print('deduction',deduction)
print('netsalary',netsalary)


#####       Salary Calculator       #####

bs=int(input("Enter basic salary of employee= "))
if bs>=10000:
    hra=0.1*bs
    ta=0.05*bs
    bonus=2000
else:
    hra=1200
    ta=500
    bonus=1000
netsal=bs+hra+ta+bonus
print(f" Bs:- {bs}  \t HRA:- {hra}  \t TA:- {ta}    \t Bonus:- {bonus}  \t Netsalary:- {netsal}")

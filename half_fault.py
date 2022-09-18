num1=int(input("enter the first number= "))
num2=int(input("enter the second number= "))
opr=input("enter the operator= ")
if num1==45 and num2==3 and opr=='*' :
   print("555")

elif num1==56 and num2==9 and opr=='+' :
    print("77")

elif num1==56 and num2==6 and opr=='/':
    print("4")

elif opr=='+':
    ans=num1+num2
    print(f"{ans}")

elif opr=='*':
    ans = num1*num2
    print(f"{ans}")

elif opr=='/':
    ans = num1/num2
    print(f"{ans}")


elif opr=='-':
    ans = num1-num2
    print(f"{ans}")
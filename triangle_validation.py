s1=int(input("Enter the first side "))
s2=int(input("Enter the second side "))
s3=int(input("Enter the third side "))
if (s1+s2)>s3 and (s2+s3)>s1 and (s3+s1)>s2:
    print("Given side is valid and triangle is valid")
else:
    print("given sides is not valid and triangle is invalid")
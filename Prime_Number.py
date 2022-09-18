#####       Prime Number Using if else statement        #####

num = (int(input(" Enter the number: ")))
for i in range(2, num):
    if num % i == 0:
        print(num, " This is not a Prime Number")
        break  #Terminate the innermost loop
else:
    print(num, "This Number is a Prime number")


#####       Prime Number Using Variable     #####
num = (int(input(" Enter the number: ")))
for i in range(2, num):
    f=0
    if num % i == 0:
        print("This is not a Prime Number")
        f = 1
        break
if ( f==0 ) :
    print(num, "This Number is a Prime number")
else:
    print(num, "This is not a Prime Number")
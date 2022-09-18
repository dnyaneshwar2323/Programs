#Enter any 2 nos from user and print the nos between range
a,b =[int(x) for x in input("enter nos ").split()]

if a<b:
    for i in range (a,b+1):
        print(i,end=" ")
else:
    for i in range (a,b-1,-1):
        print(i,end=" ")



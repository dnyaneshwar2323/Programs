date=int(input("Enter the date "))
month=int(input("Enter the month "))
year=int(input("Enter the year "))
if date==1 and date<=30 and month==4 or month==6 or month==9 or month==11:
        print("Date is valid")
elif date==1 and date<=31 and month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        print("Date is valid")
elif date==1 and date<=28 and month==2:
        print("Date is valid")
elif date==29 and month ==2 and ((year%400==0 and year%100==0) or (year%4==0 and year%100!=0)):
        print("Date is valid")
else:
        print("Date is invalid")



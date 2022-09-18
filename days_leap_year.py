days=int(input("How any days in leap year? "))
if days==366:
    print("You have cleared the first level ")
    month=int(input("Which month has an a extra day in leap year? "))
    if month==2:
        print("Congratulations!!! You have cleared test")
    else:
        print("Sorry! You have failed the test")
else:
    print("Your input is wrong, Please try again")


#####       Identify Colours using Character        #####

#Enter any character from user and print corresponding colour name

color = input("Enter first character of color name : ")
if color == 'r' or color == 'R':
    print(" Color is Red ")
elif color == 'b' or color == 'B':
    print("Color is Black or Brown or Blue")
elif color == 'w' or color == 'W':
    print("Color is White")
elif color == 'y' or color == 'Y':
    print("Color is Yellow")
elif color == 'o' or color == 'O':
    print("Color is Orange")
elif color == 'g' or color == 'G':
    print("Color is Green or Grey")
else:
    print("It is Wrong Character Please enter correct Character")

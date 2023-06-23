##Elif Statement
a=int(input("enter the number"))
if a>=50:
    print("Given number is greater than 50")
elif a==50:
    print("Given number is equal than 50")
else:
    print("Given number is smaller than 50")


b=int(input("enter the number"))
if b==10:
    print("the value of b")
elif b==20:
    print("the value of b is given")
else:
    print("not given")

##Nested if
a=int(input("enter your mark"))
if a>=35:
    print("you are passed")
    if a>=70:
        print("you are passed in A grade")
    else:
        print("you are passed in B grade")
else:
    print("Arrear")
    

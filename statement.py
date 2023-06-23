##Mathematical Operation
##a=int(input("enter the value of a"))
##b=int(input("enter the value of b"))
##c=str(input("Enter the symbol"))
##if(c=="+"):
##    print(a+b)
##elif(c=="-"):
##    print(a-b)
##elif(c=="*"):
##    print(a*b)
##elif(c=="/"):
##    print(a/b)
##elif(c=="%"):
##    print(a%b)


##leap year
a=int(input("enter the year"))
if a/4 and a/400 and a/100:
    print("it is a leap year")
elif a/4 and a!=100:
    print("It is a leap year")
else:
    print("It is not a leap year")

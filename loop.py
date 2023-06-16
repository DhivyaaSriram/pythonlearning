####Odd value
stop=int(input("enter the stop value"))
for i in range (1,stop,2):
   if i%2!=0:
       print(i)
       
##Even value
stop=int(input("enter the value"))
for i in range (2,stop,2):
    if i%2==0:
       print(i)

##Reverse order for odd
stop=int(input("enter the stop value"))
for i in range (stop,0,-1):
  if i%2!=0:
        print(i)

####Reverse order for even
stop=int(input("enter the stop value"))
for i in range(stop,0,-1):
    if i%2!=0:
        print(i)

####Ocean in one line
for i in range(5):
    print("ocean",end=")
    
####Number in one line
for i in range(0,5):
   print("i value is",i)

####no
##for i in range(1,11):
    print(i,end=",")


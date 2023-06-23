rows=int(input("enter the rows value"))
for i in range(1,rows+1):
    for j in range(i):
        print("*",end=" ")
    print()


rows=int(input("enter the rows value"))
for i in range(rows):
    for j in range(rows-i-1):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()

rows=int(input("enter the rows value"))
for i in range(rows):
    for j in range(i,rows):
        print("*",end=" ")
    print()
        


rows=int(input("enter the rows value"))
for i in range(1,rows+1):
    for j in range(i-1):
        print(" ",end=" ")
    for j in range(i,rows+1):
        print("*",end=" ")
    print()
        




    


    


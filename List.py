##List:
##5.Largest number in List:
a=[10,15,20,25,35,40]
largest=a[0]
for i in a:
    if i>largest:
        largest=i
print("The largest number in the list is",largest)

##4.Length of the list without using len:
List=[10,25,40,48,29,16]
count=0
for i in List:
    count+=1
print("The length of the List is",count)

##8.Element exists in List:
List=[6,12,18,24,30,35]
element=36
if element in List:
    result=True
else:
    result=False
print(result)

##3.Multiply the numbers in the List:
List=[1,3,5,7,9]
multiply=1
for i in List:
    multiply*=i
print(multiply)

##6.Python Program to interchange first and last element:
a=[1,2,3,4,5]
if a:
    a[0],a[-1]=a[-1],a[0]
print(a)

##10.Python program to print all possible combinations from the three digits:
digits=[1,2,3]
for digit1 in digits:
    for digit2 in digits:
        for digit3 in digits:
            if digit1!=digit2 and digit1!=digit3 and digit2!=digit3:
                print(digit1,digit2,digit3)

##7.Swap numbers:
List=[1,2,3,4,5]
value1,value2=2,3
if value1 in List and value2 in List:
    pos1=List.index(value1)
    pos2=List.index(value2)
    List[pos1],List[pos2]=List[pos2],List[pos1]
print(List)

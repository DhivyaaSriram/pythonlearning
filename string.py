##without_end('Hello') → 'ell'
##without_end('java') → 'av'
##without_end('coding') → 'odin'

string=input("enter the string")
print(string[1:-1])

name=input("enter the name"
print("Hello "+name+"!")

##first_half('WooHoo') → 'Woo'
##first_half('HelloThere') → 'Hello'
##first_half('abcdef') → 'abc'

string=input("enter the string")
length=len(string)
half=length//2
print(string[:half])

##non_start('Hello', 'There') → 'ellohere'
##non_start('java', 'code') → 'avaode'
##non_start('shotl', 'java') → 'hotlava
           
##first_two('Hello') → 'He'
##first_two('abcdefg') → 'ab'
##first_two('ab') → 'ab'

string=input("enter the string")
print(string[:2])

##make_abba('Hi', 'Bye') → 'HiByeByeHi'
##make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
##make_abba('What', 'Up') → 'WhatUpUpWhat

a=input("enter the name1")
b=input("enter the name2")
print(a+b+b+a)

##left2('Hello') → 'lloHe'
##left2('java') → 'vaja'
##left2('Hi') → 'Hi'

string=input("enter the string")
print(string[2:]+string[0:2])

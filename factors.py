# Author: Sophia Philips
# GitHub Username: sophiacphilips
# Date: 10/12/2022
# This program finds all the factors of a positive integer and lists them smallest to largest.

num_1=int(input("Please enter a positive integer:", ))
print("The factors of", num_1, "are:")
for n in range(1,num_1+1):
    if(num_1%n==0):
        print(n)


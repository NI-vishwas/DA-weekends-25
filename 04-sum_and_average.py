# Author: Vishwas Singh
# Email: vishwasks.reach@gmail.com
# Script to calculate sum & average of n numbers 
# without storing, taking the input numbers until -999 is entered
# Version: 2.0
print("enter the numbers(-999 to exit):")
num = int(input())
total = 0
count = 1
while num != -999:
    total += num
    count += 1
    num = int(input())
    

print(f"The sum of numbers is: {total}")
print(f"The average of number: {total/count}")
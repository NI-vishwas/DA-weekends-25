# Author: Vishwas Singh
# Email: vishwasks.reach@gmail.com
# Script to calculate sum & average of n numbers 
# without storing, taking the input numbers until -999 is entered
# Version: 3.0
print("enter the numbers(-999 to exit):")
total = 0
count = 0
while True:
    num = int(input())
    if num == -999:
        break

    total += num
    count += 1

print(f"The sum of numbers is: {total}")
print(f"The average of number: {total/count}")
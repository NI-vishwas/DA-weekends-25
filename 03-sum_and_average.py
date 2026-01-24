# Author: Vishwas Singh
# Email: vishwasks.reach@gmail.com
# Script to calculate sum & average of 10 numbers 
# without storing
# Version: 1.0
print("Enter the numbers: ")
total = 0
for i in range(10):
    num = int(input())
    total += num

print(f"The sum of numbers is: {total}")
print(f"The average of number: {total/10}")
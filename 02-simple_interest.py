# Author: Vishwas Singh
# Email: vishwasks.reach@gmail.com
# Script to calculate simple interest
# Version: 1.0
# si = principal * time * rate_of_interest / 100
principal = int(input("Enter the principal amount: ")) # The principal value
time_in_months = int(input("Enter the time in months ( Ex: 3 years is 36 months): "))
rate_of_interest = float(input("Enter the rate of interest in decimal(Ex: 7% is 0.07): "))

simple_interest = (principal * time_in_months * rate_of_interest) / 100

# print("Simple interest is: ", simple_interest)
# print("Simple interest is: "+ str(simple_interest))
# Format Specifiers
# print("Simple interest is: %.0f"%(simple_interest))
# print("Rs. {0} will earn a Simple interest of: {1}".format(principal, simple_interest))
print(f"Rs. {principal} will earn a Simple interest of: {simple_interest:.2f}")
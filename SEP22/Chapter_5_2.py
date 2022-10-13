'''
Created on 05.09.2022

@author: thsetzer
'''

# get user’s first and last names
#first = input("Please enter your first name (all lowercase): ")
#last = input("Please enter your last name (all lowercase): ")

# concatenate first initial with 7 chars of last name
#uname = first[0] + last[:7]


# month2.py
#  A program to print the month name, given it's number.
#  This version uses a list as a lookup table.

def main():
    # months is a list used as a lookup table
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    n = eval(input("Enter a month number (1-12): "))
    print ("The month abbreviation is", months[n-1] + ".")
main()

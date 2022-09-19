"""Write a python script which takes a three digit number from the user and displays
only its middle digit."""
n=int(input("Enter three digit number :"))
n=n//10
a=n%10
print(a)

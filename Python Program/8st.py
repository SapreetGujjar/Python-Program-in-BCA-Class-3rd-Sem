# Compute sum of natural numbers from one to n number.

sum = 0
n = int(input("Enter any integer value: "))
if n > 0:
    for i in range(1,n+1):
       sum = sum + i
    print("Sum of the numbers from 1 to",n,":",sum)
elif n==0:
    print("Sum = 0")
else:
    print("Please enter positive value ")
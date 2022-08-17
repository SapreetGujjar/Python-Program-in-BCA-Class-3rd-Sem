# Write a program to determine whether a triangle is isosceles or not?

a = int(input("Length of First Side : "))
b = int(input("Length of Second Side : "))
c = int(input("Length of Third Side : "))
print("First side :",a,"cm")
print("Second side :",b,"cm")
print("Thrid side :",c,"cm")
if  a == b == c or a == b !=c or a==c !=b or b==c !=a:
    print("Triangle is issoceles")
else:
    print("Trinangle is not issoceles")
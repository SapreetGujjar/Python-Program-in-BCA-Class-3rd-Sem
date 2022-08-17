# Compute area of following shapes: circle, rectangle, triangle, square, trapezoid and parallelogram.
import math
PI= math.pi
print("Enter your Choice :")
print("1. cicle")
print("2. Rectangle")
print("3. Triangle")
print("4. Square")
print("5. Trapeoid")
print("6. Parllelogram")

n=int(input("Enter you hoice to Calculate area : "))
if n== 1:
    r=int(input("Enter radius: "))
    AI=PI*r*r
    print("Area of circle ="(AI,2))
elif n==2:
    s1=int(input("Enter Length of Rectangle: "))
    s2=int(input("Enter Breadth of Rectangle : "))
    A2 =s1*s2
    print("Area of the Rectangle :",round(A2,2))
elif n==3:
    a =int(input("Enter First side: "))    
    b =int(input("Enter second side: "))    
    c =int(input("Enter third side: "))  
    s=(a+b+c)/2
    temp=s*(s-a)*(s-b)*(s-c)
    A3 = math.sqrt(temp)
    print("Area of the Triangle: ",round(A3,20))
elif n==4:
    side =int(input("Enter side of square :"))
    A4=side*side
    print("Area of the Square :",round(A4,2))
elif n==5:
    P1 = int(input("Enter first parallel side :"))
    P2 = int(input("Enter second parallel side :"))
    D  = int(input("Enter Distance between || side : "))
    A5 = 0.5*(P1+P2)*D
    print("Area of the Trapezoid :",round(A5,2))
elif n==6:
    base = int(input("Enter base of parallelogram :"))
    height = int(input("Enter Height :"))
    A6 = base*height
    print("Area of the Parallelogram :",round(A6,2))
else:
    print("...Please Enter Correct Choice")
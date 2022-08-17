#Compute volume of following 3D shapes: cube, cylinder, cone and sphere. 

import math
PI = math.pi
print("INDEX")
print("1. CUBE")
print("2. CYCILNDER")
print("3. CONE")
print("4. SPHERE")
print("Enter your choice to calculate volume form the above")
n = int(input())
if n == 1:
    R1 = int(input("Enter Radius : "))
    V1 = math.pow(R1,3)
    print("Volume of CUBE",round(V1,3))
elif n == 2:
    R2 = int(input("Enter Radius :"))
    H2 = int(input("Enter Height :"))
    V2 = PI*R2*R2*H2
    print("Volume of CYLINDER :",round(V2,3))
elif n == 3:
    R3 = int(input("Enter Radius :"))
    H3 = int(input("Enter Height :"))
    V3 = (1/3)*PI*R3*H3
    print("Volume of CONE :",round(V3,3))
elif n == 4:
    R4 = int(input("Enter Radius :"))
    V4 = (4/3)*PI*math.pow(R4,3)
    print("Volume od CUBE :",round(V4,3))
else:
    print("Enter the correct choice")    
print("MUHAMMAD SAAD HASAN 18B-117-CS SECTION:-A")
print("ASSIGNMENT # 3")
print("PROBLEM 3.43")

def hit(x,y,r,Xp,Yp):
    import math
    point = math.sqrt((x-Xp)**2 + (y-Yp)**2)
    if point <= r :
        print(True)
    else:
        print(False)

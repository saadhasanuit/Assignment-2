print("MUHAMMAD SAAD HASAN 18B-117-CS SECTION:-A")
print("ASSIGNMENT # 3")
print("PROBLEM 3.39")
def collision(x1,y1,r1,x2,y2,r2):
    import math
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    r = (r1 + r2)

    # For collision
    if d<= r:
        print(True)
    #Not for collision
    else:
         print(False)

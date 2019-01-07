print("MUHAMMAD SAAD HASAN 18B-117-CS SECTION:-A")
print("ASSIGNMENT # 3")
print("PRACTICE PROBLEM 3.11")
## Function allEven() that takes a list of integers and returns True if all integers in the list are even, and False otherwise
def allEven(_list):
    for num in _list:
        if num%2 != 0:
            return(False)
        else:
            return(True)

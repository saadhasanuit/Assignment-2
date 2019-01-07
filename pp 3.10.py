print("MUHAMMAD SAAD HASAN 18B-117-CS SECTION:-A")
print("ASSIGNMENT # 3")
print("PRACTICE PROBLEM 3.10")
##function noVowel() that takes a string s as input and returns True if no character in s is a vowel, and False otherwise

def noVowel(x):
    for c in x:
        if c in 'aeiouAEIOU':
            return False
    return True

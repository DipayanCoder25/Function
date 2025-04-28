'''
def studentinfo():
    print("Dipayan")
studentinfo()

def Codingal(name,grade):
    print(name)
    print(grade)
Codingal("Dipayan",7)

def Sum(a,b,c,d):
    sum=a+b+c+d
    return sum
result=Sum(122,12,24,56)
print(result)            
def add(p,q):
    return p+q
def substraction(p,q):
    return p-q
def multiplication(p,q):
    return p*q
def divison(p,q):
    return p/q
print("a. Addition")
print("b. substraction")
print("c.multiplication")
print("d.divison")

choice=input("Enter a/b/c/d")

p=int(input("Enter number 1: "))
q=int(input("Enter number 2: "))

if choice=="a":
    print(p, "+", q, "=", add(p,q))
elif choice=="b":
    print(p, "-", q,"=", substraction(p,q))  
elif choice=="c":
    print(p, "*", q, "=", multiplication(p,q))
elif choice=="d":
    print(p, "/", q,"=", divison(p,q))
else:
    print("Invalid input")              

def prime(num):
    flag=0
    for i in range(2,num-1):
        if num%i==0:
            flag=1
    if flag>0:
        return False
    else:
        return True
num=int(input("Enter a number"))
print(prime(6))  
'''
def is_prime(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
        return True
print(is_prime(7))            
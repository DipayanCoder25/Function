'''for i in range(9):
    if i==3:
        continue
    print(i)
    
def two_sum(a,b):
    return a+b
a=two_sum(5,5)
print(a)    

for i in range(9):
    if i==3:
        break
    print(i)
    
a=input("enter a word ")

for i in  a:
    if i=='A':
        print("A is found")
        break
    else:
        print("A is not found")
        
for i in range(10):
    if i%20==0:
        print("Twist")
    elif i%15==0:
        pass
    elif i%5==0:
        print("Fizz")
    elif i%3==0:
        print("Buzz")
    else:
        print(i)
        
var=10
while var>=0:
    var-=1
    if var==5:
        continue
    else:
        print("Current value is ",var)
print("\nGood bye")                
                      
                      '''
def validate_age(age_list):
    valid_age=[]
    for age in age_list:
        if age is None:
            continue
        if age<0:
            print("Invalid age found")
            break
        if age>120:
            return "Error age too high"
            
        valid_age.append(age)
    return valid_age

ages=[25,44,67,None,2,51]
result=validate_age(ages)
print(result)
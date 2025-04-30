'''def tip(billl,tip_perchentage):
    total=billl*(1+0.01*tip_perchentage)
    total=round(total,2)
    print(f"You need to pay ${total}")
tip(150,20)

def display_menu():
    print("\n  ----MENU----")
    print("1.Burger -350 ")
    print("2.Pizza -900")
    print("3.Pasta -300")
    print(" Exit \n")
def price(choice):
    prices={1:350,2:900,3:300}    
    return prices.get(choice,0)

def take_order():
    subtotal=0
    while True:
        display_menu()
        choice=int(input("Enter an item (1-3): "))
        if choice==4:
            break
        if choice==(1,2,3):
            qty=int(input("Enter the quantity: "))
            subtotal+=price(choice)*qty
        else:
            print("Invalid error")
def tip_caculate(subtotal,tip_perchantage):
    return subtotal*(tip_perchantage/100)
def display_bill(subtotal,tip):
    total=subtotal+tip
    print("---Bill---")
    print(f"Subtotal :BDT{subtotal:0.2f}")                
    print(f"Subtotal :BDT{tip:0.2f}")    
    print("Total : BDT{total:.2f}")
def main():
    print("Welcome to store")
    subtotal=take_order()
    if subtotal>0:
        tip_perchantage=float(input("Write tip percentage "))
        tip=tip_caculate(subtotal,tip_caculate)
        display_bill(subtotal,tip)
    else:
        print("No Items ordered")        
        
main()        
def display_menu():
    print("\n ----- MENU------")
    print("1. Burger  --- 350 BDT")
    print("2. Pizza  --- 900 BDT")
    print("3. Pasta  --- 300 BDT")
    print("4. Exit \n  ")
def get_price(choice):
    prices={1:350,2:900,3:300}
    return prices.get(choice,0)

def take_order():
    subtotal=0
    while True:
        display_menu()
        choice=int(input("select an item(1-4): "))
        if choice==4:
            break
        if choice in [1,2,3]:
            qty=int(input("Enter Quantity:"))
            subtotal+= get_price(choice)*qty
        else:
            print("invalid choice")
        return subtotal
        
def calculate_tip(subtotal,tip_percent):
    return subtotal*(tip_percent/100)
    
def display_bill(subtotal,tip):
    total=subtotal+tip
    print("--- BILL----")
    print(f"subtotal: BDT {subtotal:.2f}")
    print(f"subtotal: BDT {tip:.2f}")
    print(f"Total: BDT {total:.2f}")
def main():
    print("welcome to the resturant!")
    subtotal=take_order()
    if subtotal>0:
        tip_percent=float(input("Write Tip Percentage"))
        
        tip=calculate_tip(subtotal,tip_percent)
        display_bill(subtotal,tip)
    else:
        print("No Item ordered")
main()

def cube(number):
    return number*number*number

def divisible_by_3(number): 
    if number %3==0:
        return cube(number)
    else:
        return False
print(divisible_by_3(7))
print(divisible_by_3(4))   
'''
def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
    
print(factorial(2))    
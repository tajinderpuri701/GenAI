def price(user_class):
    if user_class==1:
        return 1500
    elif user_class==2:
        return 1000
    elif user_class==3:
        return 500
def age_price(user_age,ticket):
    if user_age<=5:
        return 0
    elif user_age>=60:
        return ticket*0.8
    else:
        return ticket
def extra_meal(user_meal,ticket):
    if user_meal=="yes":
        return ticket+200
    else:
        return ticket
user_name=input("Enter your name")
user_age=int(input("Enter your age"))
user_class=int(input("Choose travel class:\n1. First Class\n2. Second Class\n3. Sleeper Class\nEnter choice (1/2/3): "))
user_meal=input("Do you want to add a meal? (yes/no):").lower()
ticket=price(user_class)
ticket=age_price(user_age,ticket)
ticket=extra_meal(user_meal,ticket)
print(f"-------Total Summary--------")
print(f"Passenger Name:{user_name}")
print(f"Age:{user_age}")
print(f"Class:{user_class}")
print(f"Meal included:{user_meal}")
print(f"Total cost is : Rs.{ticket}")

print(f"Enjoy your Journey!!!")

#@2
menu=[{'Whopper Burger':150},{'Crispy Veg':100},{'Chicken Wings':120,}]
code=[{'KING50':50},{'BK20':0},{'NOCOUPON':0},]
print("MENU")
price=0
for i in menu:
    for k,v in i.items():
        print(f"{k}   Rs.{v}")
def order_price(order):
    end_order=menu[order-1]
    return list(end_order.values())[0]


order=int(input("What do you want to order 1/2/3:"))
order_numbers=int(input("how many?"))
total=order_price(order)*order_numbers
coupon_coder=input("Do you have a coupn code?(y/n)").lower()
if coupon_coder=="y":
    coupon_code=input("enter code:")
    if coupon_code=="KING50":
        print("Applying coupon...")
        print(f"Original Price:{total}")
        print(f"Discount applied: 50%")
        total*=0.5
    elif coupon_code=="BK20":
        print("Applying coupon...")
        print(f"Original Price:{total}")
        print(f"Discount applied: 20 rs off")
        total-=20

    else:
        total=total
else:
    print(f'final price:{total}')
    print("Thanks for ordering at Burger King!")

a=print("\n--- Welcome to JJs Food Court ---")
menu={"classic burger":50,"cheeseburger":75,"chicken burger":100,"maharaja burger":160,"small fries":60,"medium fries":100,"large fries":150,
      "small wings bucket":150,"medium wings bucket":230,"large wings bucket":320,"small cola":80,"medium cola":140,"large cola":200,
      "venilla cone":30,"strawberry cone":40,"chocolate cone":40,"choco lava cake":100}

order=[]
for item,price in menu.items():
    print(f"{item}= Rs{price:.2f}")

while True:
    x=input("So, What would you like to have? (whenever you are done ordering, type 'done')")
    if x in menu:
        order.append(x)
        print(f"{x} has been added to your order!")
    elif (x=="done"):
        break
    else:
        print("Sorry we don't have that")
    
if order:
    print("Your Complete Order")
    total=0
    for item in order:
        print(f"{item}= Rs{menu[item]:.2f}")
        total+=menu[item]
    print(f" Your Total Bill: Rs{total:.2f}")
else:
    print("There is nothing you ordered yet")






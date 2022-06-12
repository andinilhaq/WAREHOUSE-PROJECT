product={}
description={}
stock={}
money=0
warehouse={}

try:
    details = open("Warehouse.txt","r")

    no_items = int((details.readline()).rstrip("\n"))

    for i in range(0,no_items):
        line = (details.readline()).rstrip("\n")
        x1,x2 = line.split("#")
        x1 = int(x1)
        x2 = float(x2)
        product.update({x1:x2})
    
    for i in range(0,no_items):
        line  = (details.readline()).rstrip("\n")
        x1,x2 = line.split("#")
        x1=int(x1)
        description.update({x1: x2})

    for i in range(0,no_items):
        line = (details.readline()).rstrip("\n")
        x1,x2 = line.split("#")
        x1 = int(x1)
        x2 = int(x2)
        stock.update({x1: x2})

except:
    print("Stock kosong")

finally:
    details.close()

cart=[]

c="y"
print("="*70)
print("{:^70}".format("Warehouse APP"))
print("="*70)
print('''
Command list:

A-Add item
R-Remove item
E-Edit data
D-Add stock
L-Show product list
B-Buy
C-Checkout
S-Show purchased item
Q-Quit
Clr-Clear cart
Stat-Warehouse status
help-Show command list  
''')
print("="*70)
print()

total_cost=0
flag=0

while(c!="q" or c!= "Q"):
    c = input("Enter a command: ")

    if (c=="q" or c=="Q"):
        break
    
    elif(c=="A" or c=="a"):
        p_no = int(input("Enter item number: "))
        p_desc = input("Enter item description: ")
        p_pr = float(input("Enter item price: ")) 
        p_stock = int(input("Enter item stock: "))
        
        m=0
        for i in range(0,len(product)):
            if(p_no in product):
                p_no+=1
                m=1
        if(m==1):
            print()
            print("Item number already exists, changing value to ",p_no)

        warehouse.update({p_no: {'name':p_desc,
                                'stock':p_stock,
                                'price':p_pr    
        }})
        product.update({p_no: p_pr})
        description.update({p_no: p_desc})
        if(p_stock > -1):
            stock.update({p_no: p_stock})
        else:
            p_stock = 0
            stock.update({p_no: p_stock})
            print("The stock of an item cannot be negative, the stock has been set to 0.")
        print()
        print("Item number: ",p_no," Description: ",description.get(p_no)," Price: ",product.get(p_no)," Stock: ",stock.get(p_no))
        print("Item was added successfully!")
        print()

    elif(c=="R" or c=="r"):
            print()
            p_no = int(input("Enter item number: "))
            if(p_no in product):
                are_you_sure = input("Are you sure you want to remove that item(y/n)? ")
                if(are_you_sure=="y" or are_you_sure=="Y"):
                    product.pop(p_no)
                    description.pop(p_no)
                    stock.pop(p_no)
                    warehouse.pop(p_no)
                    print("Item successfully removed!")
                print()
            else:
                print("Sorry, we don't have such an item!")
                print()

    elif(c=="E" or c=="e"):
        print()
        p_no = int(input("Enter item number: "))
        if(p_no in warehouse):
            p_desc = input("Enter item description: ")
            p_pr = float(input("Enter item price: "))
            p_stock = int(input("Enter item stock: "))
                
            product.update({p_no: p_pr})
            description.update({p_no: p_desc})
            stock.update({p_no: p_stock})
            warehouse.update({p_no: {'name': p_desc,
                                     'stock': p_stock,
                                     'price': p_pr}})
        else:
            print("Item doesn't exist")
        print()
    
    elif(c=="D" or c=="d"):
        print()
        p_no = int(input("Enter item number: "))
        if(p_no in warehouse):
            products=warehouse[p_no]
            print("Item to be added: ", products['name'] )
            qty = int(input("Add item stock: "))
            products['stock']=products['stock']+qty
        else:
            print("Item doesn't exist")
        print()
            
    elif(c=="L" or c=="l"):
        print()
        print('List produk:')
        for i in range(0,len(warehouse)):
            products = warehouse[i+1]
            print('Product\t:', products['name'])
            print('Stock\t:', products['stock'])
            print('Price\t:', products['price'])
            print()
        print()

    elif(c=="B" or c=="b"):
        print()
        p_no = int(input("Enter Item number: "))
        buy_amount = int(input("Enter purchase amount: "))
        if(p_no in warehouse):
            products = warehouse[p_no]
            current_stock = products['stock']
            if(flag==1):
                flag=0
            if(buy_amount<=current_stock):
                current_stock = products['stock']
                stock_updt = current_stock-buy_amount
                item_price = buy_amount*products['price']
                total_cost = total_cost+item_price
                print(products['name'],"added to cart: ","Rp",item_price)
                cart.append(p_no)
                products['stock'] = stock_updt
            else:
                print("item out of stock!")
        else:
                print("Sorry! We don't have such an item!")
        print()

    elif(c=="C" or c=="c"):
        print()
        print("You bought the following items: ",cart)
        print("Total: Rp ",round(total_cost,2))
        money=money+total_cost
        total_cost=0
        flag=1
        cart.clear()
        print()
        print("You can still purchase items after check out, your cart has been reset. To quit press q")
        print()
    
    elif(c=="help"):
        print()
        print('''
Command list:

A-Add item
R-Remove item
E-Edit data
D-Add stock
L-Show product list
B-Buy
C-Checkout
S-Show purchased item
Q-Quit
Clr-Clear cart
Stat-Warehouse status
help-Show command list  
        ''')
        print()

    elif(c=="S" or c=="s"):
        print()
        print(cart)
        print()

    elif(c=="Stat" or c=="stat"):
        CurrentMoney=money
        print()
        print('Current Store Money: Rp ', CurrentMoney)
        print('Current Store info:')
        for i in range(0,len(warehouse)):
            products=warehouse[i+1]
            print('- Product: ', products['name'], '\t, Price: Rp ', products['price'], '\t, Stock:', products['stock'])
        print()
        
    elif(c=="Clr" or c=="clr"):
        print()
        confirm = input("Are you sure you want to clear item from the cart(y/n)? ")
        if(confirm=="y"):
            p_no = int(input("Enter item number to remove from cart: "))
            if(p_no in cart):
                products = warehouse[p_no]
                current_stock = products['stock']
                stock_updt = current_stock+buy_amount
                item_price = buy_amount*products['price']
                total_cost = total_cost-item_price
                j=0
                for i in range(0,len(cart)):
                    if(i==p_no):
                        j=i

                products['stock'] = stock_updt
                cart.pop(j)
                print(products['name'],"removed from cart: ")
                print()
            else:
                print()
                print("Item is not in your cart!")
                print()
    else:
        print()
        print("Input correct command!")
        print()

if(total_cost>0 and flag==0):
    print()
    print("You bought: ",cart)
    print("Total: ","Rp",round(total_cost,2))

print("\nThank you for using Warehouse APP")

try:
    details = open("Warehouse.txt","w")
    no_items=len(product)
    details.write("Warehouse Data: \n")
    for i in range(0,no_items):
        details.write(str(i+1)+". Product: "+description[i+1]+"\t, Price: Rp "+str(product[i+1])+"\t, Stock: "+str(stock[i+1])+"\n")
except:
   print("Stock saved")
  
finally:
    details.close()

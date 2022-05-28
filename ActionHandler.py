product={}
description={}
stock={}
money=0
warehouse={}

def ADDITEM():
    p_no= int(input('Enter item number: '))
    p_name= input('Enter item description: ')
    p_stock= int(input('Enter item stock: '))
    p_price= float(input('Enter item price: '))
    n=0
    for i in range(len(warehouse)):
        if (p_no in warehouse):
            p_no+=1
            n=1
    if n==1:
        print("Item number already exist, changing value to ",p_no)
    
    warehouse.update({p_no:{'name':p_name,
                            'stock':p_stock,
                            'price':p_price}})

    print("Item was added successfully!\n")
    return warehouse

def ADDSTOCK():
    p_no= int(input('Enter item number: '))
    if (p_no in warehouse):
        products=warehouse[p_no]
        print("Item to be added: ", products['name'] )
        print("Current item stock: ", products['stock'])
        qty = int(input("Add item stock: "))
        products['stock']=products['stock']+qty
    else:
        print("Item doesn't exist\n")
    return warehouse

total_cost=0
flag=0
cart={}

def BUYPRODUCT():
    p_no= int(input("Enter item number: "))
    if(p_no in warehouse):
        print("Item")
        buy_amount= int(input("Enter"))
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
            cart.update({p_no:{'name':products['name'],
                               'amount':buy_amount,
                               'total':item_price}})
            products['stock'] = stock_updt
        else:
            print("item out of stock!\n")
    else:
        print("Sorry! We don't have such an item!\n")

    return warehouse, cart
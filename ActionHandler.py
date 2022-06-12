import pandas as pd

product={}
description={}
stock={}
money=0
warehouse={}
total_cost=0
flag=0
cart={}

data = pd.read_csv('store_data.csv')
df=pd.DataFrame(data)

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
    
    warehouse.update({'no':p_no,
                      'name':p_name,
                      'stock':p_stock,
                      'price':p_price})

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

def BUYPRODUCT():
    p_no= int(input("Enter item number: "))
    if(p_no in warehouse):
        print("Item: ", warehouse[p_no]['name'])
        buy_amount= int(input("Enter purchase amount: "))
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

def CHECKOUT():
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

def STATUS():
    CurrentMoney=money
    print()
    print('Current Store Money: Rp ', CurrentMoney)
    print('Current Store info:')
    for i in range(0,len(warehouse)):
        products=warehouse[i+1]
        print('- Product: ', products['name'], '\t, Price: Rp ', products['price'], '\t, Stock:', products['stock'])
    print()

def ActionLog():
    details = pd.read_csv('Warehouse.csv', sep=';', header = None)
    df=pd.DataFrame(details)
    warehouse.to_csv('Warehouse.csv','a',index = False, header = None)

database = pd.DataFrame.from_dict(warehouse, orient='index')
database.to_csv('store_data.csv',mode ='a',index = False, header = None)
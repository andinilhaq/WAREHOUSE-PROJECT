import pandas as pd

def ADDITEM():
        details= pd.read_csv('store_data.csv')
        df= pd.DataFrame(details)

        global num
        global name
        global price 
        global stock 
        num = int(input('Enter item number: '))
        name = (input('Enter item description: '))
        check = (len(df[(df.Number == num)]) < 1 and len(df[(df.Name == name) ]) < 1)

        if check and num != "":
            price = float(input('Enter item price: '))
            stock = int(input('Enter item stock: '))
            warehouse = {'Number' : [num], 
                         'Name' : [name],
                         'Stock' : [stock],
                         'Price': [price]}
            updt=pd.DataFrame(warehouse)
            updt.to_csv('store_data.csv', mode='a', index = False, header=False)
            print('Item successfully added!\n')
            note='success'
            if note == 'success':
                lognote = pd.read_csv('ActionLog.csv')
                df2= pd.DataFrame(lognote)
                Log = "ADD_ITEM"
                product = name
                stock_change= stock
                act_log={'ActionLog': [Log],
                         'Name': [product],
                         'StockChange': [stock_change],
                         'CurrenStock': [stock]}
                ActLog=pd.DataFrame(act_log)
                ActLog.to_csv('ActionLog.csv', mode='a', index = False, header=False)
        else:
            print('Product already exist\n')
    
def ADDSTOCK():
    details= pd.read_csv('store_data.csv')
    df= pd.DataFrame(details)

    global num
    num = int(input('Enter item number: '))

    check= (len(df[(df.Number == num)])>0)
    if check and num !="":
        print()
        indeks = df[df['Number']==num].index.item()
        stock = df['Stock'][indeks] 
        print('Item to be added: ', df['Name'][indeks])
        amount= int(input('Enter stock amount: '))
        stock_updt=stock + amount
        df['Stock'][indeks]=stock_updt
        details.to_csv('store_data.csv', mode='r+', index = False)
        note= 'success'
        print('Stock updated!')
        if note == 'success':
            lognote = pd.read_csv('ActionLog.csv')
            df2= pd.DataFrame(lognote)
            Log = "ADD_STOCK"
            product = df['Name'][indeks]
            stock_change= amount
            act_log={'ActionLog': [Log],
                     'Name': [product],
                     'StockChange': [stock_change],
                     'CurrenStock': [stock_updt]}
            ActLog=pd.DataFrame(act_log)
            ActLog.to_csv('ActionLog.csv', mode='a', index = False, header=False)
            return stock_updt
    else:
        print("Item doesn't exist\n")

def TAKEITEM():
    details= pd.read_csv('store_data.csv')
    df= pd.DataFrame(details)

    global num
    global stock
    num = int(input('Enter item number: '))

    check= (len(df[(df.Number == num)])>0)
    if check and num !="":
        print()
        indeks = df[df['Number']==num].index.item()
        stock = df['Stock'][indeks]
        print('Item to be taken: ', df['Name'][indeks])
        amount= int(input('Enter take amount: '))
        stock_updt=stock - amount
        df['Stock'][indeks]=stock_updt
        details.to_csv('store_data.csv', mode='r+', index = False)
        print('Stock updated!')
        note='success'
        if note == 'success':
            lognote = pd.read_csv('ActionLog.csv')
            df2= pd.DataFrame(lognote)
            Log = "TAKE_ITEM"
            product = df['Name'][indeks]
            stock_change= amount
            act_log={'ActionLog': [Log],
                     'Name': [product],
                     'StockChange': [stock_change],
                     'CurrenStock': [stock_updt]}
            ActLog=pd.DataFrame(act_log)
            ActLog.to_csv('ActionLog.csv', mode='a', index = False, header=False)
            return stock_updt
    else:
        print("Item doesn't exist\n")

comm='y'
while (comm!= 'q' or comm!='Q'):
    print('='*60)
    print('{:^60}'.format("WAREHOUSE APP"))
    print('='*60)
    print('''\nCommand list:
    1. [N] = Add item
    2. [A] = Add stock
    3. [T] = Take item
    4. [H] = Help (Show command list)
    5. [S] = Warehouse Status
    6. [Q] = Quit
    ''')
    comm= input("Please enter a command: ")
    if (comm == 'N' or comm == 'n'):
        ADDITEM()
    elif (comm == 'A' or comm == 'a'):
        ADDSTOCK()
    elif (comm == 'T' or comm == 't'):
        TAKEITEM()
    elif (comm == 'H' or comm == 'h'):
        print('''\nCommand list:
    1. [N] = Add item
    2. [A] = Add stock
    3. [T] = Take item
    4. [H] = Help (Show command list)
    5. [S] = Warehouse Status
    6. [Q] = Quit
    ''')
    elif (comm == 'S' or comm == 's'):
        details= pd.read_csv('store_data.csv')
        df= pd.DataFrame(details)
        print('='*60)
        print('{:^60}'.format('WAREHOUSE STATUS'))
        print('='*60)
        print()
        print('Current Store info:')
        print(df)
        print()
    elif (comm == 'Q' or comm == 'q'):
        print()
        print('Thanks for using WAREHOUSE APP!')
        break
    else:
        print("Unknown input, please enter correct command! [H]: help\n")
import ActionHandler as AH

q= 'y'
print('''
Command List:
A = Add item
S = Add stock
P = Purchase item
T = Warehouse status
Q = Quit
''')
while (q!='q' or q!='Q'):
    q= input('What would you like to do? ')
    if (q=='Q' or q=='q'):
        break
    elif (q=='A' or q=='a'):
        AH.ADDITEM()
    elif (q=='S' or q=='s'):
        AH.ADDSTOCK()
    elif (q=='P' or q=='p'):
        AH.BUYPRODUCT()
    elif (q=='T' or q=='t'):
        AH.STATUS()
    elif (q=='Help'):
        print('''
Command List:
A = Add item
S = Add stock
P = Purchase item
T = Warehouse status
Q = Quit
''')
    else:
        print('Unknown command, please input another command\n')
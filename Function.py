import pandas as pd
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
 
class ADDITEM(MDScreen):
    def __init__(self, **kw):
        self.win1 = Builder.load_file('ADDITEM.kv')
        super().__init__(**kw)
    
    def ADDSTOCK(self):
            details= pd.read_csv('store_data.csv')
            df= pd.DataFrame(details)

            global num
            global name
            global price 
            global stock 
            num = self.win1.get_screen('ADDITEM').ids.num.text
            name = self.win1.get_screen('ADDITEM').ids.name.text
            price = self.win1.get_screen('ADDITEM').ids.price.text
            stock = self.win1.get_screen('ADDITEM').ids.stock.text
            matching_creds = (len(df[(df.Number == num)]) < 1 and len(df[(df.Name == name) ]) < 1)

            if matching_creds and num != "":
                
                warehouse = {'Number' : [num],
                            'Name' : [name],
                            'Stock' : [stock],
                            'Price': [price]}
                updt=pd.DataFrame(warehouse)
                updt.to_csv('store_data.csv', mode='a', index = False, header =False)
            else:
                print('Product already exist')
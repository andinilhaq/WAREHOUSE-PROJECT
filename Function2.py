import pandas as pd
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class ADDSTOCK(MDScreen):
    def __init__(self, **kw):
        self.win2 = Builder.load_file('ADDSTOCK.kv')
        super().__init__(**kw)
    def ADDSTOCK(self):
        details= pd.read_csv('store_data.csv')
        df= pd.DataFrame(details)

        global num
        global stock
        num = self.win2.get_screen('ADDSTOCK').ids.num.text

        check= (len(df[(df.Number == num)])>0)
        if check and num !="":
            print()
            print('Item to be added: ', df.Name)
            add_stock= self.win2.get_screen('ADDSTOCK').ids.amount.text
            stock_updt=stock + add_stock
            warehouse = {'Stock': stock_updt}
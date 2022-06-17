import pandas as pd
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from screens import *

class WindowManager(ScreenManager):
    pass
class MainApp(MDApp):
    WINDOW = {
        'Welcome': 'screens.welcome',
        'ADDITEM': 'Function',
        'ADDSTOCK': 'Function2',
        'TAKEITEM': 'Function3'

    }
    AUTORELOADER_PATHS = [
        ('.',{'recursive':True})
    ]
    KV_FILES = {
        'welcome.kv'
        'ADDITEM.kv'
        'ADDSTOCK.kv'
        'TAKEITEM.kv'
    }
    def build(self):
        self.wm = WindowManager()
        screens = [
            Welcome(name='welcome'),
            ADDITEM(name='Function'),
            ADDSTOCK(name= 'Function2'),
            TAKEITEM(name= 'Function3')
        ]
        for screen in screens:
            self.wm.add_widget(screen)
        return self.wm

if __name__ == '__main__':
    MainApp().run()

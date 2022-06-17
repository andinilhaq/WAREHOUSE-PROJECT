import pandas as pd
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class TAKEITEM(MDScreen):
    def __init__(self, **kw):
        Builder.load_file('TAKEITEM.kv')
        super().__init__(**kw)
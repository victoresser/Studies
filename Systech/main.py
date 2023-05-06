# Importando App, Builder (GUI)
"""
1. Criar o Aplicativo
2. Criar a função Build
"""

from kivy.app import App
from kivy.lang import Builder

GUI = Builder.load_file("file.kv")

class MeuApp(App):
    def build(self):
        return GUI

MeuApp().run()
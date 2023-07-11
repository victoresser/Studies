# Importando Libs Externas
import tkinter as tk

# Importanto Libs internas
from models.views import LoginWindow

# Cria Janela principal
root = tk.Tk()
root.withdraw()  # Esconde Janela Principal

# Janela de Login
login = LoginWindow(master=root)
login.wait_window()

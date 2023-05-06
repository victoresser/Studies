import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle
from tkinter import messagebox

class LoginWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Systech - Login")
        self.update_idletasks()
        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) // 2
        y = (self.winfo_screenheight() - self.winfo_reqheight()) // 2
        self.geometry(f"+{x}+{y}")
        self.create_widgets()
        style = ThemedStyle(self)
        style.set_theme("adapta")

    def create_widgets(self):

        # Criando campos para login
        self.loginLabel = ttk.Label(self, text="Login:")
        self.loginEntry = ttk.Entry(self)
        self.passwdLabel = ttk.Label(self, text="Senha:")
        self.passwdEntry = ttk.Entry(self, show="*")
        self.loginLabel.pack(side="left")
        self.loginEntry.pack(side="left")
        self.passwdLabel.pack(side="left")
        self.passwdEntry.pack(side="left")

        # Criando Botão para login
        self.entrarButton = ttk.Button(self, text="Entrar")
        self.entrarButton.configure("<Return>", lambda event:self.login)
        self.entrarButton.pack(side="left")

    def login(self):
        pass
import tkinter as tk
from ttkthemes import ThemedStyle as ts

class application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    # Criando campos para serem preenchidos
    def create_widgets(self):
        style = ts(self.master)
        style.set_theme("radiance")


        # Campo "Nome"
        self.name_label = tk.Label(self, font=("Arial", 11))
        self.name_label["text"] = "Nome:"
        self.name_label.pack(side="left")

        self.name_entry = tk.Entry(self, font=("Arial", 8))
        self.name_entry.pack(side="left")

        # Campo "Sobrenome"
        self.lastname_label = tk.Label(self, font=("Arial", 11))
        self.lastname_label["text"] = "Sobrenome:"
        self.lastname_label.pack(side="left")

        self.lastname_entry = tk.Entry(self, font=("Arial", 8))
        self.lastname_entry.pack(side="left")
        
        # Campo "E-mail"
        self.email_label = tk.Label(self, font=("Arial", 11))
        self.email_label["text"] = "E-mail:"
        self.email_label.pack(side="left")

        self.email_entry = tk.Entry(self, font=("Arial", 8))
        self.email_entry.pack(side="left")

        # Botão "Enviar"
        self.submit_button = tk.Button(self, font=("Arial", 14))
        self.submit_button["text"] = "Enviar"
        self.submit_button["command"] = self.submit
        self.submit_button.pack(side="bottom")
    
    # Funções do botão "Enviar"
    def submit(self):
        
        """Funções do botão "Enviar". Quando o usuário clicar no botão
        será enviado para o servidor e também será aberta uma nova janela
        que retornara uma viagem para o usuário informando que as informações foram
        enviadas com sucesso."""

        name = self.name_entry.get()
        lastname = self.lastname_entry.get()
        email = self.email_entry.get()

        print("Nome:", name)
        print("Sobrenome:", lastname)
        print("E-mail:", email)

        # Cria uma nova janela
        success_window = tk.Toplevel(self.master)

        # Define a mensagem
        message = tk.Label(success_window, text="As informações foram enviadas com sucesso!")
        message.pack()

root = tk.Tk()
app = application(master=root)
app.mainloop()
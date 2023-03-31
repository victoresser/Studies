import tkinter as tk
from ttkthemes import ThemedStyle
import mysql.connector as conn
from flask import Flask, request

# Define a conexão com o banco de dados MySQL
db = conn.connect(
    host="localhost",
    user="root",
    password="",
    database="teste"
)
# Verificando se foi possível realizar a conexão com o banco de dados
if db.is_connected():
    print("Conexão com o banco de dados realizada com sucesso!")
else:
    print("Houve algum erro com a conexão com o banco de dados\nVerifique as credênciais de acesso ao banco de dados.")

sql = "INSERT INTO cadastros (nome , sobrenome, email) VALUES (%s, %s, %s)"

flask = Flask(__name__)

class application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        
    # Criando campos para serem preenchidos
    def create_widgets(self):
        """ Campos de preenchimento do formulário """
        style = ThemedStyle(self.master)
        style.set_theme("radiance")


        # Campo "Nome"
        self.name_label = tk.Label(self, font=("Arial", 11))
        self.name_label["text"] = "Nome:"
        self.name_label.pack(side="top")

        self.name_entry = tk.Entry(self, font=("Arial", 8))
        self.name_entry.pack(side="top")

        # Campo "Sobrenome"
        self.lastname_label = tk.Label(self, font=("Arial", 11))
        self.lastname_label["text"] = "Sobrenome:"
        self.lastname_label.pack(side="top")

        self.lastname_entry = tk.Entry(self, font=("Arial", 8))
        self.lastname_entry.pack(side="top")
        
        # Campo "E-mail"
        self.email_label = tk.Label(self, font=("Arial", 11))
        self.email_label["text"] = "E-mail:"
        self.email_label.pack(side="top")

        self.email_entry = tk.Entry(self, font=("Arial", 8))
        self.email_entry.pack(side="top")

        # Botão "Enviar"
        self.submit_button = tk.Button(self, font=("Arial", 14))
        self.submit_button["text"] = "Enviar"
        self.submit_button["command"] = self.submit
        self.submit_button.pack(side="right")
    
    # Funções do botão "Enviar"
    def submit(self):
        
        """Funções do botão "Enviar". Quando o usuário clicar no botão
        será enviado para o servidor e também será aberta uma nova janela
        que retornara uma viagem para o usuário informando que as informações 
        foram enviadas com sucesso."""

        name = self.name_entry.get()
        lastname = self.lastname_entry.get()
        email = self.email_entry.get()

        print("Nome:", name)
        print("Sobrenome:", lastname)
        print("E-mail:", email)

        cursor = db.cursor()
        cursor.execute(sql,(name, lastname, email))
        db.commit()
        # if db.commit() is True:
        #     dbWindow = tk.Toplevel(self.master)
        #     dbMsg = tk.Label(dbWindow, text="Dados inseridos com sucesso!")
        #     dbMsg.pack()
        # else:
        #     dbWindowError = tk.Toplevel(self.master)
        #     dbError = tk.Label(dbWindowError, text="Houve algum problema com a inserção das informações no banco de dados!")
        #     dbError.pack()
        #     self.name_entry.delete(0, tk.END)
        #     self.lastname_entry.delete(0, tk.END)
        #     self.email_entry.delete(0, tk.END)


        # Cria uma nova janela
        success_window = tk.Toplevel(self.master)

        # Define a mensagem
        message = tk.Label(success_window, text="As informações foram enviadas com sucesso!", font=("Arial", 14))
        message.pack()

        # Limpa os campos de entrada
        self.name_entry.delete(0, tk.END)
        self.lastname_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)


root = tk.Tk()
app = application(master=root)
app.mainloop()
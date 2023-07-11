import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle
from functions import conectaDb

# Realiza conexão com banco de dados conforme parâmetro informado.
db = conectaDb("teste")

sql = "INSERT INTO cadastros (nome , sobrenome, email) VALUES (%s, %s, %s)"


class ServiceSelection(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.geometry("600x460")
        self.style = ThemedStyle(self.master)
        self.style.set_theme("radiance")
        self.master.title("Projeto Financeiro 4.5")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        services = ["Metas", "Serviço 2", "Serviço 3"]

        self.service_label = ttk.Label(self, text="Selecione um serviço:")
        self.service_label.pack(side="left")

        self.create_service_buttons(services)

    def create_service_buttons(self, services):
        for service in services:
            button = tk.Button(
                self, text=service, command=lambda s=service: self.open_form(s)
            )
            button.pack(side="left")

    def open_form(self, service):
        if service == "Metas":
            root = tk.Tk()
            app = Application(master=root, service=service)
            app.mainloop()


class Application(tk.Frame):
    def __init__(self, master=None, service=None):
        super().__init__(master)
        self.master.geometry("800x460")
        self.master = master
        self.master.title(f"Projeto Financeiro 4.5 - {service}")
        self.pack()
        self.style = ThemedStyle(self.master)
        self.style.set_theme("radiance")
        self.create_widgets()

    # Criando campos para serem preenchidos
    def create_widgets(self):
        """Campos de preenchimento do formulário"""

        # Campo "Nome"
        self.name_label = ttk.Label(self, font=("Arial", 11))
        self.name_label["text"] = "Nome:"
        self.name_label.pack(side="left")

        self.name_entry = ttk.Entry(self, font=("Arial", 8))
        self.name_entry.pack(side="left")

        # Adiciona um espaço entre os campos
        self.space_label = tk.Label(self, font=("Arial", 8))
        self.space_label["text"] = ""
        self.space_label.pack(side="left")

        # Campo "Sobrenome"
        self.lastname_label = tk.Label(self, font=("Arial", 11))
        self.lastname_label["text"] = "Sobrenome:"
        self.lastname_label.pack(side="left")

        self.lastname_entry = tk.Entry(self, font=("Arial", 8))
        self.lastname_entry.pack(side="left")

        # Adiciona um espaço entre os campos
        self.space_label = tk.Label(self, font=("Arial", 8))
        self.space_label["text"] = ""
        self.space_label.pack(side="left")

        # Campo "E-mail"
        self.email_label = tk.Label(self, font=("Arial", 11))
        self.email_label["text"] = "E-mail:"
        self.email_label.pack(side="left")

        self.email_entry = tk.Entry(self, font=("Arial", 8))
        self.email_entry.pack(side="left")

        # Adiciona um espaço entre os campos
        self.space_label = tk.Label(self, font=("Arial", 8))
        self.space_label["text"] = ""
        self.space_label.pack(side="left")

        # Botão "Enviar"
        self.submit_button = ttk.Button(self, text="Enviar")
        self.submit_button.configure(style="My.TButton")
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
        cursor.execute(sql, (name, lastname, email))
        db.commit()

        # Cria uma nova janela
        success_window = tk.Toplevel(self.master)

        # Define a mensagem
        message = tk.Label(
            success_window,
            text="As informações foram enviadas com sucesso!",
            font=("Arial", 14),
        )
        message.pack()

        # Limpa os campos de entrada
        self.name_entry.delete(0, tk.END)
        self.lastname_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)


root = tk.Tk()
app = ServiceSelection(master=root)
app.mainloop()

import json
import mysql.connector as conn


def conectaDb(db: str):
    """Para definir qual banco de dados o aplicativo deve utilizar,
    é necessário informar o nome do banco presente no arquivo config.json
    ao chamar a função 'conectaDb'."""

    # Carrega as confgurações do banco de dados a partir do arquivo config.json
    with open("config.json") as f:
        config = json.load(f)

        # Verifica se o nome do banco de dados está no arquivo JSON
        if db not in config:
            raise ValueError(f"o Banco de dados {db} não está configurado.")

        # Obtem o nome do banco de dados a partir do nome informado para à função e faz a conexão
        data = config[db]
        conexao = conn.connect(
            host=data["host"],
            user=data["user"],
            password=data["password"],
            database=data["db"],
        )
        if conexao.is_connected():
            print(f"A conexão com {db} foi realizada com sucesso!")
        else:
            print(
                f"Por favor, verifique se o nome do banco de dados ({db}) está corretamente escrito.\nCaso esteja escrito corretamente, verifique banco de dados."
            )

        return conexao

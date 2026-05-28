from datetime import date, datetime
import json


class Livro:
    def __init__(self, nome, author, data_lancamento: date):
        self.nome = nome
        self.author = author
        self.data_lancamento = data_lancamento

    def criar_livro(self, nome, author, data_lancamento: datetime):
        print(
            f"Criando livro com nome {nome}, author {author}, data de lançamento {data_lancamento}"
        )

        # Dados do livro organizados em um dicionário
        livro = {
            "titulo": self.nome,
            "author": self.author,
            "data_lancamento": self.data_lancamento,
        }

        with open("livro.json", "a", encoding="utf-8") as arquivo:
            json.dump(livro, arquivo, ensure_ascii=False, indent=4)

        print("Livro salvo com sucesso!")

    def pegar_autores(self):
        with open("livro.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        autores = [item["autor"] for item in dados["autores"]]
        print(autores)

    def imprimir_livros(self):
        with open("livro.json", "r") as f:
            dados = json.load(f)
        print(json.dumps(dados, indent=4, ensure_ascii=False))

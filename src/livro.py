from datetime import date, datetime


class Livro:
    def __init__(self, nome, author, data_lancamento: date):
        self.nome = nome
        self.author = author
        self.data_lancamento = data_lancamento

    def criar_livro(self, nome, author, data_lancamento: datetime):
        print(
            f"Criando livro com nome {nome}, author {author}, data de lançamento {data_lancamento}"
        )

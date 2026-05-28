import json

class emprestimo():

    def __init__(self, usuario, livro, data_emprestimo, codigo):
        self.usuario = usuario
        self.livro = livro
        self.data_emprestimo = data_emprestimo

    def fazer_emprestimo(self):
        print(f"Criando empréstimo do livro: {self.livro.nome} para o usuário: {usuario}.")

        emprestimo = {
            "usuario": self.usuario
            "livro": self.livro.nome
            "data do empréstimo": self.data_emprestimo
            "código do empréstimo"self.codigo
        }
        try:
            with open("emprestimo.json", "w", encoding="utf-8") as arquivo:
                json.dump(emprestimo, arquivo, ensure_ascii=False, indent=4)
            print("Empréstimo criado com sucesso.")
        except:
            print("Falha no cadastro do empréstimo.")
    
    def read_emprestimo_full(self):
        try:
            with open("emprestimo.json", "r") as arquivo:
                data = json.load(file)
                print(f"Empréstimos: {data}")
        except:
            print(f"Erro ao carregar lista de empréstimos.")
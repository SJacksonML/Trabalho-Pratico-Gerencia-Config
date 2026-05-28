class Usuario:
    def __init__(self, nome: str):
        self.nome = nome

    def cadastrar_usuario(self, nome):
        print(f"Usuário cadastrado com sucesso: {nome}")
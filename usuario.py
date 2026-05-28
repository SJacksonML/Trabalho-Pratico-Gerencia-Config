import json

class Usuario:
    def __init__(self, nome: str, email: str, senha:int):
        self.nome = nome
        self.email = email
        self.senha = senha

    def cadastrar_usuario(self):
        print(f"Usuário cadastrado com sucesso: {self.nome}")

        usuario = {
            "Usuario": self.nome,
            "Email": self.email,
            "Senha": self.senha
        }
        try:
            with open("salvar_usuario.json", "w", encoding="utf") as arquivo:
                json.dump(usuario, arquivo, ensure_ascii=False, indent=4,)
        except:
            ("Erro ao cadastrar usuário!")
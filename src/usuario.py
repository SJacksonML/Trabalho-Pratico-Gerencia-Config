import json


class Usuario:
    def __init__(self, nome: str, email: str):
        self.nome = nome
        self.email = email

    def cadastrar_usuario(self):
        usuario = {
            "Usuario": self.nome,
            "Email": self.email
        }

        try:
            with open("salvar_usuario.json", "w", encoding="utf-8") as arquivo:
                json.dump(usuario, arquivo, ensure_ascii=False, indent=4)

            print(f"Usuário cadastrado com sucesso: {self.nome}")

        except Exception as e:
            print(f"Erro ao cadastrar usuário: {e}")
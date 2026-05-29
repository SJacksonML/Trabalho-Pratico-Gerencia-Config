from datetime import datetime

from livro import Livro
from usuario import Usuario
from emprestimo import Emprestimo

class Aplication():
    '''Classe responsável pelos menus para interagir com o sistema'''

    def main_menu():
        '''Menu principal'''
        while True:
            print("Sistema de biblioteca\n1 - Devolver livro (WIP)\n2 - Solicitar empréstimo\n3 - Cadastrar livro\n4 - Menu de buscas\n5 - Sair")
            choice = int(input("Selecione uma opção: "))

            match choice:
                case 1:
                    pass
                case 2:
                    Aplication.loan_menu()
                case 3:
                    Aplication.create_book_menu()
                case 4:
                    Aplication.read_book_menu()
                case 5:
                    print("Desligando o sistema...")
                    break
                case _:
                    print("Escolha inválida")

    def read_book_menu():
        while True:
            print("\nMenu de buscas\n1 - Ver livros cadastrados\n2 - Ver autores\n3 - Voltar\n")
            
            choice = int(input("Selecione uma opção: "))

            match choice:
                case 1:
                    busca_livro = Livro("BUSCA","BUSCA",datetime.now())
                    busca_livro.imprimir_livros()
                case 2:
                    busca_livro = Livro("BUSCA","BUSCA",datetime.now())
                    busca_livro.pegar_autores()
                case 3:
                    break
                case _:
                    print("Escolha inválida")
    
    def loan_menu():
        '''Menu de empréstimos'''
        usuario = str(input("Digite seu nome: "))
        livro = str(input("Digite o nome do livro que deseja pegar emprestado: "))
        data = datetime.now()
        codigo = str(input("Digite o código do empréstimo: "))
        novo_emprestimo = Emprestimo(usuario, livro, data, codigo)

        novo_emprestimo.fazer_emprestimo()


    def create_book_menu():
        '''Menu de cadastro de livros'''
        while True:
            print("\nMenu de cadastro de livros\n1 - Realizar cadastro\n2 - Voltar\n")

            choice = int(input("Selecione uma opção: "))

            match choice:
                case 1:
                    nome = str(input("Digite o nome do seu livro: "))
                    autor = str(input("Digite o nome do autor: "))
                    data = datetime.now()
                    novo_livro = Livro(nome, autor, data)
                    novo_livro.criar_livro(nome, autor, data)
                    break
                case 2:
                    break
                case _:
                    print("Escolha inválida")

Aplication.main_menu()

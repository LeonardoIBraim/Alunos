import sqlite3
import bancodb
import os


class Alunos:
    def __init__(self, nome, sobrenome, data_nasc, rg, matricula, curso, periodo, materia, nota):
        # Conexão com o Banco de Dados
        self.conn = sqlite3.connect("banco.db")
        self.cursor = self.conn.cursor()
        # Atributos do Aluno
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nasc = data_nasc
        self.rg = rg
        self.matricula = matricula
        self.curso = curso
        self.periodo = periodo
        self.materia = materia
        self.nota = nota

    def menu(self):  # Menu de opções
        while True:
            print("Seja Bem-Vindo ao Cadastro de Alunos!")
            resp = input(
                "\n1-Criar Aluno\n""2-Acessar Dados Do Aluno\n""3-Atualizar Aluno\n""4-Deletar Aluno\n""5-Finalizar Programa\n""\nEscolha uma opção: ")

            if resp == "1":  # Criação do Aluno
                self.nome = input("Digite seu nome: ")
                self.sobrenome = input("Digite seu sobrenome: ")
                self.data_nasc = input("Informe sua data de nascimento (Ex: DD/MM/YYYY): ")
                self.rg = input("Digite o seu rg: ")
                self.matricula = input("Digite sua matrícula: ")
                self.curso = input("Informe seu curso: ")

                try:
                    self.periodo = int(input("Informe seu período(Ex: 1):  "))
                    qtd_nt = int(input("Quantas notas você deseja inserir? "))
                    i = 0
                    while i < qtd_nt:  # Aqui é para saber quantas notas o aluno deseja inserir
                        self.materia = input("Digite uma matéria: ")
                        self.nota = float(input("Digite uma nota: "))
                        comando = '''INSERT INTO Notas(matricula, curso, periodo, materia, nota) VALUES(?,?,?,?,?)'''
                        dados_notas = (aluno.matricula, aluno.curso, aluno.periodo, aluno.materia, aluno.nota)
                        self.cursor.execute(comando, dados_notas)
                        i = i + 1

                    comando = '''INSERT INTO Aluno(matricula, nome, sobrenome, data_nasc, rg) VALUES(?,?,?,?,?)'''
                    dados_aluno = (aluno.matricula, aluno.nome, aluno.sobrenome, aluno.data_nasc, aluno.rg)
                    self.cursor.execute(comando, dados_aluno)

                except ValueError:  # Aqui é onde eu trato o erro
                    input("\nInsira um número válido!\n""Tente novamente")

                else:
                    print("\nAluno criado com sucesso.")
                    input("Aperte enter para voltar ao início!")
                    os.system('cls')

            elif resp == "2":  # Acessar Dados Aluno
                self.matricula = input("Informe a sua matrícula: ")

                # Aqui é a consulta para obter os dados pessoais do aluno
                comando = f"SELECT * FROM Aluno WHERE matricula = '{self.matricula}'"
                self.cursor.execute(comando)
                for linha in self.cursor.fetchall():
                    matricula, nome, sobrenome, data_nasc, rg = linha
                    print(
                        f"\nDados do aluno\nMatrícula: {matricula}, Nome: {nome} {sobrenome}, Data de Nascimento: {data_nasc}, RG: {rg}")

                # E aqui a consulta para obter as notas do aluno
                comando = f"SELECT * FROM Notas WHERE matricula = '{self.matricula}'"
                self.cursor.execute(comando)
                for linha in self.cursor.fetchall():
                    id, matricula, curso, periodo, materia, nota = linha
                    print(
                        f"ID: {id}, Matrícula: {matricula}, Curso: {curso}, Período: {periodo}, Matéria: {materia}, Nota: {nota}")
                input("\nAperte enter para voltar ao início!\n")
                os.system('cls')

            elif resp == "3":  # Atualizar dados do aluno
                self.matricula = input("Informe a sua matrícula: ")
                opcao = input(
                    "\nQual opção deseja?\n""1-Atualizar Dados Pessoais""\n2-Atualizar Notas\n""\nEscolha uma opção: ")
                if opcao == "1":
                    # Atualização dos dados pessoais do aluno
                    novo_nome = input("Digite o novo nome: ")
                    novo_sobrenome = input("Digite o novo sobrenome: ")
                    nova_data = input("Digite a nova data de nascimento: ")
                    novo_rg = input("Digite o novo rg: ")
                    comando = f"UPDATE Aluno SET nome = '{novo_nome}', sobrenome = '{novo_sobrenome}', data_nasc = '{nova_data}', rg = '{novo_rg}' WHERE matricula = '{self.matricula}'"
                    self.cursor.execute(comando)
                    print("Aluno atualizado com sucesso.")
                    input("Aperte enter para voltar ao início!\n")
                    os.system('cls')

                elif opcao == "2":
                    try:
                        # Atualização das notas do aluno
                        novo_curso = input("Digite o novo curso: ")
                        novo_periodo = int(input("Digite o novo periodo: "))
                        informe_id = int(input("Informe o id da nota e da matéria em que deseja atualizar: "))
                        self.comando = f"SELECT * FROM Notas WHERE id = '{informe_id}'"
                        self.cursor.execute(self.comando)

                        nova_materia = input("Digite a nova matéria: ")
                        nova_nota = float(input("Digite a nova nota: "))
                        comando = f"UPDATE Notas SET curso = '{novo_curso}', periodo = '{novo_periodo}', materia = '{nova_materia}', nota = '{nova_nota}' WHERE id = '{informe_id}'"
                        self.cursor.execute(comando)
                        print("Aluno atualizado com sucesso.")
                        input("Aperte enter para voltar ao início!\n")
                        os.system('cls')
                    except ValueError:  # Tratamento de erro
                        print("\nInsira um número válido!")
                        input("Aperte enter para voltar ao início!\n")
                        os.system('cls')
                else:
                    input("Opção inválida." " Tente novamente!\n")
                    os.system('cls')

            elif resp == "4":  # Deletar aluno
                self.matricula = input("Informe a sua matrícula: ")
                opcaodel = input("\nQual opção deseja?\n""\n1-Deletar Nota""\n2-Deletar Tudo\n""\nEscolha uma opção: ")
                if opcaodel == "1":
                    # Aqui é onde eu deleto a nota do aluno
                    try:
                        id_nota = int(input("Informe o id da nota que você deseja deletar? "))
                        comando = f"DELETE FROM Notas WHERE id='{id_nota}' AND matricula = '{self.matricula}'"
                        self.cursor.execute(comando)
                        print("Nota deletada com sucesso")
                        input("Aperte enter para voltar ao início!\n")
                        os.system('cls')
                    except ValueError:  # Tratamento de erro
                        print("\nInsira um id válido!")
                        input("Aperte enter para voltar ao início!\n")

                elif opcaodel == "2":
                    # Aqui é onde eu deleto todos os dados do aluno
                    comando = f"DELETE FROM Aluno WHERE matricula = '{self.matricula}'"
                    self.cursor.execute(comando)
                    comando = f"DELETE FROM Notas WHERE matricula = '{self.matricula}'"
                    self.cursor.execute(comando)
                    print("Aluno deletado com sucesso")
                    input("Aperte enter para voltar ao início!\n")
                    os.system('cls')

                else:  # Tratamento se caso o aluno digitar alguma opção inválida
                    print("Opção inválida.")
                    input("Aperte enter para voltar ao início!\n")
                    os.system('cls')

            elif resp == "5":  # Finalização do programa
                break

            else:  # Tratamento se caso o aluno digitar uma opção inválida no menu
                input("Opção inválida." " Tente novamente!\n")
            self.conn.commit()


# Instanciação da classe Alunos e chamada do método menu
aluno = Alunos("Leonardo", "da Silva", "18/08/1995", "151415141512", "101953636353", "ADS", 1, "python", 7.7)
aluno.menu()
aluno.conn.close()

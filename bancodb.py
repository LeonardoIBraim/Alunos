import sqlite3 as conector
try:
    # Conexão com o banco de dados
    conexao = conector.connect("banco.db")
    cursor = conexao.cursor()

    # Criação da tabela Aluno
    comando = '''CREATE TABLE IF NOT EXISTS Aluno(
                matricula TEXT PRIMARY KEY NOT NULL,
                nome TEXT NOT NULL,
                sobrenome TEXT NOT NULL,
                data_nasc TEXT NOT NULL,
                rg TEXT NOT NULL
                );'''
    cursor.execute(comando)
    conexao.commit()

    # Criação da tabela Notas
    comando = '''CREATE TABLE IF NOT EXISTS Notas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                matricula TEXT NOT NULL,
                curso TEXT NOT NULL,
                periodo INT NOT NULL,
                materia TEXT NOT NULL,
                nota FLOAT NOT NULL,
                FOREIGN KEY (matricula) REFERENCES Aluno(matricula)
                ); '''
    cursor.execute(comando)
    conexao.commit()


# Tratamento de erros 
except conector.DatabaseError as err:
    print("Erro de Banco de Dados", err)
except conector.ProgrammingError as err:
    print("Erro de Progamação", err)
except conector.IntegrityError as err:
    print("Erro de Integridade", err)
except conector.OperationalError as err:
    print("Erro Operacional:", err)
except Exception as err:
    print("Erro não esperado:", err)
finally: # Fechamento do cursor e da conexão com obanco de dados
    if cursor:
        cursor.close()
    if conexao:
        conexao.close()

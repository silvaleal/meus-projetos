# `📗` Organização de uso.

```python
# Banco de dados: SQLITE3.
import sqlite3 # Não precisa instalar no pip.

def conectarDB():
    return sqlite3.connect('database.db')

# Banco de dados: MySQL.
# import pymysql # pip install pymysql ( DOC: https://pymysql.readthedocs.io/en/latest/ )
               # PYPI -> https://pypi.org/project/pymysql/

# def conectarDB():
#     host='', 
#     user='',
#     password = "",
#     database='',
#     conexao = pymysql.connect(
#         host=host,
#         user=user,
#         password=password,
#         database=database)
#     return conexao

# tb - tabela (table)
class DataScanningDB:
    def __init__(self):
        try:
            self.conexao = conectarDB()
            self.cursor = self.conexao.cursor()
            self.tb_membroslogs()
        except Exception as error:
            print()
            print(f" Algo deu errado no meio da conexão com o banco de dados.")
            print(f' Problema: {error}')
            print()
            exit() # Vai desligar o bot.

    def tb_membroslogs(self): # Tipos: entrada & saida.
        self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS membros_logs (
                user_id INT(30),
                tipo VARCHAR(20),
                data DATA
            )
        ''')
  
    def add_membroslogs(self, user_id, tipo, data):
        self.cursor.execute(f'''
            INSERT INTO membros_logs (user_id, tipo, data)
            VALUES ({user_id}, "{tipo}", "{data}")
        ''')
        self.conexao.commit()

    def get_membroslogs(self):
        self.cursor.execute(f'''
            SELECT tipo, COUNT(*) AS quantidade
            FROM membros_logs
            GROUP BY tipo;
        ''')
        return self.cursor.fetchall()

```

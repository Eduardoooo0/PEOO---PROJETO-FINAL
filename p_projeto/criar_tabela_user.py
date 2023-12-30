import sqlite3

conexao = sqlite3.connect('tabela_filmes.db')
sql = conexao.cursor()

sql.execute('CREATE TABLE filmes (titulo,categoria,duracao,data,diretor)')
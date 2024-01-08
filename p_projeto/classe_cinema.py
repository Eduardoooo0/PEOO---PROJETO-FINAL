import sqlite3
import messagebox
class Cinema:
    def __init__(self):
        self.lista_ttl = ['JOGOS VORAZES: A CANTIGA DOS PÁSSAROS E DAS SERPENTES','LEO','MUSSUM:O FILMIS','PATRULHA CANINA:UM FILME SUPERPODEROSO']
        self.lista_ctg = ['Ficção Científica/Ação/Aventura',' Animação/Família/Aventura/Comédia','Biografia','Animação/Família/Aventura']
        self.lista_drc = ['2h 38min','1h 42min','2h 2min','1h 33min']
        self.lista_data = ['15 de novembro de 2023','22 de novembro de 2023','2 de novembro de 2023 ','5 de outubro de 2023']
        self.lista_drt = ['Francis Lawrence','Robert Smigel','Silvio Guindane','Cal Brunker']

    def Consultar_filme(self):
        try:
            self.conexao = sqlite3.connect('p_projeto/tabela_filmes.db')
            self.sql = self.conexao.cursor()
            self.sql.execute('SELECT * FROM filmes')
            self.pcrfilme = self.sql.fetchall()
            self.dicionario_filmes = {}
            for i in self.pcrfilme:
                self.dicionario_filmes[i[0]] = [i[1],i[2],i[3],i[4]]
            self.conexao.commit()
            self.conexao.close()
            return self.dicionario_filmes
        except:
            messagebox.showwarning('ERRO')
    def Adicionar_filmes(self):
        try:          
            self.conexao = sqlite3.connect('p_projeto/tabela_filmes.db')
            self.sql = self.conexao.cursor()
            for i in range(len(self.lista_ttl)):
                self.sql.execute("INSERT INTO filmes (titulo,categoria,duracao,data,diretor) VALUES (?,?,?,?,?)",(self.lista_ttl[i],self.lista_ctg[i],self.lista_drc[i],self.lista_data[i],self.lista_drt[i],))
            self.conexao.commit()
            self.conexao.close()
        except:
             messagebox.showwarning('ERRO')
add = Cinema()
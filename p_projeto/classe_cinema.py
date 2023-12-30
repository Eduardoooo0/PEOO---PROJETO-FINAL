from tkinter import *
import sqlite3

class Cinema:
    def __init__(self):
        self.lista_ttl = ['JOGOS VORAZES: A CANTIGA DOS PÁSSAROS E DAS SERPENTES','LEO','MUSSUM:O FILMIS','PATRULHA CANINA:UM FILME SUPERPODEROSO']
        self.lista_ctg = ['Ficção Científica/Ação/Aventura',' Animação/Família/Aventura/Comédia','Biografia','Animação/Família/Aventura']
        self.lista_drc = ['2h 38min','1h 42min','2h 2min','1h 33min']
        self.lista_data = ['15 de novembro de 2023','22 de novembro de 2023','2 de novembro de 2023 ','5 de outubro de 2023']
        self.lista_drt = ['Francis Lawrence','Robert Smigel','Silvio Guindane','Cal Brunker']

    def Consultar_filme(self,filme):
        self.conexao = sqlite3.connect('tabela_filmes.db')
        self.sql = self.conexao.cursor()
        self.sql.execute('SELECT * FROM filmes')
        self.pcrfilme = self.sql.fetchall()
        if filme in self.pcrfilme:
            print('oi')
        else:
            print('oii')
        self.conexao.commit()
        self.conexao.close()
        
        # self.caixaPesquisa = Entry(root)
        # self.caixaPesquisa["bg"] = "black"
        # self.caixaPesquisa["borderwidth"] = "0px"
        # self.caixaPesquisa["highlightcolor"] = "white"
        # self.caixaPesquisa["highlightthickness"] = 2
        # ft = tkFont.Font(family='Times', size=14)
        # self.caixaPesquisa["font"] = ft
        # self.caixaPesquisa["fg"] = "white"
        # self.caixaPesquisa["justify"] = "center"
        # self.caixaPesquisa["relief"] = "raised"
        # self.caixaPesquisa.place(x=600, y=20, width=200, height=25)

        # self.botao_pesquisar = tk.Button(root, text="Procurar", bg="black", fg="white", font=ft,command=self.Pesquisa)
        # self.botao_pesquisar.place(x=810, y=20, width=80, height=25)

        # self.filmePesquisado = self.caixaPesquisa.get
        # print(self.filmePesquisado,'aaaaaa')
      
    def Adicionar_filmes(self):
        self.conexao = sqlite3.connect('tabela_filmes.db')
        self.sql = self.conexao.cursor()
        for i in range(len(self.lista_ttl)):
            self.sql.execute("INSERT INTO filmes (titulo,categoria,duracao,data,diretor) VALUES (?,?,?,?,?)",(self.lista_ttl[i],self.lista_ctg[i],self.lista_drc[i],self.lista_data[i],self.lista_drt[i]))
        self.conexao.commit()
        self.conexao.close()
add = Cinema()

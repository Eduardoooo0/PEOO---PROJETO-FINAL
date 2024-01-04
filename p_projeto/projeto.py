
import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image
from classe_cinema import Cinema
from tkinter import messagebox

class App:
    def __init__(self, root):
        self.cine = Cinema()
        self.cont = 0
        root.title("Controle de cinema")
        width = 1394
        height = 789
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root['bg'] = 'black'

        GButton_458 = tk.Button(root)
        GButton_458["activebackground"] = "red"
        GButton_458["bg"] = "black"
        GButton_458["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times', size=14)
        GButton_458["font"] = ft
        GButton_458["fg"] = "white"
        GButton_458["justify"] = "center"
        GButton_458["text"] = "Em cartaz"
        GButton_458.place(x=990, y=20, width=100, height=25)
        GButton_458["command"] = self.GButton_458_command

        GButton_769 = tk.Button(root)
        GButton_769["activebackground"] = "red"
        GButton_769["bg"] = "black"
        GButton_769["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times', size=14)
        GButton_769["font"] = ft
        GButton_769["fg"] = "white"
        GButton_769["justify"] = "center"
        GButton_769["text"] = "Filmes"
        GButton_769.place(x=1110, y=20, width=80, height=25)
        GButton_769["command"] = self.GButton_769_command

        GButton_369 = tk.Button(root)
        GButton_369["activebackground"] = "#260b0b"
        GButton_369["bg"] = "black"
        GButton_369["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times', size=14)
        GButton_369["font"] = ft
        GButton_369["fg"] = "white"
        GButton_369["justify"] = "center"
        GButton_369["text"] = "Minha conta"
        GButton_369["relief"] = "raised"
        GButton_369.place(x=1240, y=20, width=100, height=25)
        GButton_369["command"] = self.GButton_369_command

        GLabel_938 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=33)
        GLabel_938["bg"] = "red"
        GLabel_938["font"] = ft
        GLabel_938["fg"] = "white"
        GLabel_938["justify"] = "center"
        GLabel_938["text"] = "Lançamentos"
        GLabel_938.place(x=550, y=120, width=300, height=55)
        image_spacing = 20

        self.img_jv = ImageTk.PhotoImage(Image.open('p_projeto/imagens/jv.jpg'))
        self.label_jv = tk.Label(root, image=self.img_jv, bg='white')
        self.label_jv.bind('<Button-1>', lambda event: self.Event1(event))
        self.label_jv.place(x=70, y=250)

        self.img_leo = ImageTk.PhotoImage(Image.open('p_projeto/imagens/leo.jpg'))
        self.label_leo = tk.Label(root, image=self.img_leo, bg='white')
        self.label_leo.bind('<Button-1>', lambda event: self.Event2(event))
        self.label_leo.place(x=70 + self.img_jv.width() + image_spacing, y=250)

        self.img_muss = ImageTk.PhotoImage(Image.open('p_projeto/imagens/mussum.jpeg'))
        self.label_muss = tk.Label(root, image=self.img_muss, bg='white')
        self.label_muss.bind('<Button-1>', lambda event: self.Event3(event))
        self.label_muss.place(x=70 + (self.img_jv.width() + image_spacing) * 2, y=250)

        self.img_pc = ImageTk.PhotoImage(Image.open('p_projeto/imagens/p_c.jpeg'))
        self.label_pc = tk.Label(root, image=self.img_pc, bg='white')
        self.label_pc.bind('<Button-1>', lambda event: self.Event4(event))
        self.label_pc.place(x=70 + (self.img_jv.width() + image_spacing) * 3, y=250)

        ft = tkFont.Font(family='Times', size=16)
        self.label_pesquisar = tk.Label(root, text="Pesquisar:", font=ft)
        self.label_pesquisar.place(x=500, y=20, height=25)

        self.caixaPesquisa = tk.Entry(root)
        self.caixaPesquisa["bg"] = "white"
        self.caixaPesquisa["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times', size=14)
        self.caixaPesquisa["font"] = ft
        self.caixaPesquisa["justify"] = "center"
        self.caixaPesquisa["relief"] = "raised"
        self.caixaPesquisa.place(x=600, y=20, width=200, height=25)

        self.botao_pesquisar = tk.Button(root, text="Procurar", font=ft,command=self.Pesquisa)
        self.botao_pesquisar.place(x=810, y=20, width=80, height=25)

    def GButton_458_command(self):
        print("command")

    def GButton_769_command(self):
        print("command")

    def GButton_369_command(self):
        print("command")

    def GButton_978_command(self):
        print("command")
    def Pesquisa (self):
        self.filmePesquisado = self.caixaPesquisa.get()
        self.filmePesquisado = self.filmePesquisado.upper()
        self.dicionario = self.cine.Consultar_filme()
        self.dicionariocvs = self.dicionario.keys()
        for i in self.dicionariocvs:
          if self.filmePesquisado in i:
            self.filmeprc = i
            if self.filmeprc == 'JOGOS VORAZES: A CANTIGA DOS PÁSSAROS E DAS SERPENTES':
                self.Detalhes_jv()
            if self.filmeprc == 'LEO':
                self.Detalhes_leo()
            if self.filmeprc == 'MUSSUM:O FILMIS':
                self.Detalhes_mussum()
            if self.filmeprc == 'PATRULHA CANINA:UM FILME SUPERPODEROSO':
                self.Detalhes_pc()

          else:
            pass
    def Detalhes_jv(self):
        self.canva = tk.Canvas(root)
        self.canva.place(x=60,y=100,width=1285,height=600)
        self.imagem = ImageTk.PhotoImage(Image.open('p_projeto/imagens/jv.jpg'))
        self.canva.create_image(200,275,image=self.imagem)
        self.botao = tk.Button(self.canva, text="X", command= lambda:self.Sair(self.canva))
        self.botao['bg'] = 'red'
        self.botao['fg'] = 'white'
        self.botao["borderwidth"] = "0px"
        self.botao.place(x=1250,y=5,height=20,width=30)
        self.canva.create_text(760, 90, text="JOGOS VORAZES: A CANTIGA DOS PÁSSAROS E DAS SERPENTES", font=("Times", 15, "bold"))
        self.canva.create_text(420, 140, text="SINOPSE",fill="gray",font=("Times", 10,"bold"))
        self.canva.create_text(764, 210, text=" Antes de Katniss Everdeen, sua revolução e o envolvimento do 13 distrito,houve o Presidente Snow, ou melhor, Coriolanus Snow. A Cantiga dos\n Pássaros e das Serpentes é a história do ditador de Panem antes de chegar ao poder. Anos antes, Coriolanus Snow vivia na capital,nascido na\n grande casa de Snow, que não anda muito bem em popularidade e financeiramente. Ele se prepara para sua oportunidade de glória como um\n mentor dos Jogos. O destino de sua Casa depende da pequena chance de Coriolanus ser capaz de encantar, enganar e manipular seus colegas\n para conseguir mentorar o tributo vencedor. Foi lhe dado a tarefa humilhante de mentorar a garota tributo do Distrito 12. Os destinos dos\n dois estão agora interligados – toda escolha que Coriolanus fizer terá consequências dentro e fora do Jogo. Na arena, a batalha será mortal\n e a garota terá que sobreviver a cada segundo. Fora da arena, Coriolanus começa a se apegar a garota, mas terá que ter que qualquer passo\n que der, fará com que a menina e ele mesmo sofram de alguma maneira.", font=("Times", 8, "bold"))
        self.canva.create_text(447, 280, text="Data de lançamento:",fill="gray",font=("Times", 10,"bold"))
        self.canva.create_text(575, 280, text="15 de Novembro de 2023",font=("Times", 10,"bold"))
        self.canva.create_text(415, 300, text="Diretor:",fill="gray",font=("Times", 10,"bold"))
        self.canva.create_text(495, 300, text="Francis Lawrence",font=("Times", 10,"bold"))
        self.canva.create_text(424, 320, text="Categoria:",fill="gray",font=("Times", 10,"bold"))
        self.canva.create_text(550, 320, text=" Ficção Científica, Ação, Aventura",font=("Times", 10,"bold"))
        self.canva.create_text(420, 340, text="Duração:",fill="gray",font=("Times", 10,"bold"))
        self.canva.create_text(475, 340, text="2h 38min",font=("Times", 10,"bold"))
        self.botao_comprar = tk.Button(self.canva, text="COMPRAR INGRESSO",bg='red' ,fg='white',font=("Times", 12,"bold"),command=lambda:self.Comprar())
        self.botao_comprar.place(x=700,y=400,height=50,width=250)
    def Detalhes_leo(self):
         self.canva = tk.Canvas(root)
         self.canva.place(x=60,y=100,width=1285,height=600)

         self.imagem = ImageTk.PhotoImage(Image.open('p_projeto/imagens/leo.jpg'))
         self.canva.create_image(200,275,image=self.imagem)
         self.botao = tk.Button(self.canva, text="X", command= lambda:self.Sair(self.canva))
         self.botao['bg'] = 'red'
         self.botao['fg'] = 'white'
         self.botao["borderwidth"] = "0px"
         self.botao.place(x=1250,y=5,height=20,width=30)
         self.canva.create_text(760, 90, text="LEO", font=("Times", 15, "bold"))
         self.canva.create_text(420, 140, text="SINOPSE",fill="gray",font=("Times", 10,"bold"))
         self.canva.create_text(757, 190, text=" Leo (Adam Sandler) é um velho lagarto que está há anos preso com uma tartaruga (Bill Burr) em um terrário na sala de aula de uma escola.\n Então, ao descobrir que tem apenas mais um ano de vida, Leo planeja fugir das quatro paredes de vidro para viver o restante de seu tempo\n no mundo fora. Porém, nada vai como planejado, já que ele se envolve com os problemas da turma. No final, seus últimos desejos não são\n nada como imaginava - ou planejava - mas o resultado o surpreende.", font=("Times", 8, "bold"))
         self.canva.create_text(447, 240, text="Data de lançamento:",fill="gray",font=("Times", 10,"bold"))
         self.canva.create_text(575, 240, text="22 de Novembro de 2023",font=("Times", 10,"bold"))
         self.canva.create_text(415, 260, text="Diretor:",fill="gray",font=("Times", 10,"bold"))
         self.canva.create_text(485, 260, text="Robert Smigel",font=("Times", 10,"bold"))
         self.canva.create_text(424, 280, text="Categoria:",fill="gray",font=("Times", 10,"bold"))
         self.canva.create_text(560, 280, text=" Animação, Família, Aventura, Comédia",font=("Times", 10,"bold"))
         self.canva.create_text(420, 300, text="Duração:",fill="gray",font=("Times", 10,"bold"))
         self.canva.create_text(475, 300, text="1h 42min",font=("Times", 10,"bold"))
         self.botao_comprar = tk.Button(self.canva, text="COMPRAR INGRESSO",bg='red' ,fg='white',font=("Times", 12,"bold"),command=lambda:self.Comprar())
         self.botao_comprar.place(x=700,y=400,height=50,width=250)

    def Detalhes_mussum(self):
         self.canva = tk.Canvas(root)
         self.canva.place(x=60,y=100,width=1285,height=600)

         self.imagem = ImageTk.PhotoImage(Image.open('p_projeto/imagens/mussum.jpeg'))
         self.canva.create_image(200,275,image=self.imagem)
         self.botao = tk.Button(self.canva, text="X", command= lambda:self.Sair(self.canva))
         self.botao['bg'] = 'red'
         self.botao['fg'] = 'white'
         self.botao["borderwidth"] = "0px"

         self.botao.place(x=1250,y=5,height=20,width=30)
         self.canva.create_text(760, 90, text="MUSSUM:O FILMIS", font=("Times", 15, "bold"))
         self.canva.create_text(420, 140, text="SINOPSE",fill="gray",font=("Times", 10,"bold"))
         self.canva.create_text(755, 215, text=" Mussum, o Filmis é uma cinebiografia brasileira dirigida por Silvio Guindane e roteirizada por Paulo Cursino, com base no livro Mussum -\n uma história de Humor e Samba, de Juliano Barreto. A trama mostra a história real sobre a vida e trajetória de Antônio Carlos Bernardes\n Gomes, popularmente apelidado de Mussum - interpretado, no filme, pelo ator Ailton Graça (Carandiru, Travessia). Tendo crescido\n como um garoto pobre, filho de empregada doméstica analfabeta e com passado militar, Mussum ficou conhecido por ter se tornado um\n dos maiores humoristas do Brasil. Além de fundar o grupo musical Os Originais do Samba, ele encontrou seu caminho para a fama\n na televisão após se unir ao famoso quarteto Os Trapalhões, formado por - além dele - Renato Aragão (Gero Camilo), Dedé Santana (Felipe\n Rocha) e Zacarias (Gustavo Nader). Também fazem parte do elenco os atores Thawan Lucas Bandeira, Yuri Marçal, Cacau Protásio, Neusa\n Borges, Jennifer Dias e Cinnara Leal.", font=("Times", 8, "bold"))
         self.canva.create_text(447, 290, text="Data de lançamento:",fill="gray",font=("Times", 10,"bold"))
         self.canva.create_text(575, 290, text="02 de Novembro de 2023",font=("Times", 10,"bold"))
         self.canva.create_text(415, 310, text="Diretor:",fill="gray",font=("Times", 10,"bold"))
         self.canva.create_text(485, 310, text="Silvio Guindane",font=("Times", 10,"bold"))
         self.canva.create_text(424, 330, text="Categoria:",fill="gray",font=("Times", 10,"bold"))
         self.canva.create_text(485, 330, text="Biografia",font=("Times", 10,"bold"))
         self.canva.create_text(420, 350, text="Duração:",fill="gray",font=("Times", 10,"bold"))
         self.canva.create_text(475, 350, text="2h 2min",font=("Times", 10,"bold"))
         self.botao_comprar = tk.Button(self.canva, text="COMPRAR INGRESSO",bg='red' ,fg='white',font=("Times", 12,"bold"),command=lambda:self.Comprar())
         self.botao_comprar.place(x=700,y=400,height=50,width=250)
    def Detalhes_pc(self):
         self.canva = tk.Canvas(root)
         self.canva.place(x=60,y=100,width=1285,height=600)

         self.imagem = ImageTk.PhotoImage(Image.open('p_projeto/imagens/p_c.jpeg'))
         self.canva.create_image(200,275,image=self.imagem)
         self.botao = tk.Button(self.canva, text="X", command= lambda:self.Sair(self.canva))
         self.botao['bg'] = 'red'
         self.botao['fg'] = 'white'
         self.botao["borderwidth"] = "0px"
         self.botao.place(x=1250,y=5,height=20,width=30)
         self.canva.create_text(760, 90, text="PATRULHA CANINA:UM FILME SUPERPODEROSO", font=("Times", 15, "bold"))
         self.canva.create_text(420, 140, text="SINOPSE",fill="gray",font=("Times", 10,"bold"))
         self.canva.create_text(760, 200, text=" Em Patrulha Canina - Um Filme Superpoderoso, os filhotes da Patrulha Canina ganham poderes após um meteoro mágico cair em Adventure\n City. Para um deles, é um grande sonho que se tornou realidade - porém, a felicidade dos patrulheiros pode estar ameaçada quando o maior\n inimigo dos filhotes foge da prisão e se une a uma cientista maluca para tentar roubar seus poderes místicos. Correndo o risco de\n colocar toda a população de Adventure City em sério perigo, a Patrulha Canina agora precisará, mais do que nunca, se manter unida\n independentemente de qual seja o seu tamanho para deter os inimigos antes que seja tarde demais.", font=("Times", 8, "bold"))
         self.canva.create_text(447, 250, text="Data de lançamento:",fill="gray",font=("Times", 10,"bold"))
         self.canva.create_text(570, 250, text="05 de Outubro de 2023",font=("Times", 10,"bold"))
         self.canva.create_text(415, 270, text="Diretor:",fill="gray",font=("Times", 10,"bold"))
         self.canva.create_text(480, 270, text="Cal Brunker",font=("Times", 10,"bold"))
         self.canva.create_text(424, 290, text="Categoria:",fill="gray",font=("Times", 10,"bold"))
         self.canva.create_text(535, 290, text=" Animação, Família, Aventura",font=("Times", 10,"bold"))
         self.canva.create_text(420, 310, text="Duração:",fill="gray",font=("Times", 10,"bold"))
         self.canva.create_text(475, 310, text="1h 43min",font=("Times", 10,"bold"))
         self.botao_comprar = tk.Button(self.canva, text="COMPRAR INGRESSO",bg='red' ,fg='white',font=("Times", 12,"bold"),command=lambda:self.Comprar())
         self.botao_comprar.place(x=700,y=400,height=50,width=250)

    def Sair(self,canva):
        canva.destroy()
    def Event1(self,evento):
      self.Detalhes_jv()
    def Event2(self,evento):
      self.Detalhes_leo()
    def Event3(self,evento):
      self.Detalhes_mussum()
    def Event4(self,evento):
      self.Detalhes_pc()

    def Comprar(self):
      self.canva2 = tk.Canvas(self.canva, width=600, height=400, bg='white')
      self.canva2.place(x=550,y=50)
      self.canva2.create_text(300, 50, text="CINEMA",font=( "Times", 20, "bold"	))
      self.canva2.create_text(300, 80, text="IFRN campus Caicó, 59300-000, Nova caicó",font=( "Times", 10, "bold"	))
      self.canva2.create_text(195, 120, text="Sala:",fill="gray",font=( "Times", 10, "bold"	))
      self.canva2.create_text(215, 120, text="1",font=( "Times", 10, "bold"	))
      self.canva2.create_text(300, 120, text="2D",fill="gray",font=( "Times", 10, "bold"))
      self.canva2.create_text(405, 120, text="DUB",fill="gray",font=( "Times", 10, "bold"))
      self.canva2.create_text(235, 160, text="Quant. de ingressos:",fill="gray",font=( "Times", 10, "bold"))
      self.quant = tk.Entry(self.canva2,font=("Times", 10, "bold"),width=10)
      self.quant["borderwidth"] = "0px"
      self.quant["justify"] = "center"
      self.quant["relief"] = "raised"
      self.quant["bg"] = "gray"
      self.quant.place(x=300,y=150,height=20)
      self.canva2.create_text(230, 190, text="Valor do ingresso:",fill="gray",font=( "Times", 10, "bold"))
      self.canva2.create_text(315, 190, text="R$ 20,00",font=( "Times", 10, "bold"))
      self.botao_ok = tk.Button(self.canva2, text="OK",bg='green' ,fg='white',font=("Times", 10,"bold"),command=lambda:self.Ok(self.quant.get()))
      self.botao_ok["borderwidth"] = "0px"
      self.botao_ok.place(x=375,y=150,height=20)

      self.botao_finalizar = tk.Button(self.canva2, text="FINALIZAR COMPRA",bg='red' ,fg='white',font=("Times", 12,"bold"),command=lambda:self.Finalizar(self.canva2))
      self.botao_finalizar.place(x=180,y=300,height=50,width=250)

      self.botao = tk.Button(self.canva2, text="X", command= lambda:self.Sair(self.canva2))
      self.botao['bg'] = 'red'
      self.botao['fg'] = 'white'
      self.botao["borderwidth"] = "0px"
      self.botao.place(x=565,y=5,height=20,width=30)
    def Ok(self, quant):
      self.cont += 1
      self.valor_final = int(quant) * 20
      if self.cont == 1:
          self.canva2.create_text(240, 230, text="Total a pagar:", fill="gray", font=("Times", 15, "bold"))
          self.textvalor = self.canva2.create_text(330, 230, text=f"R$ {str(self.valor_final)}", font=("Times", 15, "bold"))
      else:
          self.canva2.itemconfig(self.textvalor, text=f"R$ {str(self.valor_final)}")
    def Finalizar(self,canva):
       messagebox.showinfo("Compra finalizada")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

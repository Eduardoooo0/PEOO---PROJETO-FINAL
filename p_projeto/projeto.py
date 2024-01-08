
import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image
from classe_cinema import Cinema
from tkinter import messagebox
import pickle

class App:
    def __init__(self, root):
        self.root = root
        self.cine = Cinema()
        self.cont = 0
        self.root.title("Controle de cinema")
        width = 1394
        height = 789
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)
        self.root['bg'] = 'black'

        self.GLabel_938 = tk.Label(self.root)
        ft = tkFont.Font(family='Times', size=33)
        self.GLabel_938["bg"] = "red"
        self.GLabel_938["font"] = ft
        self.GLabel_938["fg"] = "white"
        self.GLabel_938["justify"] = "center"
        self.GLabel_938["text"] = "Lançamentos"
        self.GLabel_938.place(x=550, y=120, width=300, height=55)
        image_spacing = 20

        self.img_jv = ImageTk.PhotoImage(Image.open('imagens/jv.jpg'))
        self.label_jv = tk.Label(self.root, image=self.img_jv, bg='white')
        self.label_jv.bind('<Button-1>', lambda event: self.Event1(event))
        self.label_jv.place(x=70, y=250)

        self.img_leo = ImageTk.PhotoImage(Image.open('imagens/leo.jpg'))
        self.label_leo = tk.Label(self.root, image=self.img_leo, bg='white')
        self.label_leo.bind('<Button-1>', lambda event: self.Event2(event))
        self.label_leo.place(x=70 + self.img_jv.width() + image_spacing, y=250)

        self.img_muss = ImageTk.PhotoImage(Image.open('imagens/mussum.jpeg'))
        self.label_muss = tk.Label(self.root, image=self.img_muss, bg='white')
        self.label_muss.bind('<Button-1>', lambda event: self.Event3(event))
        self.label_muss.place(x=70 + (self.img_jv.width() + image_spacing) * 2, y=250)

        self.img_pc = ImageTk.PhotoImage(Image.open('imagens/p_c.jpeg'))
        self.label_pc = tk.Label(self.root, image=self.img_pc, bg='white')
        self.label_pc.bind('<Button-1>', lambda event: self.Event4(event))
        self.label_pc.place(x=70 + (self.img_jv.width() + image_spacing) * 3, y=250)

        self.l1_texto = "JOGOS VORAZES: A CANTIGA DOS PÁSSAROS E DAS SERPENTES"
        self.l2_texto = "LEO"
        self.l3_texto = "MUSSUM:O FILMIS"
        self.l4_texto = "PATRULHA CANINA:UM FILME SUPERPODEROSO"
        self.nomef = []

        self.GButton_369 = tk.Button(self.root)
        self.GButton_369["activebackground"] = "red"
        self.GButton_369["bg"] = "black"
        self.GButton_369["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times', size=14)
        self.GButton_369["font"] = ft
        self.GButton_369["fg"] = "white"
        self.GButton_369["justify"] = "center"
        self.GButton_369["text"] = "Minha conta"
        self.GButton_369["relief"] = "raised"
        self.GButton_369.place(x=1240, y=20, width=100, height=25)
        self.GButton_369["command"] = self.criar_entrar_conta


    def criar_entrar_conta(self):
      self.canva3 = tk.Canvas(self.root)
      self.canva3['bg'] = 'white'
      self.canva3.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=400, height=220)
      
      self.botao = tk.Button(self.canva3, text="X", command=lambda: self.Sair(self.canva3))
      self.botao['bg'] = 'red'
      self.botao['fg'] = 'white'
      self.botao["borderwidth"] = "0px"
      self.botao.place(relx=0.95, rely=0.05, anchor=tk.CENTER, width=20, height=15)

      self.nome_label = tk.Label(self.canva3, text='Nome do usuário:')
      self.nome_label.place(relx=0.25, rely=0.35, anchor=tk.CENTER)

      self.nome_entry = tk.Entry(self.canva3)
      self.nome_entry.place(relx=0.75, rely=0.35, anchor=tk.CENTER)

      self.senha_label = tk.Label(self.canva3, text='Senha:')
      self.senha_label.place(relx=0.25, rely=0.5, anchor=tk.CENTER)

      self.senha_entry = tk.Entry(self.canva3, show='*')
      self.senha_entry.place(relx=0.75, rely=0.5, anchor=tk.CENTER)

      self.botao_criar_entrar = tk.Button(self.canva3, text='Criar/Entrar Conta', command=self.entra_em_conta)
      self.botao_criar_entrar["bg"] = "red"
      self.botao_criar_entrar["borderwidth"] = "0px"
      self.botao_criar_entrar["fg"] = "white"
      self.botao_criar_entrar["justify"] = "center"
      self.botao_criar_entrar.place(relx=0.5, rely=0.65, anchor=tk.CENTER)



    def entra_em_conta(self):
        
        nome = self.nome_entry.get()
        senha = self.senha_entry.get()
        
        if self.verificar_nome_existente(nome):
            self.GButton_369["text"] = nome
            self.GButton_369.place(x=1240, y=20, width=100, height=25)
            self.GButton_369["command"] = self.b_da_Conta
            self.Sair(self.canva3)
        else:
            self.adicionar_pessoa(nome, senha)

    def verificar_nome_existente(self, nome):
        try:
            arquivo = open("pessoas.bin", "rb")
            pessoas = pickle.load(arquivo)
            for pessoa in pessoas:
                if pessoa["nome"] == nome:
                    arquivo.close()
                    return True
            arquivo.close()
        except FileNotFoundError:
            return False
        
        return False

    def adicionar_pessoa(self, nome, senha):
        pessoa = {"nome": nome, "senha": senha}
        try:
            arquivo = open("pessoas.bin", "rb")
            pessoas = pickle.load(arquivo)
        except FileNotFoundError:
            pessoas = []

        pessoas.append(pessoa)

        try:
            arquivo = open("pessoas.bin", "wb")
            pickle.dump(pessoas, arquivo)
        finally:
            arquivo.close()
    
    

    def b_da_Conta(self):
      self.GButton_369["bg"] = "white"
      self.GButton_369['fg'] = 'black'
      self.menu_conta()
    def menu_conta (self):
      self.canva4 = tk.Canvas(self.root)
      self.canva4['bg'] = 'white'
      self.canva4.place(x=1240, y=45, width=100, height=100)
      
      self.botao = tk.Button(self.canva4, text="X",  command=lambda: self.b_apag_mud(self.canva4))
      self.botao['bg'] = 'red'
      self.botao['fg'] = 'white'
      self.botao["borderwidth"] = "0px"
      self.botao.place(x=81, y=2,  width=19, height=15)

      self.b_sair = tk.Button(self.canva4, text="Sair", command = self.sair_conta)
      self.b_sair['bg'] = 'red'
      self.b_sair['fg'] = 'white'
      self.b_sair["borderwidth"] = "0px"
      self.b_sair.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=100, height=20)
    def b_apag_mud (self,canv):
      canv.destroy()
      self.GButton_369["bg"] = "black"
      self.GButton_369['fg'] = 'white'
       
    def sair_conta(self):
      self.Sair(self.canva4)
      self.GButton_369 = tk.Button(self.root)
      self.GButton_369["activebackground"] = "red"
      self.GButton_369["bg"] = "black"
      self.GButton_369["borderwidth"] = "0px"
      ft = tkFont.Font(family='Times', size=14)
      self.GButton_369["font"] = ft
      self.GButton_369["fg"] = "white"
      self.GButton_369["justify"] = "center"
      self.GButton_369["text"] = "Minha conta"
      self.GButton_369["relief"] = "raised"
      self.GButton_369.place(x=1240, y=20, width=100, height=25)
      self.GButton_369["command"] = self.criar_entrar_conta

    def Detalhes_jv(self):
      self.canva = tk.Canvas(self.root)
      self.canva['bg'] = 'white'
      self.canva.place(x=60, y=100, width=1285, height=600)
      self.imagem = ImageTk.PhotoImage(Image.open('imagens/jv.jpg'))
      self.canva.create_image(200, 275, image=self.imagem)
      self.botao = tk.Button(self.canva, text="X", command=lambda: self.Sair(self.canva))
      self.botao['bg'] = 'red'
      self.botao['fg'] = 'white'
      self.botao["borderwidth"] = "0px"
      self.botao.place(x=1250, y=5, height=20, width=30)

      self.nomef.append(self.l1_texto)
      self.MostraI()

      self.l1 = tk.Label(self.canva, text=self.nomef[len(self.nomef)-1], font=("Times", 15, "bold"), bg='white').place(x=375, y=70)
      self.l = tk.Label(self.canva,text="Antes de Katniss Everdeen, sua revolução e o envolvimento do 13 distrito, houve o Presidente Snow, ou melhor, Coriolanus Snow. A Cantiga dos Pássaros e das Serpentes é a história do ditador de Panem antes de chegar ao poder. Anos antes, Coriolanus Snow vivia na capital, nascido na grande casa de Snow, que não anda muito bem em popularidade e financeiramente. Ele se prepara para sua oportunidade de glória como um mentor dos Jogos. O destino de sua Casa depende da pequena chance de Coriolanus ser capaz de encantar, enganar e manipular seus colegas para conseguir mentorar o tributo vencedor. Foi lhe dado a tarefa humilhante de mentorar a garota tributo do Distrito 12. Os destinos dos dois estão agora interligados – toda escolha que Coriolanus fizer terá consequências dentro e fora do Jogo. Na arena, a batalha será mortal e a garota terá que sobreviver a cada segundo. Fora da arena, Coriolanus começa a se apegar a garota, mas terá que ter que qualquer passo que der, fará com que a menina e ele mesmo sofram de alguma maneira.",font=("Times", 8, "bold"),anchor="w",justify="left",wraplength=900, bg='white').place(x=375, y=130)   


    def Detalhes_leo(self):
      self.canva = tk.Canvas(self.root)
      self.canva['bg'] = 'white'
      self.canva.place(x=60, y=100, width=1285, height=600)
      self.imagem = ImageTk.PhotoImage(Image.open('imagens/leo.jpg'))
      self.canva.create_image(200, 275, image=self.imagem)
      self.botao = tk.Button(self.canva, text="X", command=lambda: self.Sair(self.canva))
      self.botao['bg'] = 'red'
      self.botao['fg'] = 'white'
      self.botao["borderwidth"] = "0px"
      self.botao.place(x=1250, y=5, height=20, width=30)

      self.nomef.append(self.l2_texto)
      self.MostraI()

      self.l1 = tk.Label(self.canva, text=self.nomef[len(self.nomef)-1], font=("Times", 15, "bold"), bg='white').place(x=375, y=70)
      self.l = tk.Label(self.canva,text="Leo (Adam Sandler) é um velho lagarto que está há anos preso com uma tartaruga (Bill Burr) em um terrário na sala de aula de uma escola.\nEntão, ao descobrir que tem apenas mais um ano de vida, Leo planeja fugir das quatro paredes de vidro para viver o restante de seu tempo\nno mundo fora. Porém, nada vai como planejado, já que ele se envolve com os problemas da turma. No final, seus últimos desejos não são\nnada como imaginava - ou planejava - mas o resultado o surpreende.",font=("Times", 8, "bold"),anchor="w",justify="left",wraplength=900, bg='white').place(x=375, y=130)


    def Detalhes_mussum(self):
        self.canva = tk.Canvas(self.root)
        self.canva['bg'] = 'white'
        self.canva.place(x=60,y=100,width=1285,height=600)
        self.imagem = ImageTk.PhotoImage(Image.open('imagens/mussum.jpeg'))
        self.canva.create_image(200,275,image=self.imagem)
        self.botao = tk.Button(self.canva, text="X", command= lambda:self.Sair(self.canva))
        self.botao['bg'] = 'red'
        self.botao['fg'] = 'white'
        self.botao["borderwidth"] = "0px"
        self.botao.place(x=1250,y=5,height=20,width=30)

        self.nomef.append(self.l3_texto)
        self.MostraI()

        self.l1 = tk.Label(self.canva, text=self.nomef[len(self.nomef)-1], font=("Times", 15, "bold"), bg='white').place(x=375, y=70)
        self.l = tk.Label(self.canva,text=" Mussum, o Filmis é uma cinebiografia brasileira dirigida por Silvio Guindane e roteirizada por Paulo Cursino, com base no livro Mussum -\n uma história de Humor e Samba, de Juliano Barreto. A trama mostra a história real sobre a vida e trajetória de Antônio Carlos Bernardes\n Gomes, popularmente apelidado de Mussum - interpretado, no filme, pelo ator Ailton Graça (Carandiru, Travessia). Tendo crescido\n como um garoto pobre, filho de empregada doméstica analfabeta e com passado militar, Mussum ficou conhecido por ter se tornado um\n dos maiores humoristas do Brasil. Além de fundar o grupo musical Os Originais do Samba, ele encontrou seu caminho para a fama\n na televisão após se unir ao famoso quarteto Os Trapalhões, formado por - além dele - Renato Aragão (Gero Camilo), Dedé Santana (Felipe\n Rocha) e Zacarias (Gustavo Nader). Também fazem parte do elenco os atores Thawan Lucas Bandeira, Yuri Marçal, Cacau Protásio, Neusa\n Borges, Jennifer Dias e Cinnara Leal.", font=("Times", 8, "bold"),anchor="w",justify="left",wraplength=900, bg='white').place(x=375, y=130)


    def Detalhes_pc(self):
        self.canva = tk.Canvas(self.root)
        self.canva['bg'] = 'white'
        self.canva.place(x=60,y=100,width=1285,height=600)
        self.imagem = ImageTk.PhotoImage(Image.open('imagens/p_c.jpeg'))
        self.canva.create_image(200,275,image=self.imagem)
        self.botao = tk.Button(self.canva, text="X", command= lambda:self.Sair(self.canva))
        self.botao['bg'] = 'red'
        self.botao['fg'] = 'white'
        self.botao["borderwidth"] = "0px"
        self.botao.place(x=1250,y=5,height=20,width=30)

        self.nomef.append(self.l4_texto)
        self.MostraI()

        self.l1 = tk.Label(self.canva, text=self.nomef[len(self.nomef)-1], font=("Times", 15, "bold"), bg='white').place(x=375, y=70)
        self.l = tk.Label(self.canva, text=" Em Patrulha Canina - Um Filme Superpoderoso, os filhotes da Patrulha Canina ganham poderes após um meteoro mágico cair em Adventure\n City. Para um deles, é um grande sonho que se tornou realidade - porém, a felicidade dos patrulheiros pode estar ameaçada quando o maior\n inimigo dos filhotes foge da prisão e se une a uma cientista maluca para tentar roubar seus poderes místicos. Correndo o risco de\n colocar toda a população de Adventure City em sério perigo, a Patrulha Canina agora precisará, mais do que nunca, se manter unida\n independentemente de qual seja o seu tamanho para deter os inimigos antes que seja tarde demais.",font=("Times", 8, "bold"),anchor="w",justify="left",wraplength=900, bg='white').place(x=375, y=130)


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
    
    def MostraI(self):

      self.l = tk.Label(self.canva, text="SINOPSE", fg="gray", font=("Times", 10, "bold"), bg='white').place(x=375, y=110)
      self.l = tk.Label(self.canva, text="Data de lançamento:", fg="gray", font=("Times", 10, "bold"), bg='white').place(x=375, y=240)
      self.l = tk.Label(self.canva, text="Diretor:", fg="gray", font=("Times", 10, "bold"), bg='white').place(x=375, y=280)
      self.l = tk.Label(self.canva, text="Categoria:", fg="gray", font=("Times", 10, "bold"), bg='white').place(x=375, y=320)
      self.l = tk.Label(self.canva, text="Duração:", fg="gray", font=("Times", 10, "bold"), bg='white').place(x=375, y=360)
      self.filmedatela = self.nomef[len(self.nomef)-1]
      self.dicionario = self.cine.Consultar_filme()
      self.dicionariocvs = self.dicionario.keys()
      for i in self.dicionariocvs:
        if self.filmedatela in i:
          self.filmeprc = i
          if self.filmeprc == 'JOGOS VORAZES: A CANTIGA DOS PÁSSAROS E DAS SERPENTES':
            self.MostraDetalhes(self.filmeprc)
          if self.filmeprc == 'LEO':
             self.MostraDetalhes(self.filmeprc)
          if self.filmeprc == 'MUSSUM:O FILMIS':
            self.MostraDetalhes(self.filmeprc)
          if self.filmeprc == 'PATRULHA CANINA:UM FILME SUPERPODEROSO':
            self.MostraDetalhes(self.filmeprc)

        else:
          pass
      self.botao_comprar = tk.Button(self.canva, text="COMPRAR INGRESSO", bg='red', fg='white', font=("Times", 12, "bold"), borderwidth='0px', command=lambda: self.Comprar())
      self.botao_comprar.place(x=580, y=425, height=50, width=250)

    def MostraDetalhes (self,filmeMostrado):
      self.dicionario = self.cine.Consultar_filme()
      self.infom = self.dicionario[filmeMostrado]
      self.l = tk.Label(self.canva, text=self.infom[2], font=("Times", 10, "bold"), bg='white').place(x=500, y=240)
      self.l = tk.Label(self.canva, text=self.infom[3], font=("Times", 10, "bold"), bg='white').place(x=500, y=280)
      self.l = tk.Label(self.canva, text=self.infom[0], font=("Times", 10, "bold"), bg='white').place(x=500, y=320)
      self.l = tk.Label(self.canva, text=self.infom[1], font=("Times", 10, "bold"), bg='white').place(x=500, y=360)
    

    def Comprar(self):
        self.canva2 = tk.Canvas(self.canva, width=600, height=400, bg='white')
        self.canva2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.canva2.create_text(300, 50, text="CINEMA", font=("Times", 20, "bold"))
        self.canva2.create_text(300, 80, text="IFRN campus Caicó, 59300-000, Nova caicó", font=("Times", 10, "bold"))
        self.canva2.create_text(195, 120, text="Sala:", font=("Times", 10, "bold"))
        self.canva2.create_text(215, 120, text="1", font=("Times", 10, "bold"))
        self.canva2.create_text(300, 120, text="2D", font=("Times", 10, "bold"))
        self.canva2.create_text(405, 120, text="DUB", font=("Times", 10, "bold"))
        self.canva2.create_text(235, 160, text="Quant. de ingressos:", font=("Times", 10, "bold"))
        self.quant = tk.Entry(self.canva2, font=("Times", 10, "bold"), width=10)
        self.quant["borderwidth"] = "0px"
        self.quant["justify"] = "center"
        self.quant["relief"] = "raised"
        self.quant["bg"] = "gray"
        self.quant.place(x=300, y=150, height=20)
        self.canva2.create_text(230, 190, text="Valor do ingresso:", font=("Times", 10, "bold"))
        self.canva2.create_text(315, 190, text="R$ 20,00", font=("Times", 10, "bold"))
        self.botao_ok = tk.Button(self.canva2, text="OK", bg='green', fg='white', font=("Times", 10, "bold"), command=lambda: self.Ok(self.quant.get()))
        self.botao_ok["borderwidth"] = "0px"
        self.botao_ok.place(x=375, y=150, height=20)

        self.botao_finalizar = tk.Button(self.canva2, text="FINALIZAR COMPRA", bg='red', fg='white', font=("Times", 12, "bold"), borderwidth='0px', command=lambda: self.Finalizar(self.canva2))
        self.botao_finalizar.place(x=180, y=300, height=50, width=250)

        self.botao = tk.Button(self.canva2, text="X", command=lambda: self.Sair(self.canva2))
        self.botao['bg'] = 'red'
        self.botao['fg'] = 'white'
        self.botao["borderwidth"] = "0px"
        self.botao.place(x=565, y=5, height=20, width=30)

    def Ok(self, quant):
        self.valor_final = int(quant) * 20

        self.v = tk.Label(self.canva2, text="Total a pagar:", font=("Times", 15, "bold"), bg='white').place(x=180, y=230)
        self.v = tk.Label(self.canva2, text=f"R$ {str(self.valor_final)}", font=("Times", 15, "bold"), bg='white').place(x=305, y=230)

    def Finalizar(self, canva):
        messagebox.showinfo("Compra finalizada")

    def fazer_backup(self):
        try:
            with open('backup_dados.pickle', 'wb') as arquivo:
              pickle.dump(self.cine, arquivo)
              messagebox.showinfo("Backup", "Backup dos dados realizado com sucesso.")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao fazer o backup: {str(e)}")


if __name__ == "__main__":
    janela = tk.Tk()
    app = App(janela)
    janela.mainloop()





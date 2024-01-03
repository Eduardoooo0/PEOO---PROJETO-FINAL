
import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image
from classe_cinema import Cinema


class App:
    def __init__(self, root):
        self.cine = Cinema()
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
        self.label_jv.bind('<Button-1>', lambda event: self.Detalhes_jv(event))
        self.label_jv.place(x=70, y=250)

        self.img_leo = ImageTk.PhotoImage(Image.open('p_projeto/imagens/leo.jpg'))
        self.label_leo = tk.Label(root, image=self.img_leo, bg='white')
        self.label_leo.bind('<Button-1>', lambda event: self.Detalhes_leo(event))
        self.label_leo.place(x=70 + self.img_jv.width() + image_spacing, y=250)

        self.img_muss = ImageTk.PhotoImage(Image.open('p_projeto/imagens/mussum.jpeg'))
        self.label_muss = tk.Label(root, image=self.img_muss, bg='white')
        self.label_muss.bind('<Button-1>', lambda event: self.Detalhes_mussum(event))
        self.label_muss.place(x=70 + (self.img_jv.width() + image_spacing) * 2, y=250)

        self.img_pc = ImageTk.PhotoImage(Image.open('p_projeto/imagens/p_c.jpeg'))
        self.label_pc = tk.Label(root, image=self.img_pc, bg='white')
        self.label_pc.bind('<Button-1>', lambda event: self.Detalhes_pc(event))
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
        if self.filmePesquisado.upper() in self.cine.Consultar_filme():
          pass
        else:
          pass
    def Detalhes_jv(self,evento):
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
    def Detalhes_leo(self,evento):
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
    def Detalhes_mussum(self,evento):
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
    def Detalhes_pc(self,evento):
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
    def Sair(self,canva):
        canva.destroy()




if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()


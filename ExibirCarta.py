import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
from PIL import ImageTk, Image
import Programa

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "testeIMG.ui")

class TesteimgApp:
    def __init__(self, master=None):
        # build ui
        self.toplevel1 = tk.Toplevel()
        self.toplevel1.title("Carta de Descontinuidade")
        self.frame2 = tk.Frame(self.toplevel1)
        self.label1 = tk.Label(self.frame2)
        self.cap_PNG = tk.PhotoImage(file='logo.PNG')
        self.label1.configure(background='#a5d6ef', cursor='gumby', image=self.cap_PNG)
        self.label1.place(anchor='nw', height='100', relx='0.013', rely='0.01', width='150', x='0', y='0')
        self.label2 = ttk.Label(self.frame2)
        self.label2.configure(background='#a5d6ef', font='{eras demi itc} 36 ', text='SHProgram')
        self.label2.place(anchor='nw', relx='0.146', rely='0.02', x='0', y='0')
        self.label3 = ttk.Label(self.frame2)
        self.label3.configure(borderwidth='5', font='{arial} 24 {}', relief='groove', text='Carta de Descontinuidade')
        self.label3.place(anchor='nw', relx='0.6', rely='0.03', width='370', x='0', y='0')
        
        self.button1 = tk.Button(self.frame2)
        self.button1.configure(text='Equipamentos')
        self.button1.place(anchor='nw', relx='0.013', rely='0.237', width='150', x='0', y='0')
        self.button1.configure(command= lambda:[self.limpartree(),self.exDesativados(), self.imagem()])

        self.button2 = tk.Button(self.frame2)
        self.button2.configure(text='Equip em Des.')
        self.button2.place(anchor='nw', relx='0.013', rely='0.327', width='150', x='0', y='0')
        self.button2.configure(command= lambda:[self.limpartree(),self.exDesativadosDes(), self.imagem1()])

        self.entPatriNumSerie = ttk.Entry(self.frame2)
        _text_ = '''Patrimônio ou N° Série'''
        self.entPatriNumSerie.delete('0', 'end')
        self.entPatriNumSerie.insert('0', _text_)
        self.entPatriNumSerie.place(anchor='nw', relx='0.013', rely='0.207', width='150', x='0', y='0')

        self.entNumReg = ttk.Entry(self.frame2)
        _text_ = '''Número de Registro'''
        self.entNumReg.delete('0', 'end')
        self.entNumReg.insert('0', _text_)
        self.entNumReg.place(anchor='nw', relx='0.013', rely='0.297', width='150', x='0', y='0')
        
        self.canvas1 = tk.Canvas(self.frame2)
        self.canvas1.configure(scrollregion = (0,0,5000,5000))
        self.canvas1.place(anchor='nw', height='551', relx='0.146', rely='0.207', width='1107', x='0', y='0')

        self.scrollbar1 = ttk.Scrollbar(self.frame2)
        self.scrollbar1.configure(command=self.canvas1.xview,orient='horizontal')
        self.scrollbar1.place(anchor='nw', relx='0.146', rely='0.977', width='1107', x='0', y='0')
        self.scrollbar2 = ttk.Scrollbar(self.frame2)
        self.scrollbar2.configure(command=self.canvas1.yview,orient='vertical')
        self.scrollbar2.place(anchor='nw', height='551', relx='0.987', rely='0.207', x='0', y='0')
        self.canvas1.config(xscrollcommand=self.scrollbar1.set, yscrollcommand=self.scrollbar2.set)
        
        self.treeview1 = ttk.Treeview(self.frame2)
        self.treeview1.place(anchor='nw', height='60', relx='0.146', rely='0.119', width='1107', x='0', y='0')
        self.frame2.configure(background='#a5d6ef', borderwidth='5', height='730', relief='sunken')
        self.frame2.configure(takefocus=True, width='1330')
        self.frame2.place(anchor='nw', relx='0.003', rely='0.003', x='0', y='0')
        self.toplevel1.configure(background='#669bdb', borderwidth='5', height='700', relief='raised')
        self.toplevel1.configure(takefocus=True, width='1350')
        self.toplevel1.geometry('1350x750')

        app_width =1350
        app_height =750

        screen_width =self.toplevel1.winfo_screenwidth()
        screen_height=self.toplevel1.winfo_screenheight()

        x = (screen_width/2)-(app_width/2)
        y = (screen_height/2)-(app_height/2)

        self.toplevel1.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')


        self.treeview1['columns']=('c1','c2','c3','c4','c5')
        self.treeview1.column('#0',width=0)
        self.treeview1.column('c1',width=100)
        self.treeview1.column('c2',width=100)
        self.treeview1.column('c3',width=100)
        self.treeview1.column('c4',width=100)
        self.treeview1.column('c5',width=500)
        self.treeview1.heading('#0',text='')
        self.treeview1.heading('#1',text='Nome Técnico')
        self.treeview1.heading('#2',text='Modelo')
        self.treeview1.heading('#3',text='Data de Treinamento')
        self.treeview1.heading('#4',text='Treinados')
        

        # Main widget
        self.mainwindow = self.toplevel1

    def imagem(self):
        x = Programa.exibirFotosDesativ(self.entPatriNumSerie.get())
        self.img = ImageTk.PhotoImage(Image.open(x)) 
        self.canvas1.create_image(1,1, anchor='nw', image=self.img)
        self.canvas1.image = self.img

    def imagem1(self):
        x = Programa.exibirFotosDesativDes(self.entNumReg.get())
        self.img = ImageTk.PhotoImage(Image.open(x)) 
        self.canvas1.create_image(1,1, anchor='nw', image=self.img)
        self.canvas1.image = self.img

    def limpartree(self):
        self.treeview1.delete(*self.treeview1.get_children())

    def exDesativados(self):
        self.treeview1['columns']=('c1','c2','c3','c4','c5','c6','c7','c8')
        self.treeview1.column('#0',width=0)
        self.treeview1.column('c1',width=100)
        self.treeview1.column('c2',width=100)
        self.treeview1.column('c3',width=100)
        self.treeview1.column('c4',width=130)
        self.treeview1.column('c5',width=130)
        self.treeview1.column('c6',width=130)
        self.treeview1.column('c7',width=100)
        self.treeview1.column('c8',width=100)
        self.treeview1.heading('#0',text='')
        self.treeview1.heading('#1',text='Tipo')
        self.treeview1.heading('#2',text='Patrimônio')
        self.treeview1.heading('#3',text='Número de Série')
        self.treeview1.heading('#4',text='Data de Desativação')
        self.treeview1.heading('#5',text='Motivo da Desativação')
        self.treeview1.heading('#6',text='Número do Processo')
        self.treeview1.heading('#7',text='Observação')
        self.treeview1.heading('#8',text='Log In')
        r1 = Programa.ProcDesativados(self.entPatriNumSerie.get())
        for i in r1:
            self.treeview1.insert('','end',values=(i))

    def exDesativadosDes(self):
        self.treeview1['columns']=('c1','c2','c3','c4','c5','c6','c7')
        self.treeview1.column('#0',width=0)
        self.treeview1.column('c1',width=100)
        self.treeview1.column('c2',width=130)
        self.treeview1.column('c3',width=130)
        self.treeview1.column('c4',width=130)
        self.treeview1.column('c5',width=130)
        self.treeview1.column('c6',width=100)
        self.treeview1.column('c7',width=100)
        self.treeview1.heading('#0',text='')
        self.treeview1.heading('#1',text='Tipo')
        self.treeview1.heading('#2',text='Número de Registro')
        self.treeview1.heading('#3',text='Data de Desativação')
        self.treeview1.heading('#4',text='Motivo da Desativação')
        self.treeview1.heading('#5',text='Número do Processo')
        self.treeview1.heading('#6',text='Observação')
        self.treeview1.heading('#7',text='Log In')
        r1 = Programa.ProcDesativadosDes(self.entNumReg.get())
        for i in r1:
            self.treeview1.insert('','end',values=(i))

    def run(self):
        self.mainwindow.mainloop()

def abre():
    app = TesteimgApp()
    app.run()

#abre()

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
        self.toplevel1.title("Exibir Treinamentos")
        self.frame2 = tk.Frame(self.toplevel1)
        self.label1 = tk.Label(self.frame2)
        self.cap_PNG = tk.PhotoImage(file='logo.PNG')
        self.label1.configure(background='#a5d6ef', cursor='gumby', image=self.cap_PNG)
        self.label1.place(anchor='nw', height='100', relx='0.013', rely='0.01', width='150', x='0', y='0')
        self.label2 = ttk.Label(self.frame2)
        self.label2.configure(background='#a5d6ef', font='{eras demi itc} 36 ', text='SHProgram')
        self.label2.place(anchor='nw', relx='0.146', rely='0.02', x='0', y='0')
        self.label3 = ttk.Label(self.frame2)
        self.label3.configure(borderwidth='5', font='{arial} 24 {}', relief='groove', text='Treinamentos')
        self.label3.place(anchor='nw', relx='0.68', rely='0.03', x='0', y='0')
        
        self.button1 = tk.Button(self.frame2)
        self.button1.configure(text='Treinamentos')
        self.button1.place(anchor='nw', relx='0.013', rely='0.302', width='150', x='0', y='0')
        self.button1.configure(command= lambda:[self.limpartree(),self.exTreinados()])

        self.button2 = tk.Button(self.frame2)
        self.button2.configure(text='Exibir Imagem')
        self.button2.place(anchor='nw', relx='0.013', rely='0.342', width='150', x='0', y='0')
        self.button2.configure(command=lambda:[self.limpacanvas() ,self.imagem()])

        x = Programa.NomeTecTreinados()
        r1 = []
        for i in x:
            if i[0] not in r1:
                r1.append(i[0])

        self.combobox3 = ttk.Combobox(self.frame2)
        self.combobox3.configure(cursor='arrow',state="readonly",values=r1)
        self.combobox3.place(anchor='nw', relx='0.013', rely='0.222', width='150', x='0', y='0')

        self.combobox1 = ttk.Combobox(self.frame2)
        self.combobox1.configure(cursor='arrow',state='readonly',values=Programa.ModeloTreinados(self.combobox3.bind("<<ComboboxSelected>>",self.getSelected)))
        self.combobox1.place(anchor='nw', relx='0.013', rely='0.262', width='150', x='0', y='0')
        
        self.canvas1 = tk.Canvas(self.frame2)
        self.canvas1.configure(scrollregion = (0,0,5000,5000))
        self.canvas1.place(anchor='nw', height='542', relx='0.146', rely='0.22', width='1107', x='0', y='0')

        self.scrollbar1 = ttk.Scrollbar(self.frame2)
        self.scrollbar1.configure(command=self.canvas1.xview,orient='horizontal')
        self.scrollbar1.place(anchor='nw', relx='0.146', rely='0.977', width='1107', x='0', y='0')
                           
        self.scrollbar2 = ttk.Scrollbar(self.frame2)
        self.scrollbar2.configure(command=self.canvas1.yview,orient='vertical')
        self.scrollbar2.place(anchor='nw', height='542', relx='0.987', rely='0.22', x='0', y='0')
        self.canvas1.config(xscrollcommand=self.scrollbar1.set, yscrollcommand=self.scrollbar2.set)
        
        self.treeview1 = ttk.Treeview(self.frame2)
        self.treeview1.place(anchor='nw', height='80', relx='0.146', rely='0.105', width='1107', x='0', y='0')

        self.scrollbar3 = ttk.Scrollbar(self.frame2)
        self.scrollbar3.configure(command=self.treeview1.yview,orient='vertical')
        self.scrollbar3.place(anchor='nw', height='80', relx='0.987', rely='0.105', x='0', y='0')
        
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
        self.treeview1.heading('#4',text='Turno')
        

        # Main widget
        self.mainwindow = self.toplevel1

    def imagem(self):
        Item=self.treeview1.focus()
        I1 = self.treeview1.item(Item)['values'][0]
        I2 = self.treeview1.item(Item)['values'][1]
        I3 = self.treeview1.item(Item)['values'][2]
        I4 = self.treeview1.item(Item)['values'][3]
        x = Programa.exibirFotos(I1,I2,I3,I4)
        self.img = ImageTk.PhotoImage(Image.open(x)) 
        self.canvas1.create_image(1,1, anchor='nw', image=self.img)
        self.canvas1.image = self.img

    def limpartree(self):
        self.treeview1.delete(*self.treeview1.get_children())

    def limpacanvas(self):
        self.canvas1.delete('all')

    def exTreinados(self):
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
        self.treeview1.heading('#4',text='Turno')
        r1 = Programa.exibirTreinados(self.combobox3.get(),self.combobox1.get())
        for i in r1:
            self.treeview1.insert('','end',values=(i))

    def run(self):
        self.mainwindow.mainloop()

    def getSelected(self, event):
        self.combobox1['values']=Programa.ModeloTreinados(self.combobox3.get())
        self.combobox1.set('')

def abre():
    app = TesteimgApp()
    app.run()

#abre()

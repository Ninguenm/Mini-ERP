import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
import Programa,ExibirCarta
import AvisoSucess,AvisoNSucess

#PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
#PROJECT_UI = os.path.join(PROJECT_PATH, "inicial.ui")

class InicialApp:
    def __init__(self, master=None):
        # build ui
        self.toplevel1 = tk.Toplevel()
        
        self.toplevel1.title("Exibir Desativados")
        self.frame2 = tk.Frame(self.toplevel1)
        self.treeview1 = ttk.Treeview(self.frame2)
        self.treeview1.place(anchor='nw', height='615', relx='0.13', rely='0.12', width='1130', x='0', y='0')
        self.scrollbar1 = ttk.Scrollbar(self.frame2)
        self.scrollbar1.configure(orient='horizontal',command=self.treeview1.xview)
        self.scrollbar1.place(anchor='nw', relx='0.13', rely='0.977', width='1130', x='0', y='0')
        self.treeview1.configure(xscroll=self.scrollbar1.set)
        
        self.scrollbar2 = ttk.Scrollbar(self.frame2)
        self.scrollbar2.configure(orient='vertical',command=self.treeview1.yview)
        self.scrollbar2.place(anchor='nw', height='615', relx='0.987', rely='0.12', x='0', y='0')
        self.treeview1.configure(yscroll=self.scrollbar2.set)
        
        self.button11 = tk.Button(self.frame2)
        self.button11.configure(text='Equipamentos')
        self.button11.place(anchor='nw', relx='0.013', rely='.20', width='150', x='0', y='0')
        self.button11.configure(command=lambda:[self.limpartree(), self.Desativ_view()])
        
        self.button12 = tk.Button(self.frame2)
        self.button12.configure(text='Equipamentos em Des.')
        self.button12.place(anchor='nw', relx='0.013', rely='0.25', width='150', x='0', y='0')
        self.button12.configure(command=lambda:[self.limpartree(), self.DesativDes_view()])
        
        self.button13 = tk.Button(self.frame2)
        self.button13.configure(text='Cartas de Descontinuidade')
        self.button13.place(anchor='nw', relx='0.013', rely='.30', width='150', x='0', y='0')
        self.button13.configure(command=ExibirCarta.abre)
        
        self.label1 = ttk.Label(self.frame2)
        self.cap_PNG = tk.PhotoImage(file='logo.PNG')
        self.label1.configure(background='#a5d6ef', cursor='gumby', image=self.cap_PNG)
        self.label1.place(anchor='nw', height='100', relx='0.013', rely='0.01', width='150', x='0', y='0')
        self.label2 = ttk.Label(self.frame2)
        self.label2.configure(background='#a5d6ef', font='{eras demi itc} 36 ', text='SHProgram')
        self.label2.place(anchor='nw', relx='0.146', rely='0.02', x='0', y='0')
        self.label3 = ttk.Label(self.frame2)
        self.label3.configure(borderwidth='5', font='{arial} 20 {}', relief='groove', text='HMCC')
        self.label3.place(anchor='nw', relx='0.48', rely='0.04', x='0', y='0')

        '''self.lblCadastrante = tk.Label(self.frame2)
        self.lblCadastrante.configure(background='#a5d6ef', font='{arial} 12 {bold underline}', foreground='#ff0000')
        self.lblCadastrante.place(anchor='nw', relx='0.9', rely='0.00', x='0', y='0')
        self.lblCadastrante.configure(text=(Programa.logado[0]))'''
        
        self.frame2.configure(background='#a5d6ef', borderwidth='5', height=730,width=1330,relief='sunken')
        self.frame2.place(anchor='nw', relx='0.003', rely='0.003', x='0', y='0')
        
        self.toplevel1.configure(background='#669bdb', borderwidth='5', height=700, width=1350, relief='raised')

        app_width =1350
        app_height =750

        screen_width =self.toplevel1.winfo_screenwidth()
        screen_height=self.toplevel1.winfo_screenheight()

        x = (screen_width/2)-(app_width/2)
        y = (screen_height/2)-(app_height/2)

        self.toplevel1.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

        # Main widget
        self.mainwindow = self.toplevel1

    def limpartree(self):
        self.treeview1.delete(*self.treeview1.get_children())

    def Desativ_view(self):
        self.label3.configure(text='Desativações de Equipamentos')
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
        r1 = Programa.TodosDesativados()
        for i in r1:
            self.treeview1.insert('','end',values=(i))

    def DesativDes_view(self):
        self.label3.configure(text='Desativações de Equipamentos em Desenvolvimento')
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
        r1 = Programa.TodosDesativadosDes()
        for i in r1:
            self.treeview1.insert('','end',values=(i))

    def run(self):
        self.mainwindow.mainloop()

    def sair(self):
        self.mainwindow.destroy()
            
def abre():
    app = InicialApp()
    app.run()

#abre()

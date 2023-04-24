import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import pygubu
import Programa,AvisoSucess,AvisoNSucess

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "Treinados.ui")

class TreinadosApp:
    def __init__(self, master=None):
        # build ui
        self.toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        self.toplevel1.title("Cadastrar Treinamento")
        self.frame2 = tk.Frame(self.toplevel1)
        self.label2 = tk.Label(self.frame2)
        self.label2.configure(font='{arial} 16 {}', justify='left', relief='groove', takefocus=True)
        self.label2.configure(text='Treinamento')
        self.label2.place(anchor='nw', relx='0.23', rely='0.04', width='250', x='0', y='0')

        x = Programa.Todos()
        r1 = []
        for i in x:
            if i[2] not in r1:
                r1.append(i[2])

        self.combobox3 = ttk.Combobox(self.frame2)
        self.combobox3.configure(cursor='arrow',state="readonly",values=r1)
        self.combobox3.place(anchor='nw', relx='0.4', rely='0.18', width='220', x='0', y='0')

        self.combobox2 = ttk.Combobox(self.frame2)
        self.combobox2.configure(cursor='arrow',state='readonly',values=Programa.TodosDale(self.combobox3.bind("<<ComboboxSelected>>",self.getSelected)))
        self.combobox2.place(anchor='nw', relx='0.4', rely='0.30', width='220', x='0', y='0')

        '''self.entNometec = tk.Entry(self.frame2)
        self.entNometec.configure(justify='left')
        self.entNometec.place(anchor='nw', relx='0.4', rely='0.18', width='220', x='0', y='0')
        
        self.entModelo = tk.Entry(self.frame2)
        self.entModelo.place(anchor='nw', relx='0.4', rely='0.30', width='220', x='0', y='0')'''
        
        self.entDtTrein = tk.Entry(self.frame2)
        self.entDtTrein.place(anchor='nw', relx='0.4', rely='0.42', width='220', x='0', y='0')
        
        #!!!!!
        self.combobox1 = ttk.Combobox(self.frame2)
        self.combobox1.configure(cursor='arrow',values=['Turno Manhã','Turno Tarde','Turno Noite','Outro: Digite'])
        self.combobox1.place(anchor='nw', relx='0.4', rely='0.54', width='220', x='0', y='0')
        #!!!!!
        
        self.entCaminho = tk.Entry(self.frame2)
        self.entCaminho.delete('0', 'end')
        self.entCaminho.place(anchor='nw', relx='.1', rely='.72', width='350', x='0', y='0')

        self.btnInserir = tk.Button(self.frame2)
        self.btnInserir.configure(text='Anexar Arquivo')
        self.btnInserir.place(anchor='nw', height='20', relx='0.402', rely='0.66', width='220', x='0', y='0')
        self.btnInserir.configure(command=self.inserirArquivo)
        
        self.lblNometec = tk.Label(self.frame2)
        self.lblNometec.configure(relief='groove', takefocus=False, text='*Nome Técnico')
        self.lblNometec.place(anchor='nw', relx='0.10', rely='0.18', width='130', x='0', y='0')
        self.lblModelo = tk.Label(self.frame2)
        self.lblModelo.configure(relief='groove', text='*Modelo')
        self.lblModelo.place(anchor='nw', relx='0.10', rely='0.30', width='130', x='0', y='0')
        self.lblDtTrein = tk.Label(self.frame2)
        self.lblDtTrein.configure(relief='groove', text='*Data de Treinamento')
        self.lblDtTrein.place(anchor='nw', relx='0.10', rely='0.42', width='130', x='0', y='0')
        self.lblTreinados = tk.Label(self.frame2)
        self.lblTreinados.configure(relief='groove', text='Turno')
        self.lblTreinados.place(anchor='nw', relx='0.10', rely='0.54', width='130', x='0', y='0')
        self.lblInserirImg = tk.Label(self.frame2)
        self.lblInserirImg.configure(relief='groove', text='*Inserir Imagem')
        self.lblInserirImg.place(anchor='nw', relx='0.1', rely='0.66', width='130', x='0', y='0')
        
        self.btnCadastrar = tk.Button(self.frame2)
        self.btnCadastrar.configure(font='{Arial} 12 {}', text='Cadastrar')
        self.btnCadastrar.place(anchor='nw', relx='0.23', rely='0.84', width='100', x='0', y='0')
        self.btnCadastrar.configure(command=self.insert)
        
        self.btnSair = tk.Button(self.frame2)
        self.btnSair.configure(font='{Arial} 12 {}', text='Sair')
        self.btnSair.place(anchor='nw', relx='0.54', rely='0.84', width='100', x='0', y='0')
        self.btnSair.configure(command=self.fecha)

        self.label3 = tk.Label(self.frame2)
        self.label3.configure(background='#a5d6ef', font='{Arial} 12 {bold}', foreground='#ff171d', text='* Campos Obrigatórios')
        self.label3.place(anchor='nw', relx='0.60', rely='0.95', x='0', y='0')

        self.frame2.configure(background='#a5d6ef', borderwidth='5', height='485', relief='sunken')
        self.frame2.configure(width='450')
        self.frame2.place(anchor='nw', relx='0.003', rely='0.003', x='0', y='0')
        self.toplevel1.configure(background='#669bdb', borderwidth='5', height='500', relief='raised')
        self.toplevel1.configure(width='465')
        
        app_width =465
        app_height =500

        screen_width =self.toplevel1.winfo_screenwidth()
        screen_height=self.toplevel1.winfo_screenheight()

        x = (screen_width/2)-(app_width/2)
        y = (screen_height/2)-(app_height/2)

        self.toplevel1.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

        

        
        self.mainwindow = self.toplevel1
    

    def run(self):
        self.mainwindow.mainloop()

    def fecha(self):
        self.mainwindow.destroy()

    def inserirArquivo(self):
        r1 = filedialog.askopenfilenames()
        self.entCaminho.insert('0', r1[0])
        return r1[0]

    def getSelected(self, event):
        self.combobox2['values']=Programa.TodosDale(self.combobox3.get())
        self.combobox2.set('')

    def insert(self):
        try:
            Programa.cadastrarTreinados(self.combobox3.get(),self.combobox2.get(),self.entDtTrein.get(),self.combobox1.get(),self.entCaminho.get())
            self.mainwindow.destroy()
            AvisoSucess.abre()
        except:
            AvisoNSucess.abre()
            #raise


def abre():
    app = TreinadosApp()
    app.run()

#abre()


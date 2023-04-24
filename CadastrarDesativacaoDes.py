import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import pygubu
import Programa,AvisoSucess,AvisoNSucess

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "DesativacaoCertissima.ui")

class DesativacaoDesApp:
    def __init__(self, master=None):
        # build ui
        self.toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        self.toplevel1.title("Desativação de Equipamento em Desenv.")
        self.frame2 = tk.Frame(self.toplevel1)
        self.label2 = tk.Label(self.frame2)
        self.label2.configure(font='{arial} 16 {}', justify='left', relief='groove', takefocus=False)
        self.label2.configure(text='Desativação de Equipamento em Desenv.')
        self.label2.place(anchor='nw', relx='0.05', rely='0.04', x='0', y='0')
        self.entNumRegistro = tk.Entry(self.frame2)
        self.entNumRegistro.configure(justify='left')
        self.entNumRegistro.place(anchor='nw', relx='0.33', rely='0.14', width='170', x='0', y='0')
        self.entData_Desativ = tk.Entry(self.frame2)
        self.entData_Desativ.place(anchor='nw', relx='0.33', rely='0.24', width='170', x='0', y='0')
        self.entMotivo_Desativ = tk.Entry(self.frame2)
        self.entMotivo_Desativ.place(anchor='nw', relx='0.33', rely='0.34', width='170', x='0', y='0')
        self.entNum_Processo = tk.Entry(self.frame2)
        self.entNum_Processo.place(anchor='nw', relx='0.33', rely='0.44', width='170', x='0', y='0')
        self.entObs = tk.Entry(self.frame2)
        self.entObs.place(anchor='nw', relx='0.33', rely='0.54', width='170', x='0', y='0')
    
        self.lblNumRegistro = tk.Label(self.frame2)
        self.lblNumRegistro.configure(relief='groove', takefocus=False, text='*Número de Registro')
        self.lblNumRegistro.place(anchor='nw', relx='0.03', rely='0.14', width='130', x='0', y='0')
        self.lblData_Desativ = tk.Label(self.frame2)
        self.lblData_Desativ.configure(relief='groove', text='*Data de Desativação')
        self.lblData_Desativ.place(anchor='nw', relx='0.03', rely='0.24', width='130', x='0', y='0')
        self.lblMotivo_Desativ = tk.Label(self.frame2)
        self.lblMotivo_Desativ.configure(relief='groove', text='*Motivo de Desativação')
        self.lblMotivo_Desativ.place(anchor='nw', relx='0.03', rely='0.34', width='130', x='0', y='0')
        self.lblNum_Processo = tk.Label(self.frame2)
        self.lblNum_Processo.configure(relief='groove', text='*Número de Processo')
        self.lblNum_Processo.place(anchor='nw', relx='0.03', rely='0.44', width='130', x='0', y='0')
        self.lblObs = tk.Label(self.frame2)
        self.lblObs.configure(relief='groove', text='Observação')
        self.lblObs.place(anchor='nw', relx='0.03', rely='0.54', width='130', x='0', y='0')
        
        self.lblCarta = tk.Label(self.frame2)
        self.lblCarta.configure(relief='groove', text='Carta Descontinuidade')
        self.lblCarta.place(anchor='nw', relx='0.037', rely='0.64', width='125', x='0', y='0')
        
        self.btnCadastrar = tk.Button(self.frame2)
        self.btnCadastrar.configure(font='{Arial} 12 {}', text='Cadastrar')
        self.btnCadastrar.place(anchor='nw', relx='0.76', rely='0.32', width='100', x='0', y='0')
        self.btnCadastrar.configure(command=self.insert)

        self.btnAnexar = tk.Button(self.frame2)
        self.btnAnexar.configure(text='Anexar')
        self.btnAnexar.place(anchor='nw', relx='0.33', rely='0.64', width='170',height='20', x='0', y='0')
        self.btnAnexar.configure(command=self.inserirArquivo)
        self.entCaminho = tk.Entry(self.frame2)
        self.entCaminho.place(anchor='nw', relx='0.034', rely='0.68', width='300', x='0', y='0')
        
        self.btnSair = tk.Button(self.frame2)
        self.btnSair.configure(font='{Arial} 12 {}', text='Sair')
        self.btnSair.place(anchor='nw', relx='0.76', rely='0.45', width='100', x='0', y='0')
        self.btnSair.configure(command=self.fecha)
        
        self.label1 = tk.Label(self.frame2)
        self.label1.configure(background='#a5d6ef', font='{arial} 12 {bold underline}', foreground='#ff0000', text="""Atenção! 
A desativação de um equipamento é permanente
e cessa a possibilidade de registrar novas ações.
""")
        self.label1.place(anchor='nw', relx='0.07', rely='0.75', x='0', y='0')
        self.label3 = tk.Label(self.frame2)
        self.label3.configure(background='#a5d6ef', font='{Arial} 12 {bold}', foreground='#ff171d', text='* Campos Obrigatórios')
        self.label3.place(anchor='nw', relx='0.60', rely='0.95', x='0', y='0')
        self.frame2.configure(background='#a5d6ef', borderwidth='5', height='600', relief='sunken')
        self.frame2.configure(width='450')
        self.frame2.place(anchor='nw', relx='0.003', rely='0.003', x='0', y='0')
        self.toplevel1.configure(background='#669bdb', borderwidth='5', height='615', relief='raised')
        self.toplevel1.configure(width='465')

        app_width =465
        app_height =615

        screen_width =self.toplevel1.winfo_screenwidth()
        screen_height=self.toplevel1.winfo_screenheight()

        x = (screen_width/2)-(app_width/2)
        y = (screen_height/2)-(app_height/2)

        self.toplevel1.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')


        # Main widget
        self.mainwindow = self.toplevel1
    

    def run(self):
        self.mainwindow.mainloop()

    def fecha(self):
        self.mainwindow.destroy()

    def inserirArquivo(self):
        r1 = filedialog.askopenfilenames()
        self.entCaminho.insert('0', r1[0])
        return r1[0]

    def insert(self):
        try:
            Programa.cadastrarDesativacaoDes(self.entNumRegistro.get(),self.entData_Desativ.get(),self.entMotivo_Desativ.get(),self.entNum_Processo.get(),self.entObs.get(),self.entCaminho.get())
            self.mainwindow.destroy()
            AvisoSucess.abre()
        except:
            AvisoNSucess.abre()


def abre():
    app = DesativacaoDesApp()
    app.run()

#abre()

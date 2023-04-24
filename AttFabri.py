import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
import Programa,AvisoSucess,AvisoNSucess

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "CadastroFabri.ui")

class CadastrofabriApp:
    def __init__(self, master=None):
        # build ui
        self.toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        self.toplevel1.title("Atualizar Fabricante")
        self.frame2 = tk.Frame(self.toplevel1)

        r1 = Programa.TodosFabri()
        r2 = []
        for i in r1:
            r2.append(i[0])

        self.combobox4 = ttk.Combobox(self.frame2)
        self.combobox4.configure(cursor='arrow',state="readonly",values=r2)
        self.combobox4.place(anchor='nw', relx='0.33', rely='0.20', width='170', x='0', y='0')
        
        self.label2 = tk.Label(self.frame2)
        self.label2.configure(font='{arial} 16 {}', justify='left', relief='groove', takefocus=True)
        self.label2.configure(text='Atualizar Fabricante')
        self.label2.place(anchor='nw', relx='0.17', rely='0.04', width='300', x='0', y='0')
        self.entContato = tk.Entry(self.frame2)
        self.entContato.place(anchor='nw', relx='0.33', rely='0.45', width='170', x='0', y='0')
        self.ent2Contato = tk.Entry(self.frame2)
        self.ent2Contato.place(anchor='nw', relx='0.33', rely='0.50', width='170', x='0', y='0')
        self.entEmail = tk.Entry(self.frame2)
        self.entEmail.place(anchor='nw', relx='0.33', rely='0.55', width='170', x='0', y='0')
        self.entAdress = tk.Entry(self.frame2)
        self.entAdress.place(anchor='nw', relx='0.33', rely='0.60', width='170', x='0', y='0')
        self.entCNPJ = tk.Entry(self.frame2)
        self.entCNPJ.place(anchor='nw', relx='0.33', rely='0.65', width='170', x='0', y='0')
        self.entAutorizada = tk.Entry(self.frame2)
        self.entAutorizada.place(anchor='nw', relx='0.33', rely='0.70', width='170', x='0', y='0')
        self.entCtAutorizada = tk.Entry(self.frame2)
        self.entCtAutorizada.place(anchor='nw', relx='0.33', rely='0.75', width='170', x='0', y='0')
        self.entAutorizada2 = tk.Entry(self.frame2)
        self.entAutorizada2.place(anchor='nw', relx='0.33', rely='0.80', width='170', x='0', y='0')
        self.entCt2Autorizada = tk.Entry(self.frame2)
        self.entCt2Autorizada.place(anchor='nw', relx='0.33', rely='0.85', width='170', x='0', y='0')
        self.entAutorizada3 = tk.Entry(self.frame2)
        self.entAutorizada3.place(anchor='nw', relx='0.33', rely='0.90', width='170', x='0', y='0')
        self.entCt3Autorizada = tk.Entry(self.frame2)
        self.entCt3Autorizada.place(anchor='nw', relx='0.33', rely='0.95', width='170', x='0', y='0')
        
        self.lblEmpresa = tk.Label(self.frame2)
        self.lblEmpresa.configure(relief='groove', takefocus=False, text='*Empresa')
        self.lblEmpresa.place(anchor='nw', relx='0.037', rely='0.20', width='125', x='0', y='0')
        self.lblContato = tk.Label(self.frame2)
        self.lblContato.configure(relief='groove', text='*Contato')
        self.lblContato.place(anchor='nw', relx='0.037', rely='0.45', width='125', x='0', y='0')
        self.lbl2Contato = tk.Label(self.frame2)
        self.lbl2Contato.configure(relief='groove', text='2° Contato')
        self.lbl2Contato.place(anchor='nw', relx='0.037', rely='0.50', width='125', x='0', y='0')
        self.lblEmail = tk.Label(self.frame2)
        self.lblEmail.configure(relief='groove', text='Email Contato')
        self.lblEmail.place(anchor='nw', relx='0.037', rely='0.55', width='125', x='0', y='0')
        self.lblAdress = tk.Label(self.frame2)
        self.lblAdress.configure(relief='groove', text='Endereço Físico')
        self.lblAdress.place(anchor='nw', relx='0.037', rely='0.60', width='125', x='0', y='0')
        self.lblCNPJ = tk.Label(self.frame2)
        self.lblCNPJ.configure(relief='groove', text='CNPJ')
        self.lblCNPJ.place(anchor='nw', relx='0.037', rely='0.65', width='125', x='0', y='0')
        self.lbblAutorizada = tk.Label(self.frame2)
        self.lbblAutorizada.configure(relief='groove', text='Empresa Autorizada')
        self.lbblAutorizada.place(anchor='nw', relx='0.037', rely='0.70', width='125', x='0', y='0')
        self.lblCtAutorizada = tk.Label(self.frame2)
        self.lblCtAutorizada.configure(relief='groove', text='Contato Autorizada')
        self.lblCtAutorizada.place(anchor='nw', relx='0.037', rely='0.75', width='125', x='0', y='0')
        self.lblAutorizada2 = tk.Label(self.frame2)
        self.lblAutorizada2.configure(relief='groove', text='2°Empresa Autorizada')
        self.lblAutorizada2.place(anchor='nw', relx='0.037', rely='0.80', width='125', x='0', y='0')
        self.lblCt2Autorizada = tk.Label(self.frame2)
        self.lblCt2Autorizada.configure(relief='groove', text='Contato 2° Autorizada')
        self.lblCt2Autorizada.place(anchor='nw', relx='0.037', rely='0.85', width='125', x='0', y='0')
        self.lblAutorizada3 = tk.Label(self.frame2)
        self.lblAutorizada3.configure(relief='groove', text='3°Empresa Autorizada')
        self.lblAutorizada3.place(anchor='nw', relx='0.037', rely='0.90', width='125', x='0', y='0')
    
        self.lblCt3Autorizada = tk.Label(self.frame2)
        self.lblCt3Autorizada.configure(relief='groove', text='Contato 3° Autorizada')
        self.lblCt3Autorizada.place(anchor='nw', relx='0.037', rely='0.95', width='125', x='0', y='0')

        self.btnCad = tk.Button(self.frame2)
        self.btnCad.configure(font='{Arial} 12 {}', text='Atualizar')
        self.btnCad.place(anchor='nw', relx='0.75', rely='0.45', width='100', x='0', y='0')
        self.btnCad.configure(command=self.insert)
        
        self.btnSair = tk.Button(self.frame2)
        self.btnSair.configure(font='{Arial} 12 {}', text='Sair')
        self.btnSair.place(anchor='nw', relx='0.75', rely='0.60', width='100', x='0', y='0')
        self.btnSair.configure(command=self.fecha)

        self.label3 = tk.Label(self.frame2)
        self.label3.configure(background='#a5d6ef', font='{Arial} 12 {bold}', foreground='#ff171d', text='Insira o Fabricante a ser Atualizado')
        self.label3.place(anchor='nw', relx='0.037', rely='0.15', x='0', y='0')

        self.label4 = tk.Label(self.frame2)
        self.label4.configure(background='#a5d6ef', font='{Arial} 12 {bold}', foreground='#ff171d', text="""Preencha os campos que deseja atualizar,
caso não queira atualizar algum campo
basta deixá-lo em branco""")
        self.label4.place(anchor='nw', relx='0.037', rely='0.285', x='0', y='0')
        
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

    def insert(self):
        try:
            Programa.AlterarFabri(self.entEmpresa.get(),self.entContato.get(),self.ent2Contato.get(),self.entEmail.get(),self.entAdress.get(),self.entCNPJ.get(),self.entAutorizada.get(),self.entCtAutorizada.get(),self.entAutorizada2.get(),self.entCt2Autorizada.get(),self.entAutorizada3.get(),self.entCt3Autorizada.get())
            self.mainwindow.destroy()
            AvisoSucess.abre()
        except:
            AvisoNSucess.abre()


def abre():
    app = CadastrofabriApp()
    app.run()

#abre()

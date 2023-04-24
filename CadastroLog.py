import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
import Programa
import AvisoSucess

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "CadastroLogin.ui")

class CadastrologinApp:
    def __init__(self, master=None):
        # build ui
        self.toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        self.frame2 = tk.Frame(self.toplevel1)
        self.toplevel1.title("Cadastro de Conta")
        self.entNome = tk.Entry(self.frame2)
        self.entNome.configure(justify='left')
        self.entNome.place(anchor='nw', relx='0.4', rely='0.25', width='220', x='0', y='0')
        self.label2 = tk.Label(self.frame2)
        self.label2.configure(font='{arial} 16 {}', justify='left', relief='groove', takefocus=True)
        self.label2.configure(text='Cadastro de Conta')
        self.label2.place(anchor='nw', relx='0.23', rely='0.04', width='250', x='0', y='0')
        self.entUser = tk.Entry(self.frame2)
        self.entUser.place(anchor='nw', relx='0.4', rely='0.365', width='220', x='0', y='0')
        self.entSenha = tk.Entry(self.frame2)
        self.entSenha.configure(font='{MS Outlook} 12 {}')
        self.entSenha.place(anchor='nw', relx='0.4', rely='0.48', width='220', x='0', y='0')
        self.entConSenha = tk.Entry(self.frame2)
        self.entConSenha.configure(font='{ms outlook} 12 {}', validate='none')
        self.entConSenha.place(anchor='nw', relx='0.4', rely='0.595', width='220', x='0', y='0')
        self.entRF = tk.Entry(self.frame2)
        self.entRF.place(anchor='nw', relx='0.4', rely='0.71', width='220', x='0', y='0')
        self.label3 = tk.Label(self.frame2)
        self.label3.configure(relief='groove', takefocus=False, text='Nome Completo')
        self.label3.place(anchor='nw', relx='0.12', rely='0.25', width='120', x='0', y='0')
        self.label4 = tk.Label(self.frame2)
        self.label4.configure(relief='groove', text='Usuário')
        self.label4.place(anchor='nw', relx='0.12', rely='0.365', width='120', x='0', y='0')
        self.label5 = tk.Label(self.frame2)
        self.label5.configure(relief='groove', text='Senha')
        self.label5.place(anchor='nw', relx='0.12', rely='0.48', width='120', x='0', y='0')
        self.label6 = tk.Label(self.frame2)
        self.label6.configure(relief='groove', text='Confirme a senha')
        self.label6.place(anchor='nw', relx='0.12', rely='0.595', width='120', x='0', y='0')
        self.label7 = tk.Label(self.frame2)
        self.label7.configure(relief='groove', text='RF')
        self.label7.place(anchor='nw', relx='0.12', rely='0.71', width='120', x='0', y='0')

        self.label8 = tk.Label(self.frame2)
        self.label8.configure(background='#a5d6ef', font='{arial} 12 {bold}', foreground='#ff0000', text='')
        self.label8.place(anchor='nw', relx='0.23', rely='0.16', width='250', x='0', y='0')

        
        self.btnCadastrar = tk.Button(self.frame2)
        self.btnCadastrar.configure(font='{Arial} 12 {}', text='Cadastrar')
        self.btnCadastrar.place(anchor='nw', relx='0.23', rely='0.84', width='100', x='0', y='0')
        self.btnCadastrar.configure(command=self.cadastro)
        
        self.btnSair = tk.Button(self.frame2)
        self.btnSair.configure(font='{Arial} 12 {}', text='Sair')
        self.btnSair.place(anchor='nw', relx='0.54', rely='0.84', width='100', x='0', y='0')
        self.btnSair.configure(command=self.sair)

        self.frame2.configure(background='#a5d6ef', borderwidth='5', height='400', relief='sunken')
        self.frame2.configure(width='450')
        self.frame2.place(anchor='nw', relx='0.003', rely='0.003', x='0', y='0')
        self.toplevel1.configure(background='#669bdb', borderwidth='5', height='415', relief='raised')
        self.toplevel1.configure(width='465')

        app_width =465
        app_height =415

        screen_width =self.toplevel1.winfo_screenwidth()
        screen_height=self.toplevel1.winfo_screenheight()

        x = (screen_width/2)-(app_width/2)
        y = (screen_height/2)-(app_height/2)

        self.toplevel1.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')


        # Main widget
        self.mainwindow = self.toplevel1
    

    def run(self):
        self.mainwindow.mainloop()

    def cadastro(self):
        try:
            Programa.cadastrar(self.entNome.get(),self.entUser.get(),self.entSenha.get(),self.entConSenha.get(),self.entRF.get())
            self.mainwindow.destroy()
            AvisoSucess.abre()
        except:
            self.label8.configure(text="Dados Não Correspondem!")

    def sair(self):
        self.mainwindow.destroy()
        
def abre():
    app = CadastrologinApp()
    app.run()

#abre()


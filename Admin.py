import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
import Programa,AlterarSenhaAdm,CadastrarFabri,CadastrarSetor,AttFabri

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "CadastroLogin.ui")

class CadastrologinApp:
    def __init__(self, master=None):
        # build ui
        self.toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        self.toplevel1.title("Administrador")
        self.frame2 = tk.Frame(self.toplevel1)
        self.label2 = tk.Label(self.frame2)
        self.label2.configure(font='{arial} 16 {}', justify='left', relief='groove', takefocus=True)
        self.label2.configure(text='Administrador')
        self.label2.place(anchor='nw', relx='0.23', rely='0.04', width='250', x='0', y='0')
        
        self.btnAlterarSenha = tk.Button(self.frame2)
        self.btnAlterarSenha.configure(font='{Arial} 11 {}', text='Alterar Senha Admin')
        self.btnAlterarSenha.place(anchor='nw', height='40', relx='0.05', rely='0.7', width='190', x='0', y='0')
        self.btnAlterarSenha.configure(command=AlterarSenhaAdm.abre)

        self.btnIntervalos = tk.Button(self.frame2)
        self.btnIntervalos.configure(font='{Arial} 11 {}', text='Atualizar Fabricante')
        self.btnIntervalos.place(anchor='nw', height='40', relx='0.53', rely='0.7', width='190', x='0', y='0')
        self.btnIntervalos.configure(command=AttFabri.abre)
        
        self.btnFabri = tk.Button(self.frame2)
        self.btnFabri.configure(font='{Arial} 11 {}', text='Cadastrar Fabricante')
        self.btnFabri.place(anchor='nw', height='40', relx='0.05', rely='0.34', width='190', x='0', y='0')
        self.btnFabri.configure(command=CadastrarFabri.abre)
        
        self.btnSetor = tk.Button(self.frame2)
        self.btnSetor.configure(font='{Arial} 11 {}', text='Cadastrar Setor')
        self.btnSetor.place(anchor='nw', height='40', relx='0.53', rely='0.34', width='190', x='0', y='0')
        self.btnSetor.configure(command=CadastrarSetor.abre)
        
        self.frame2.configure(background='#a5d6ef', borderwidth='5', height='200', relief='sunken')
        self.frame2.configure(width='450')
        self.frame2.place(anchor='nw', relx='0.003', rely='0.003', x='0', y='0')
        self.toplevel1.configure(background='#669bdb', borderwidth='5', height='215', relief='raised')
        self.toplevel1.configure(width='465')

        app_width =465
        app_height =215

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


def abre():
    app = CadastrologinApp()
    app.run()
#abre()

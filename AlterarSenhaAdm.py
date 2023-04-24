import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
import Programa,AvisoSucess,AvisoNSucess

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "AlterarSenhaAdmin.ui")

class AlterarsenhaadminApp:
    def __init__(self, master=None):
        # build ui
        self.toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        self.frame2 = tk.Frame(self.toplevel1)
        self.label2 = tk.Label(self.frame2)
        self.toplevel1.title("Alterar Senha do Administrador")
        self.label2.configure(font='{arial} 16 {}', justify='left', relief='groove', takefocus=True)
        self.label2.configure(text='Alterar Senha do Administrador')
        self.label2.place(anchor='nw', relx='0.17', rely='0.07', width='300', x='0', y='0')
        
        self.button2 = tk.Button(self.frame2)
        self.button2.configure(font='{Arial} 11 {}', text='Alterar Senha')
        self.button2.place(anchor='nw', height='40', relx='0.341', rely='0.7', width='150', x='0', y='0')
        self.button2.configure(command=self.insert)
        
        self.entNovaSenha = tk.Entry(self.frame2)
        _text_ = ''''''
        self.entNovaSenha.delete('0', 'end')
        self.entNovaSenha.insert('0', _text_)
        self.entNovaSenha.place(anchor='nw', relx='.39', rely='0.4', width='200', x='0', y='0')
        
        self.label1 = tk.Label(self.frame2)
        self.label1.configure(relief='groove', text='Nova Senha')
        self.label1.place(anchor='nw', relx='0.17', rely='0.4', width='90', x='0', y='0')
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

    def insert(self):
        try:
            Programa.atualizarXesque(self.entNovaSenha.get())
            self.mainwindow.destroy()
            AvisoSucess.abre()
        except:
            AvisoNSucess.abre()

def abre():
    app = AlterarsenhaadminApp()
    app.run()

#abre()

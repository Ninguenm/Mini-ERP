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
        self.toplevel1.title("Cadastrar Setor")
        self.frame2 = tk.Frame(self.toplevel1)
        self.label2 = tk.Label(self.frame2)
        self.label2.configure(font='{arial} 16 {}', justify='left', relief='groove', takefocus=True)
        self.label2.configure(text='Cadastrar Setor')
        self.label2.place(anchor='nw', relx='0.17', rely='0.07', width='300', x='0', y='0')
        
        self.btnCad = tk.Button(self.frame2)
        self.btnCad.configure(font='{Arial} 11 {}', text='Cadastrar')
        self.btnCad.place(anchor='nw', height='40', relx='0.341', rely='0.7', width='150', x='0', y='0')
        self.btnCad.configure(command=self.insert)
        
        self.lblAndar = tk.Label(self.frame2)
        self.lblAndar.configure(relief='groove', text='Andar')
        self.lblAndar.place(anchor='nw', relx='0.17', rely='0.33', width='90', x='0', y='0')
        self.label3 = tk.Label(self.frame2)
        self.label3.configure(relief='groove', text='Setor')
        self.label3.place(anchor='nw', relx='0.17', rely='0.5', width='90', x='0', y='0')

        self.combobox1 = ttk.Combobox(self.frame2)
        self.combobox1.configure(cursor='arrow',state='readonly',values=list(Programa.ListaAndares()))
        self.combobox1.place(anchor='nw', relx='0.39', rely='0.33', width='200', x='0', y='0')
        
        self.entry2 = tk.Entry(self.frame2)
        _text_ = ''''''
        self.entry2.delete('0', 'end')
        self.entry2.insert('0', _text_)
        self.entry2.place(anchor='nw', relx='0.39', rely='0.5', width='200', x='0', y='0')
        
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

    def insert(self):
        try:
            Programa.cadastrarSetor(self.combobox1.get(),self.entry2.get())
            self.mainwindow.destroy()
            AvisoSucess.abre()
        except:
            raise

def abre():
    app = AlterarsenhaadminApp()
    app.run()
#abre()

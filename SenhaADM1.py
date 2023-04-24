import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
import RecSenha,Programa

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "AdminPerm.ui")

class AdminpermApp:
    def __init__(self, master=None):
        # build ui
        self.toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        self.toplevel1.title("Permissão Admin")
        
        self.frame2 = tk.Frame(self.toplevel1)
        self.label2 = tk.Label(self.frame2)
        self.label2.configure(font='{arial} 16 {}', justify='left', relief='groove', takefocus=True)
        self.label2.configure(text='Necessário Permissão Admin')
        self.label2.place(anchor='nw', relx='0.06', rely='0.16', width='300', x='0', y='0')
        
        self.btnOK = tk.Button(self.frame2)
        self.btnOK.configure(font='{Arial} 10 {}', text='OK')
        self.btnOK.place(anchor='nw', height='20', relx='0.82', rely='0.66', width='40', x='0', y='0')
        self.btnOK.configure(command=self.OK)
        
        self.entry1 = ttk.Entry(self.frame2)
        self.entry1.configure(font='{MS Outlook} 12 {}')
        self.entry1.place(anchor='nw', relx='0.315', rely='0.66', width='170', x='0', y='0')
        self.label1 = ttk.Label(self.frame2)
        self.label1.configure(background='#a5d6ef', borderwidth='1', relief='groove', text=' Senha Admin')
        self.label1.place(anchor='nw', relx='0.06', rely='0.67', width='85', x='0', y='0')
        self.frame2.configure(background='#a5d6ef', borderwidth='5', height='120', relief='sunken')
        self.frame2.configure(width='350')
        self.frame2.place(anchor='nw', relx='0.003', rely='0.003', x='0', y='0')
        self.toplevel1.configure(background='#669bdb', borderwidth='5', height='135', relief='raised')
        self.toplevel1.configure(takefocus=True, width='365')

        app_width =365
        app_height =135

        screen_width =self.toplevel1.winfo_screenwidth()
        screen_height=self.toplevel1.winfo_screenheight()

        x = (screen_width/2)-(app_width/2)
        y = (screen_height/2)-(app_height/2)

        self.toplevel1.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')


        # Main widget
        self.mainwindow = self.toplevel1
    

    def run(self):
        self.mainwindow.mainloop()

    def OK(self):
        senha = self.entry1.get()
        if senha == Programa.ODale():
            self.mainwindow.destroy()
            RecSenha.abre()
        return senha
        

def abre():
    app = AdminpermApp()
    app.run()

#abre()


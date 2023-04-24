import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "Aviso.ui")

class AvisoApp:
    def __init__(self, master=None):
        # build ui
        self.toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        
        self.toplevel1.title("Dados Incorretos")
        self.frame2 = tk.Frame(self.toplevel1)
        self.btnOK = tk.Button(self.frame2)
        self.btnOK.configure(text='Ok')
        self.btnOK.place(anchor='nw', relx='0.40', rely='0.6', width='100', x='0', y='0')
        self.btnOK.configure(command = self.exit)
        
        self.label2 = tk.Label(self.frame2)
        self.label2.configure(font='{arial} 16 {}', foreground='#ff0000', justify='left', relief='groove')
        self.label2.configure(takefocus=True, text='Dados Incorretos!')
        self.label2.place(anchor='nw', relx='0.14', rely='0.16', width='250', x='0', y='0')
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

    def exit(self):
        self.mainwindow.destroy()

def abre():
    app = AvisoApp()
    app.run()

#abre()

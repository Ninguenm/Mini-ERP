import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
import Programa,SenhaADM,SenhaADM1,SenhaADM2,Principal,PopUpAlarme,AvisoSucess,AvisoNSucess



PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "LogIn.ui")

class LoginApp:
    def __init__(self, master=None):
        # build ui
        self.toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        self.toplevel1.title("Log In")
        self.frame2 = tk.Frame(self.toplevel1)
        self.label2 = tk.Label(self.frame2)
        self.label2.configure(font='{arial} 16 {}', justify='left', relief='groove', takefocus=True)
        self.label2.configure(text='Log in')
        self.label2.place(anchor='nw', relx='0.49', rely='0.11', width='160', x='0', y='0')
        self.entry2 = tk.Entry(self.frame2)
        self.entry2.place(anchor='nw', relx='0.4', rely='0.32', width='220', x='0', y='0')
        self.entry3 = tk.Entry(self.frame2)
        self.entry3.configure(font='{MS Outlook} 12 {}')
        self.entry3.place(anchor='nw', relx='0.4', rely='0.45', width='220', x='0', y='0')
        self.label4 = tk.Label(self.frame2)
        self.label4.configure(relief='groove', text='RF')
        self.label4.place(anchor='nw', relx='0.12', rely='0.32', width='120', x='0', y='0')
        self.label5 = tk.Label(self.frame2)
        self.label5.configure(relief='groove', text='Senha')
        self.label5.place(anchor='nw', relx='0.12', rely='0.45', width='120', x='0', y='0')
        
        self.btnEntrar = tk.Button(self.frame2)
        self.btnEntrar.configure(font='{Arial} 12 {}', text='Entrar')
        self.btnEntrar.place(anchor='nw', relx='0.405', rely='0.55', width='100', x='0', y='0')
        self.btnEntrar.configure(command=self.log)
        
        self.btnCadastrar = tk.Button(self.frame2)
        self.btnCadastrar.configure(font='{Arial} 10 {}', text='Cadastrar')
        self.btnCadastrar.place(anchor='nw', height='20', relx='0.675', rely='0.69', width='100', x='0', y='0')
        self.btnCadastrar.configure(command=self.cadastrar)
        
        self.btnSair = tk.Button(self.frame2)
        self.btnSair.configure(font='{arial} 12 {}', text='Sair')
        self.btnSair.place(anchor='nw', relx='0.675', rely='0.55', width='100', x='0', y='0')
        self.btnSair.configure(command=self.sair)

        self.btnForgotPW = tk.Button(self.frame2)
        self.btnForgotPW.configure(font='{arial} 10 {}', text='Alterar senha')
        self.btnForgotPW.place(anchor='nw', height='20', relx='0.675', rely='0.80', width='100', x='0', y='0')
        self.btnForgotPW.configure(command=self.senha)

        self.btnAdmin = tk.Button(self.frame2)
        self.btnAdmin.configure(text='Administrador')
        self.btnAdmin.place(anchor='nw', height='20', relx='0.675', rely='0.91', width='100', x='0', y='0')
        self.btnAdmin.configure(command=self.Admin)

        self.btnBck = tk.Button(self.frame2)
        self.btnBck.configure(text='BackUp')
        self.btnBck.place(anchor='nw', height='20', relx='0.4', rely='0.91', width='100', x='0', y='0')
        self.btnBck.configure(command=self.BckUp)

        self.label1 = tk.Label(self.frame2)
        self.label1.configure(background='#a5d6ef', font='{arial} 12 {}', text='Não possui conta?')
        self.label1.place(anchor='nw', relx='0.36', rely='0.68', x='0', y='0')
        self.label3 = tk.Label(self.frame2)
        self.label3.configure(background='#a5d6ef', font='{arial} 12 {bold}', foreground='#ff0000', text='')
        self.label3.place(anchor='nw', relx='0.39', rely='0.215', width='250', x='0', y='0')
        self.label6 = tk.Label(self.frame2)
        self.label6.configure(background='#a5d6ef', font='{arial} 12 {}', text='Esqueceu a senha?')
        self.label6.place(anchor='nw', relx='0.34', rely='0.795', x='0', y='0')
        
        self.label7 = tk.Label(self.frame2)
        self.cap_PNG = tk.PhotoImage(file='LogInLogo.PNG')
        self.label7.configure(background='#a5d6ef', image=self.cap_PNG)
        self.label7.place(anchor='nw', height='70', relx='0.12', rely='0.105', width='120', x='0', y='0')
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

    def cadastrar(self):
        try:
            self.mainwindow.destroy()
            SenhaADM.abre()
        except:
            pass

    def senha(self):
        try:
            self.mainwindow.destroy()
            SenhaADM1.abre()
        except:
            pass

    def BckUp(self):
        try:
            Programa.BackUP()
            AvisoSucess.abre()
        except:
            AvisoNSucess.abre()

    def Admin(self):
        try:
            self.mainwindow.destroy()
            SenhaADM2.abre()
        except:
            pass

    def sair(self):
        self.mainwindow.destroy()

    def log(self):
        try:
            Programa.login(self.entry2.get(),self.entry3.get())
            Programa.logado = Programa.login(self.entry2.get(),self.entry3.get())
            self.mainwindow.destroy()
            PopUpAlarme.abre()
            Principal.abre()
        except:
            self.label3.configure(text="Usuário ou Senha incorretos!")
            
def abre():
    app = LoginApp()
    app.run()
abre()


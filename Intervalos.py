import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
import Programa,AvisoSucess,AvisoNSucess,AvisoDesativado

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "ReentradaCertissima.ui")

class ReentradaApp:
    def __init__(self, master=None):
        # build ui
        self.toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        self.frame2 = tk.Frame(self.toplevel1)
        self.toplevel1.title("Alterar Intervalo de Calibração e Preventiva")
        self.label2 = tk.Label(self.frame2)
        self.label2.configure(font='{arial} 16 {}', justify='left', relief='groove', takefocus=False)
        self.label2.configure(text='Alterar Intervalo de Calibração e Preventiva')
        self.label2.place(anchor='nw', relx='0.015', rely='0.04', width='430', x='0', y='0')

        x = Programa.Todos()
        r1 = []
        for i in x:
            if i[2] not in r1:
                r1.append(i[2])

        self.combobox3 = ttk.Combobox(self.frame2)
        self.combobox3.configure(cursor='arrow',state="readonly",values=r1)
        self.combobox3.place(anchor='nw', relx='0.50', rely='0.16', width='170', x='0', y='0')

        self.combobox1 = ttk.Combobox(self.frame2)
        self.combobox1.configure(cursor='arrow',state='readonly',values=Programa.TodosDale(self.combobox3.bind("<<ComboboxSelected>>",self.getSelected)))
        self.combobox1.place(anchor='nw', relx='0.50', rely='0.26', width='170', x='0', y='0')
############
        
        self.entData = tk.Entry(self.frame2)
        self.entData.place(anchor='nw', relx='0.50', rely='0.36', width='170', x='0', y='0')

        self.entCalibrAntigo = tk.Entry(self.frame2)
        self.entCalibrAntigo.place(anchor='nw', relx='0.50', rely='0.46', width='170', x='0', y='0')
        self.entCalibrNovo = tk.Entry(self.frame2)
        self.entCalibrNovo.place(anchor='nw', relx='0.50', rely='0.56', width='170', x='0', y='0')

        self.entPrevAntigo = tk.Entry(self.frame2)
        self.entPrevAntigo.place(anchor='nw', relx='0.50', rely='0.66', width='170', x='0', y='0')
        self.entPrevNovo = tk.Entry(self.frame2)
        self.entPrevNovo.place(anchor='nw', relx='0.50', rely='0.76', width='170', x='0', y='0')

        
        self.lblNomeTec = tk.Label(self.frame2)
        self.lblNomeTec.configure(relief='groove', takefocus=False, text='*Nome Técnico')
        self.lblNomeTec.place(anchor='nw', relx='0.1', rely='0.16', width='170', x='0', y='0')
        self.lblModelo = tk.Label(self.frame2)
        self.lblModelo.configure(relief='groove', text='*Modelo')
        self.lblModelo.place(anchor='nw', relx='0.1', rely='0.26', width='170', x='0', y='0')
        self.lblData = tk.Label(self.frame2)
        self.lblData.configure(relief='groove', text='*Data')
        self.lblData.place(anchor='nw', relx='0.1', rely='0.36', width='170', x='0', y='0')
        self.lblCalibrAntigo = tk.Label(self.frame2)
        self.lblCalibrAntigo.configure(relief='groove', text='Intervalo de Calibração Antigo')
        self.lblCalibrAntigo.place(anchor='nw', relx='0.1', rely='0.46', width='170', x='0', y='0')
        self.lblCalibrNovo = tk.Label(self.frame2)
        self.lblCalibrNovo.configure(relief='groove', text='*Intervalo de Calibração Novo')
        self.lblCalibrNovo.place(anchor='nw', relx='0.1', rely='0.56', width='170', x='0', y='0')
        self.lblPrevAntigo = tk.Label(self.frame2)
        self.lblPrevAntigo.configure(relief='groove', text='Intervalo de Preventiva Antigo')
        self.lblPrevAntigo.place(anchor='nw', relx='0.1', rely='0.66', width='170', x='0', y='0')
        self.lblPrevNovo = tk.Label(self.frame2)
        self.lblPrevNovo.configure(relief='groove', text='*Intervalo de Preventiva Antigo')
        self.lblPrevNovo.place(anchor='nw', relx='0.1', rely='0.76', width='170', x='0', y='0')

        self.label3 = tk.Label(self.frame2)
        self.label3.configure(background='#a5d6ef', font='{Arial} 12 {bold}', foreground='#ff171d', text='* Campos Obrigatórios')
        self.label3.place(anchor='nw', relx='0.60', rely='0.95', x='0', y='0')
        
        self.btnCadastrar = tk.Button(self.frame2)
        self.btnCadastrar.configure(font='{Arial} 12 {}', text='Cadastrar')
        self.btnCadastrar.place(anchor='nw', relx='0.25', rely='0.86', width='100', x='0', y='0')
        self.btnCadastrar.configure(command=self.insert)
        
        self.btnSair = tk.Button(self.frame2)
        self.btnSair.configure(font='{Arial} 12 {}', text='Sair')
        self.btnSair.place(anchor='nw', relx='0.55', rely='0.86', width='100', x='0', y='0')
        self.btnSair.configure(command=self.fecha)
        
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

    def getSelected(self, event):
        self.combobox1['values']=Programa.TodosDale(self.combobox3.get())
        self.combobox1.set('')

    def fecha(self):
        self.mainwindow.destroy()

    def insert(self):
        try:
            Programa.cadastrarTempCalibrPrev(self.combobox3.get(),self.combobox1.get(),self.entData.get(),self.entCalibrAntigo.get(),self.entCalibrNovo.get(),self.entPrevAntigo.get(),self.entPrevNovo.get())
            self.mainwindow.destroy()
            AvisoSucess.abre()
        except:
            AvisoNSucess.abre()


def abre():
    app = ReentradaApp()
    app.run()

#abre()

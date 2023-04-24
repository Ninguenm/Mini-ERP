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
        self.toplevel1.title("Retorno de Equipamento")
        self.frame2 = tk.Frame(self.toplevel1)
        self.label2 = tk.Label(self.frame2)
        self.label2.configure(font='{arial} 16 {}', justify='left', relief='groove', takefocus=False)
        self.label2.configure(text='Retorno de Equipamento')
        self.label2.place(anchor='nw', relx='0.14', rely='0.04', width='320', x='0', y='0')
        self.entPatri = tk.Entry(self.frame2)
        self.entPatri.configure(justify='left')
        self.entPatri.place(anchor='nw', relx='0.32', rely='0.16', width='170', x='0', y='0')

        self.combobox4 = ttk.Combobox(self.frame2)
        self.combobox4.place(anchor='nw', relx='.32', rely='.24', width='170', x='0', y='0')
        self.combobox4.configure(cursor='arrow',values=['Digite o N° Série','Ilegível'])
        
        self.entData_reentrada = tk.Entry(self.frame2)
        self.entData_reentrada.place(anchor='nw', relx='0.32', rely='0.32', width='170', x='0', y='0')

        self.combobox1 = ttk.Combobox(self.frame2)
        self.combobox1.configure(cursor='arrow',values=['Calibração','Preventiva','Esporádica','Outro: Digite'])
        self.combobox1.place(anchor='nw', relx='0.32', rely='0.40', width='170', x='0', y='0')

        self.combobox5 = ttk.Combobox(self.frame2)
        self.combobox5.place(anchor='nw', relx='.32', rely='0.56', width='170', x='0', y='0')
        self.combobox5.configure(cursor='arrow',values=list(Programa.ListaAndares()))

        self.combobox6 = ttk.Combobox(self.frame2)
        self.combobox6.place(anchor='nw', relx='.32', rely='0.64', width='170', x='0', y='0')
        self.combobox6.configure(cursor='arrow',values=Programa.ListaSetores(self.combobox5.bind("<<ComboboxSelected>>",self.getSelected)))

        self.entLocal = tk.Entry(self.frame2)
        self.entLocal.configure(justify='left')
        self.entLocal.place(anchor='nw', relx='0.32', rely='0.72', width='170', x='0', y='0')
        
        self.entPcsTrocadas = tk.Entry(self.frame2)
        self.entPcsTrocadas.place(anchor='nw', relx='0.32', rely='0.48', width='170', x='0', y='0')
        self.entResponsavel = tk.Entry(self.frame2)
        self.entResponsavel.place(anchor='nw', relx='0.32', rely='0.80', width='170', x='0', y='0')
        self.entObs = tk.Entry(self.frame2)
        self.entObs.place(anchor='nw', relx='0.32', rely='0.88', width='170', x='0', y='0')
        
        self.lblPatri = tk.Label(self.frame2)
        self.lblPatri.configure(relief='groove', takefocus=False, text='*Patrimônio')
        self.lblPatri.place(anchor='nw', relx='0.037', rely='0.16', width='120', x='0', y='0')
        self.lblNumSerie = tk.Label(self.frame2)
        self.lblNumSerie.configure(relief='groove', text='*Número de Série')
        self.lblNumSerie.place(anchor='nw', relx='0.037', rely='0.24', width='120', x='0', y='0')
        self.lblData_reentrada = tk.Label(self.frame2)
        self.lblData_reentrada.configure(relief='groove', text='*Data do Retorno')
        self.lblData_reentrada.place(anchor='nw', relx='0.037', rely='0.32', width='120', x='0', y='0')
        self.lblMotivo = tk.Label(self.frame2)
        self.lblMotivo.configure(relief='groove', text='*Motivo')
        self.lblMotivo.place(anchor='nw', relx='0.037', rely='0.40', width='120', x='0', y='0')
        self.lblPcsTrocadas = tk.Label(self.frame2)
        self.lblPcsTrocadas.configure(relief='groove', text='Peças Trocadas')
        self.lblPcsTrocadas.place(anchor='nw', relx='0.037', rely='0.48', width='120', x='0', y='0')

        self.lblAndar_Dest = tk.Label(self.frame2)
        self.lblAndar_Dest.configure(relief='groove', text='*Andar de Destino')
        self.lblAndar_Dest.place(anchor='nw', relx='0.037', rely='0.56', width='120', x='0', y='0')
        self.lblSetor_Dest = tk.Label(self.frame2)
        self.lblSetor_Dest.configure(relief='groove', text='*Setor de Destino')
        self.lblSetor_Dest.place(anchor='nw', relx='0.037', rely='0.64', width='120', x='0', y='0')
        self.lblLocal_Dest = tk.Label(self.frame2)
        self.lblLocal_Dest.configure(relief='groove', text='Local de Destino')
        self.lblLocal_Dest.place(anchor='nw', relx='0.037', rely='0.72', width='120', x='0', y='0')
        
        self.lblResponsavel = tk.Label(self.frame2)
        self.lblResponsavel.configure(relief='groove', text='*Responsavel')
        self.lblResponsavel.place(anchor='nw', relx='0.037', rely='0.80', width='120', x='0', y='0')
        self.lblObs = tk.Label(self.frame2)
        self.lblObs.configure(relief='groove', text='Observação')
        self.lblObs.place(anchor='nw', relx='0.037', rely='0.88', width='120', x='0', y='0')

        self.label3 = tk.Label(self.frame2)
        self.label3.configure(background='#a5d6ef', font='{Arial} 12 {bold}', foreground='#ff171d', text='* Campos Obrigatórios')
        self.label3.place(anchor='nw', relx='0.60', rely='0.95', x='0', y='0')
        
        self.btnCadastrar = tk.Button(self.frame2)
        self.btnCadastrar.configure(font='{Arial} 12 {}', text='Cadastrar')
        self.btnCadastrar.place(anchor='nw', relx='0.76', rely='0.42', width='100', x='0', y='0')
        self.btnCadastrar.configure(command=self.insert)
        
        self.btnSair = tk.Button(self.frame2)
        self.btnSair.configure(font='{Arial} 12 {}', text='Sair')
        self.btnSair.place(anchor='nw', relx='0.76', rely='0.61', width='100', x='0', y='0')
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

    def fecha(self):
        self.mainwindow.destroy()

    def getSelected(self, event):
        self.combobox6['values']=Programa.ListaSetores(self.combobox5.get())
        self.combobox6.set('')

    def insert(self):
        try:
            Programa.cadastrarReentrada(self.entPatri.get(),self.combobox4.get(),self.entData_reentrada.get(),self.combobox1.get(),self.entPcsTrocadas.get(),self.combobox5.get(),self.combobox6.get(),self.entLocal.get(),self.entResponsavel.get(),self.entObs.get())
            self.mainwindow.destroy()
            AvisoSucess.abre()
        except TypeError:
            AvisoDesativado.abre()
        except:
            raise


def abre():
    app = ReentradaApp()
    app.run()

#abre()

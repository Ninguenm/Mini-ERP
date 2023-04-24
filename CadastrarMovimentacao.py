import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
import Programa,AvisoSucess,AvisoNSucess,AvisoDesativado

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "MovimentacaoCertissima.ui")

class MovimentacaocertissimaApp:
    def __init__(self, master=None):
        # build ui
        # build ui
        self.toplevel1 = tk.Toplevel()
        self.frame2 = tk.Frame(self.toplevel1)
        self.toplevel1.title("Cadastro de Movimentação")
        
        self.label2 = tk.Label(self.frame2)
        self.label2.configure(font='{arial} 16 {}', justify='left', relief='groove', takefocus=False)
        self.label2.configure(text='Cadastro de Movimentação')
        self.label2.place(anchor='nw', relx='0.18', rely='0.04', width='300', x='0', y='0')
        
        self.entPatri = tk.Entry(self.frame2)
        self.entPatri.configure(justify='left')
        self.entPatri.place(anchor='nw', relx='0.32', rely='0.14', width='170', x='0', y='0')

        self.combobox4 = ttk.Combobox(self.frame2)
        self.combobox4.place(anchor='nw', relx='.32', rely='.21', width='170', x='0', y='0')
        self.combobox4.configure(cursor='arrow',values=['Digite o N° Série','Ilegível'])
        
        self.entData = tk.Entry(self.frame2)
        self.entData.place(anchor='nw', relx='0.32', rely='0.28', width='170', x='0', y='0')

        y = ''
        z = ''
        h = ''

        self.btnOK = tk.Button(self.frame2)
        self.btnOK.configure(font='{Arial} 6 {}', text='OK')
        self.btnOK.place(anchor='nw', relx='0.71', rely='0.14', width='20',height='20', x='0', y='0')
        self.btnOK.configure(command=self.OK)


        self.lblAndares = tk.Label(self.frame2)
        self.lblAndares.configure(relief='groove', takefocus=False, text=y)
        self.lblAndares.place(anchor='nw', relx='0.32', rely='0.35', width='170', x='0', y='0')

        self.lblSetores = tk.Label(self.frame2)
        self.lblSetores.configure(relief='groove', takefocus=False, text=z)
        self.lblSetores.place(anchor='nw', relx='0.32', rely='0.42', width='170', x='0', y='0')

        self.lblLocais = tk.Label(self.frame2)
        self.lblLocais.configure(relief='groove', takefocus=False, text=h)
        self.lblLocais.place(anchor='nw', relx='0.32', rely='0.49', width='170', x='0', y='0')
        
        self.combobox21 = ttk.Combobox(self.frame2)
        self.combobox21.place(anchor='nw', relx='.32', rely='.56', width='170', x='0', y='0')
        self.combobox21.configure(cursor='arrow',state='readonly',values=list(Programa.ListaAndares()))
        
        self.combobox11 = ttk.Combobox(self.frame2)
        self.combobox11.place(anchor='nw', relx='0.32', rely='.63', width='170', x='0', y='0')
        self.combobox11.configure(cursor='arrow',state='readonly',values=Programa.ListaSetores(self.combobox21.bind("<<ComboboxSelected>>",self.getSelected1)))
        
        self.entLocal_Dest = tk.Entry(self.frame2)
        self.entLocal_Dest.place(anchor='nw', relx='0.32', rely='0.70', width='170', x='0', y='0')

        self.entAcessorio = tk.Entry(self.frame2)
        self.entAcessorio.place(anchor='nw', relx='0.32', rely='0.77', width='170', x='0', y='0')
        self.entOrdem_Serv = tk.Entry(self.frame2)
        self.entOrdem_Serv.place(anchor='nw', relx='0.32', rely='0.84', width='170', x='0', y='0')
        self.entObs = tk.Entry(self.frame2)
        self.entObs.place(anchor='nw', relx='0.32', rely='0.91', width='170', x='0', y='0')
        
        self.lblPatri = tk.Label(self.frame2)
        self.lblPatri.configure(relief='groove', takefocus=False, text='*Patrimônio')
        self.lblPatri.place(anchor='nw', relx='0.037', rely='0.14', width='120', x='0', y='0')
        self.lblNumSerie = tk.Label(self.frame2)
        self.lblNumSerie.configure(relief='groove', text='*Número de Série')
        self.lblNumSerie.place(anchor='nw', relx='0.037', rely='0.21', width='120', x='0', y='0')
        self.lblData = tk.Label(self.frame2)
        self.lblData.configure(relief='groove', text='*Data')
        self.lblData.place(anchor='nw', relx='0.037', rely='0.28', width='120', x='0', y='0')
        self.lblAndar_Orig = tk.Label(self.frame2)
        self.lblAndar_Orig.configure(relief='groove', text='*Andar de Origem')
        self.lblAndar_Orig.place(anchor='nw', relx='0.037', rely='0.35', width='120', x='0', y='0')
        self.lblSetor_Orig = tk.Label(self.frame2)
        self.lblSetor_Orig.configure(relief='groove', text='*Setor de Origem')
        self.lblSetor_Orig.place(anchor='nw', relx='0.037', rely='0.42', width='120', x='0', y='0')
        self.lblLocal_Orig = tk.Label(self.frame2)
        self.lblLocal_Orig.configure(relief='groove', text='Local de Origem')
        self.lblLocal_Orig.place(anchor='nw', relx='0.037', rely='0.49', width='120', x='0', y='0')
        self.lblAndar_Dest = tk.Label(self.frame2)
        self.lblAndar_Dest.configure(relief='groove', text='*Andar de Destino')
        self.lblAndar_Dest.place(anchor='nw', relx='0.037', rely='0.56', width='120', x='0', y='0')
        self.lblSetor_Dest = tk.Label(self.frame2)
        self.lblSetor_Dest.configure(relief='groove', text='*Setor de Destino')
        self.lblSetor_Dest.place(anchor='nw', relx='0.037', rely='0.63', width='120', x='0', y='0')
        self.lblLocal_Dest = tk.Label(self.frame2)
        self.lblLocal_Dest.configure(relief='groove', text='Local de Destino')
        self.lblLocal_Dest.place(anchor='nw', relx='0.037', rely='0.70', width='120', x='0', y='0')
        self.lblAcessorio = tk.Label(self.frame2)
        self.lblAcessorio.configure(relief='groove', text='Acessórios')
        self.lblAcessorio.place(anchor='nw', relx='0.037', rely='0.77', width='120', x='0', y='0')
        self.lblOrdem_Serv = tk.Label(self.frame2)
        self.lblOrdem_Serv.configure(relief='groove', text='*Ordem de Serviço')
        self.lblOrdem_Serv.place(anchor='nw', relx='0.037', rely='0.84', width='120', x='0', y='0')
        self.lblObs = tk.Label(self.frame2)
        self.lblObs.configure(relief='groove', text='Observação')
        self.lblObs.place(anchor='nw', relx='0.037', rely='0.91', width='120', x='0', y='0')

        self.label3 = tk.Label(self.frame2)
        self.label3.configure(background='#a5d6ef', font='{Arial} 12 {bold}', foreground='#ff171d', text='* Campos Obrigatórios')
        self.label3.place(anchor='nw', relx='0.60', rely='0.95', x='0', y='0')
        
        self.btnCad = tk.Button(self.frame2)
        self.btnCad.configure(font='{Arial} 12 {}', text='Cadastrar')
        self.btnCad.place(anchor='nw', relx='0.75', rely='0.42', width='100', x='0', y='0')
        self.btnCad.configure(command=self.insert)
        
        self.btnSair = tk.Button(self.frame2)
        self.btnSair.configure(font='{Arial} 12 {}', text='Sair')
        self.btnSair.place(anchor='nw', relx='0.75', rely='0.61', width='100', x='0', y='0')
        self.btnSair.configure(command=self.fecha)
        
        self.frame2.configure(background='#a5d6ef', borderwidth='5', height='600', relief='sunken')
        self.frame2.configure(width='450')
        self.frame2.place(anchor='nw', relx='0.003', rely='0.003', x='0', y='0')
        self.toplevel1.configure(background='#669bdb', borderwidth='5', height='615', relief='raised')
        self.toplevel1.configure(width='465')

        app_width = 465
        app_height = 615

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

    def OK(self):
        X = Programa.procisso(self.combobox4.get(),self.entPatri.get())
        self.lblAndares.configure(text=X[0][0])
        self.lblSetores.configure(text=X[0][1])
        self.lblLocais.configure(text=X[0][2])

    def getSelected(self, event):
        self.combobox1['values']=Programa.ListaSetores(self.combobox2.get())
        self.combobox1.set('')

    def getSelected1(self, event):
        self.combobox11['values']=Programa.ListaSetores(self.combobox21.get())
        self.combobox11.set('')

    def insert(self):
        try:
            Programa.cadastrarMovimentacao(self.entPatri.get(),self.combobox4.get(),self.entData.get(),self.combobox21.get(),self.combobox11.get(),self.entLocal_Dest.get(),self.entAcessorio.get(),self.entOrdem_Serv.get(),self.entObs.get())
            self.mainwindow.destroy()
            AvisoSucess.abre()
        except TypeError:
            AvisoDesativado.abre()
        except:
            AvisoNSucess.abre()


def abre():
    app = MovimentacaocertissimaApp()
    app.run()
#abre()

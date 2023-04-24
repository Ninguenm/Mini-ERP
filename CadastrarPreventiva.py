import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
import Programa,AvisoSucess,AvisoNSucess,AvisoDesativado

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "CadastroCalibracao.ui")

class CadastrocalibracaoApp:
    def __init__(self, master=None):
        # build ui
        self.toplevel1 = tk.Toplevel()
        self.frame2 = tk.Frame(self.toplevel1)
        self.toplevel1.title("Cadastro de Manutenção Preventiva")
        
        self.label2 = tk.Label(self.frame2)
        self.label2.configure(font='{arial} 16 {}', justify='left', relief='groove', takefocus=False)
        self.label2.configure(text='Cadastro de Manutenção Preventiva')
        self.label2.place(anchor='nw', relx='0.11', rely='0.04', width='350', x='0', y='0')
        
        self.entPatri = tk.Entry(self.frame2)
        self.entPatri.configure(justify='left')
        self.entPatri.place(anchor='nw', relx='0.32', rely='0.14', width='170', x='0', y='0')
        
        self.combobox4 = ttk.Combobox(self.frame2)
        self.combobox4.place(anchor='nw', relx='.32', rely='.21', width='170', x='0', y='0')
        self.combobox4.configure(cursor='arrow',values=['Digite o N° Série','Ilegível'])
        
        self.entData_ret = tk.Entry(self.frame2)
        self.entData_ret.place(anchor='nw', relx='0.32', rely='0.28', width='170', x='0', y='0')
        self.entAcessorio_ret = tk.Entry(self.frame2)
        self.entAcessorio_ret.place(anchor='nw', relx='0.32', rely='0.35', width='170', x='0', y='0')
        
        self.combobox2 = ttk.Combobox(self.frame2)
        self.combobox2.place(anchor='nw', relx='.32', rely='.42', width='170', x='0', y='0')
        self.combobox2.configure(cursor='arrow',state='readonly',values=list(Programa.ListaAndares()))
        
        self.combobox1 = ttk.Combobox(self.frame2)
        self.combobox1.place(anchor='nw', relx='.32', rely='.49', width='170', x='0', y='0')
        self.combobox1.configure(cursor='arrow',state='readonly',values=Programa.ListaSetores(self.combobox2.bind("<<ComboboxSelected>>",self.getSelected)))
        
        self.entLocal_ret = tk.Entry(self.frame2)
        self.entLocal_ret.place(anchor='nw', relx='0.32', rely='0.56', width='170', x='0', y='0')
        self.entEmpresa = tk.Entry(self.frame2)
        self.entEmpresa.place(anchor='nw', relx='.32', rely='.63', width='170', x='0', y='0')
        self.entTecnico = tk.Entry(self.frame2)
        self.entTecnico.place(anchor='nw', relx='0.32', rely='0.70', width='170', x='0', y='0')
        self.entOrdem_Serv = tk.Entry(self.frame2)
        self.entOrdem_Serv.place(anchor='nw', relx='0.32', rely='0.77', width='170', x='0', y='0')
        self.entEnferm_Resp = tk.Entry(self.frame2)
        self.entEnferm_Resp.place(anchor='nw', relx='0.32', rely='0.84', width='170', x='0', y='0')
        self.entObs = tk.Entry(self.frame2)
        self.entObs.place(anchor='nw', relx='0.32', rely='0.91', width='170', x='0', y='0')
        
        self.lblPatrii = tk.Label(self.frame2)
        self.lblPatrii.configure(relief='groove', takefocus=False, text='*Patrimônio')
        self.lblPatrii.place(anchor='nw', relx='0.037', rely='0.14', width='120', x='0', y='0')
        self.lblNumSerie = tk.Label(self.frame2)
        self.lblNumSerie.configure(relief='groove', text='*Número de Série')
        self.lblNumSerie.place(anchor='nw', relx='0.037', rely='0.21', width='120', x='0', y='0')
        self.lblData_ret = tk.Label(self.frame2)
        self.lblData_ret.configure(relief='groove', text='*Data da Retirada')
        self.lblData_ret.place(anchor='nw', relx='0.037', rely='0.28', width='120', x='0', y='0')
        self.lblAcessorio_ret = tk.Label(self.frame2)
        self.lblAcessorio_ret.configure(relief='groove', text='Acessórios Retirados')
        self.lblAcessorio_ret.place(anchor='nw', relx='0.037', rely='0.35', width='120', x='0', y='0')
        self.lblAndar_ret = tk.Label(self.frame2)
        self.lblAndar_ret.configure(relief='groove', text='*Andar Retirado')
        self.lblAndar_ret.place(anchor='nw', relx='0.037', rely='0.42', width='120', x='0', y='0')
        self.lblSetor_ret = tk.Label(self.frame2)
        self.lblSetor_ret.configure(relief='groove', text='*Setor Retirado')
        self.lblSetor_ret.place(anchor='nw', relx='0.037', rely='0.49', width='120', x='0', y='0')
        self.lblLocal_ret = tk.Label(self.frame2)
        self.lblLocal_ret.configure(relief='groove', text='Local Retirado')
        self.lblLocal_ret.place(anchor='nw', relx='0.037', rely='0.56', width='120', x='0', y='0')
        self.lblEmpresa = tk.Label(self.frame2)
        self.lblEmpresa.configure(relief='groove', text='*Empresa Responsável')
        self.lblEmpresa.place(anchor='nw', relx='0.037', rely='0.63', width='120', x='0', y='0')
        self.lblTecnico = tk.Label(self.frame2)
        self.lblTecnico.configure(relief='groove', text='*Técnico')
        self.lblTecnico.place(anchor='nw', relx='0.037', rely='0.70', width='120', x='0', y='0')
        self.lblOrdem_Serv = tk.Label(self.frame2)
        self.lblOrdem_Serv.configure(relief='groove', text='*Ordem de Serviço')
        self.lblOrdem_Serv.place(anchor='nw', relx='0.037', rely='0.77', width='120', x='0', y='0')
        self.lblEnferm_Resp = tk.Label(self.frame2)
        self.lblEnferm_Resp.configure(relief='groove', text='*Enfermeira Resp.')
        self.lblEnferm_Resp.place(anchor='nw', relx='0.037', rely='0.84', width='120', x='0', y='0')
        
        self.btnCad = tk.Button(self.frame2)
        self.btnCad.configure(font='{Arial} 12 {}', text='Cadastrar')
        self.btnCad.place(anchor='nw', relx='0.75', rely='0.42', width='100', x='0', y='0')
        self.btnCad.configure(command=self.insert)
        
        self.btnSair = tk.Button(self.frame2)
        self.btnSair.configure(font='{Arial} 12 {}', text='Sair')
        self.btnSair.place(anchor='nw', relx='0.75', rely='0.61', width='100', x='0', y='0')
        self.btnSair.configure(command=self.fecha)
        
        self.lblObs = tk.Label(self.frame2)
        self.lblObs.configure(relief='groove', text='Observação')
        self.lblObs.place(anchor='nw', relx='0.037', rely='0.91', width='120', x='0', y='0')

        self.label3 = tk.Label(self.frame2)
        self.label3.configure(background='#a5d6ef', font='{Arial} 12 {bold}', foreground='#ff171d', text='* Campos Obrigatórios')
        self.label3.place(anchor='nw', relx='0.60', rely='0.95', x='0', y='0')
                
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
        self.combobox1['values']=Programa.ListaSetores(self.combobox2.get())
        self.combobox1.set('')
        
    def insert(self):
        try:
            Programa.cadastrarPreventiva(self.entPatri.get(),self.combobox4.get(),self.entData_ret.get(),self.entAcessorio_ret.get(),self.combobox2.get(),self.combobox1.get(),self.entLocal_ret.get(),self.entEmpresa.get(),self.entTecnico.get(),self.entOrdem_Serv.get(),self.entEnferm_Resp.get(),self.entObs.get())
            self.mainwindow.destroy()
            AvisoSucess.abre()
        except TypeError:
            AvisoDesativado.abre()
        except:
            AvisoNSucess.abre()


def abre():
    app = CadastrocalibracaoApp()
    app.run()

#abre()


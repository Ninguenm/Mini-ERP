import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
import Programa,AvisoSucess,AvisoNSucess

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "CadastrarEquipDes.ui")

class CadastrarequipdesApp:
    def __init__(self, master=None):
        # build ui
        self.toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        self.frame2 = tk.Frame(self.toplevel1)
        self.toplevel1.title("Cadastro de equipamento em desenvolvimento")
        
        self.label2 = tk.Label(self.frame2)
        self.label2.configure(font='{arial} 16 {}', justify='left', relief='groove', takefocus=False)
        self.label2.configure(text='Cadastro de equipamento em desenvolvimento')
        self.label2.place(anchor='nw', relx='0.0', rely='0.02', width='442', x='0', y='0')
        
        self.entNomeTec = tk.Entry(self.frame2)
        self.entNomeTec.configure(justify='left')
        self.entNomeTec.place(anchor='nw', relx='0.32', rely='0.119', width='170', x='0', y='0')
        self.entModelo = tk.Entry(self.frame2)
        self.entModelo.place(anchor='nw', relx='0.32', rely='0.179', width='170', x='0', y='0')
        self.entDesenv = tk.Entry(self.frame2)
        self.entDesenv.place(anchor='nw', relx='0.32', rely='0.239', width='170', x='0', y='0')
        self.entNumReg = tk.Entry(self.frame2)
        self.entNumReg.place(anchor='nw', relx='0.32', rely='0.299', width='170', x='0', y='0')
        self.entAcessorios = tk.Entry(self.frame2)
        self.entAcessorios.place(anchor='nw', relx='0.32', rely='0.359', width='170', x='0', y='0')
        self.entInsumos = tk.Entry(self.frame2)
        self.entInsumos.place(anchor='nw', relx='0.32', rely='0.419', width='170', x='0', y='0')
        self.entData_Ent = tk.Entry(self.frame2)
        self.entData_Ent.place(anchor='nw', relx='0.32', rely='0.479', width='170', x='0', y='0')

        self.combobox2 = ttk.Combobox(self.frame2)
        self.combobox2.place(anchor='nw', relx='0.32', rely='0.539', width='170', x='0', y='0')
        self.combobox2.configure(cursor='arrow',state='readonly',values=list(Programa.ListaAndares()))
        
        self.combobox1 = ttk.Combobox(self.frame2)
        self.combobox1.place(anchor='nw', relx='0.32', rely='0.599', width='170', x='0', y='0')
        self.combobox1.configure(cursor='arrow',state='readonly',values=Programa.ListaSetores(self.combobox2.bind("<<ComboboxSelected>>",self.getSelected)))
        
        self.entLocal_Inst = tk.Entry(self.frame2)
        self.entLocal_Inst.place(anchor='nw', relx='0.32', rely='0.659', width='170', x='0', y='0')
        
        self.combobox3 = ttk.Combobox(self.frame2)
        self.combobox3.place(anchor='nw', relx='0.32', rely='0.719', width='170', x='0', y='0')
        self.combobox3.configure(cursor='arrow',values=('Sim','Não'))
        
        self.entResponsavel = tk.Entry(self.frame2)
        self.entResponsavel.place(anchor='nw', relx='0.32', rely='0.779', width='170', x='0', y='0')
        self.entObs = tk.Entry(self.frame2)
        self.entObs.place(anchor='nw', relx='0.32', rely='0.839', width='170', x='0', y='0')
        
        self.lblNomeTec = tk.Label(self.frame2)
        self.lblNomeTec.configure(relief='groove', takefocus=False, text='*Nome Técnico')
        self.lblNomeTec.place(anchor='nw', relx='0.037', rely='0.119', width='120', x='0', y='0')
        self.lblModelo = tk.Label(self.frame2)
        self.lblModelo.configure(relief='groove', text='*Modelo')
        self.lblModelo.place(anchor='nw', relx='0.037', rely='0.179', width='120', x='0', y='0')
        self.lblDesenv = tk.Label(self.frame2)
        self.lblDesenv.configure(relief='groove', text='*Desenvolvedor')
        self.lblDesenv.place(anchor='nw', relx='0.037', rely='0.239', width='120', x='0', y='0')
        self.lblNumReg = tk.Label(self.frame2)
        self.lblNumReg.configure(relief='groove', text='*Número de Registro')
        self.lblNumReg.place(anchor='nw', relx='0.037', rely='0.299', width='120', x='0', y='0')
        self.lblAcessorios = tk.Label(self.frame2)
        self.lblAcessorios.configure(relief='groove', text='Acessórios')
        self.lblAcessorios.place(anchor='nw', relx='0.037', rely='0.359', width='120', x='0', y='0')
        self.lblInsumos = tk.Label(self.frame2)
        self.lblInsumos.configure(relief='groove', text='Insumos')
        self.lblInsumos.place(anchor='nw', relx='0.037', rely='0.419', width='120', x='0', y='0')
        self.lblData_Ent = tk.Label(self.frame2)
        self.lblData_Ent.configure(relief='groove', text='*Data de Entrada')
        self.lblData_Ent.place(anchor='nw', relx='0.037', rely='0.479', width='120', x='0', y='0')
        self.lblAndar_Inst = tk.Label(self.frame2)
        self.lblAndar_Inst.configure(relief='groove', text='*Andar Instalado')
        self.lblAndar_Inst.place(anchor='nw', relx='0.037', rely='0.539', width='120', x='0', y='0')
        self.lblSetor_Inst = tk.Label(self.frame2)
        self.lblSetor_Inst.configure(relief='groove', text='*Setor Instalado')
        self.lblSetor_Inst.place(anchor='nw', relx='0.037', rely='0.599', width='120', x='0', y='0')
        self.lblLocal_Inst = tk.Label(self.frame2)
        self.lblLocal_Inst.configure(relief='groove', text='Local Instalado')
        self.lblLocal_Inst.place(anchor='nw', relx='0.037', rely='0.659', width='120', x='0', y='0')
        self.lblTreinamento = tk.Label(self.frame2)
        self.lblTreinamento.configure(relief='groove', text='Treinamento')
        self.lblTreinamento.place(anchor='nw', relx='0.037', rely='0.719', width='120', x='0', y='0')
        
        self.btnCad = tk.Button(self.frame2)
        self.btnCad.configure(font='{Arial} 12 {}', text='Cadastrar')
        self.btnCad.place(anchor='nw', relx='0.75', rely='0.42', width='100', x='0', y='0')
        self.btnCad.configure(command=self.insert)
        
        self.btnSair = tk.Button(self.frame2)
        self.btnSair.configure(font='{Arial} 12 {}', text='Sair')
        self.btnSair.place(anchor='nw', relx='0.75', rely='0.61', width='100', x='0', y='0')
        self.btnSair.configure(command=self.fecha)
        
        self.lblResponsavel = tk.Label(self.frame2)
        self.lblResponsavel.configure(relief='groove', text='*Responsável')
        self.lblResponsavel.place(anchor='nw', relx='0.037', rely='0.779', width='120', x='0', y='0')
        self.lblObs = tk.Label(self.frame2)
        self.lblObs.configure(relief='groove', text='Observação')
        self.lblObs.place(anchor='nw', relx='0.037', rely='0.839', width='120', x='0', y='0')

        self.label3 = tk.Label(self.frame2)
        self.label3.configure(background='#a5d6ef', font='{Arial} 12 {bold}', foreground='#ff171d', text='* Campos Obrigatórios')
        self.label3.place(anchor='nw', relx='0.60', rely='0.90', x='0', y='0')
        
        self.frame2.configure(background='#a5d6ef', borderwidth='5', height='635', relief='sunken')
        self.frame2.configure(width='450')
        self.frame2.place(anchor='nw', relx='0.003', rely='0.003', x='0', y='0')
        self.toplevel1.configure(background='#669bdb', borderwidth='5', height='650', relief='raised')
        self.toplevel1.configure(width='465')

        app_width =465
        app_height =650

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
            Programa.cadastrarEquipDes(self.entNomeTec.get(),self.entModelo.get(),self.entDesenv.get(),self.entNumReg.get(),self.entAcessorios.get(),self.entInsumos.get(),self.entData_Ent.get(),self.combobox2.get(),self.combobox1.get(),self.entLocal_Inst.get(),self.combobox3.get(),self.entResponsavel.get(),self.entObs.get())
            self.mainwindow.destroy()
            AvisoSucess.abre()
        except:
            AvisoNSucess.abre()


def abre():
    app = CadastrarequipdesApp()
    app.run()

#abre()


import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
import Programa
import CadastroEquip,ExibirTreinados,CadastroEquipDes,CadastrarDesativacao,CadastrarEsporadica,CadastrarMovimentacao,CadastrarPreventiva,CadastrarReentrada,CadastroCalibr,JanelaProc,PopUpAlarme,Exibição,Alarmes,CadastrarTreinados,Desativar,ExibirDesativados
import AvisoSucess

#PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
#PROJECT_UI = os.path.join(PROJECT_PATH, "inicial.ui")

class InicialApp:
    def __init__(self, master=None):
        
        # build ui
        self.toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        self.toplevel1.title("SHP HMCC")
        self.frame2 = tk.Frame(self.toplevel1)
        self.treeview1 = ttk.Treeview(self.frame2)
        self.treeview1.place(anchor='nw', height='615', relx='0.146', rely='0.12', width='1107', x='0', y='0')
        self.scrollbar1 = ttk.Scrollbar(self.frame2)
        self.scrollbar1.configure(orient='horizontal',command=self.treeview1.xview)
        self.scrollbar1.place(anchor='nw', relx='0.146', rely='0.977', width='1107', x='0', y='0')
        self.treeview1.configure(xscroll=self.scrollbar1.set)
        
        self.scrollbar2 = ttk.Scrollbar(self.frame2)
        self.scrollbar2.configure(orient='vertical',command=self.treeview1.yview)
        self.scrollbar2.place(anchor='nw', height='615', relx='0.987', rely='0.12', x='0', y='0')
        self.treeview1.configure(yscroll=self.scrollbar2.set)
        
        self.btnCadEquip = tk.Button(self.frame2)
        self.btnCadEquip.configure(text='Cadastrar Equipamento')
        self.btnCadEquip.place(anchor='nw', relx='0.013', rely='0.37', width='150', x='0', y='0')
        self.btnCadEquip.configure(command = self.insert)

        self.btnCadTreinados = tk.Button(self.frame2)
        self.btnCadTreinados.configure(text='Cadastrar Treinamento')
        self.btnCadTreinados.place(anchor='nw', relx='0.013', rely='0.42', width='150', x='0', y='0')
        self.btnCadTreinados.configure(command = CadastrarTreinados.abre)

        self.btnExibirTreinados = tk.Button(self.frame2)
        self.btnExibirTreinados.configure(text='Exibir Treinamento')
        self.btnExibirTreinados.place(anchor='nw', relx='0.013', rely='0.47', width='150', x='0', y='0')
        self.btnExibirTreinados.configure(command = ExibirTreinados.abre)
        
        self.btnCadEquipDes = tk.Button(self.frame2)
        self.btnCadEquipDes.configure(text='Cad. Equip. em Desenv.')
        self.btnCadEquipDes.place(anchor='nw', relx='0.013', rely='0.52', width='150', x='0', y='0')
        self.btnCadEquipDes.configure(command = self.insertDes)
        
        self.btnCadCalibr = tk.Button(self.frame2)
        self.btnCadCalibr.configure(text='Cadastrar Calibração')
        self.btnCadCalibr.place(anchor='nw', relx='0.013', rely='.57', width='150', x='0', y='0')
        self.btnCadCalibr.configure(command=self.insertCalibr)
        
        self.btnCadPrev = tk.Button(self.frame2)
        self.btnCadPrev.configure(text='Cadastrar Preventiva')
        self.btnCadPrev.place(anchor='nw', relx='0.013', rely='.62', width='150', x='0', y='0')
        self.btnCadPrev.configure(command=self.insertPreventiva)
        
        self.btnCadEspor = tk.Button(self.frame2)
        self.btnCadEspor.configure(text='Cadastrar Esporádica')
        self.btnCadEspor.place(anchor='nw', relx='0.013', rely='.67', width='150', x='0', y='0')
        self.btnCadEspor.configure(command=self.insertEsporadica)
        
        self.btnCadReentr = tk.Button(self.frame2)
        self.btnCadReentr.configure(text='Cadastrar Retorno')
        self.btnCadReentr.place(anchor='nw', relx='0.013', rely='.72', width='150', x='0', y='0')
        self.btnCadReentr.configure(command=self.insertReentrada)
        
        self.btnCadMov = tk.Button(self.frame2)
        self.btnCadMov.configure(text='Cadastrar Movimentação')
        self.btnCadMov.place(anchor='nw', relx='0.013', rely='.77', width='150', x='0', y='0')
        self.btnCadMov.configure(command=self.insertMovimentacao)

        self.btnDesativ = tk.Button(self.frame2)
        self.btnDesativ.configure(text='Equipamentos Desativados')
        self.btnDesativ.place(anchor='nw', relx='0.013', rely='.87', width='150', x='0', y='0')
        self.btnDesativ.configure(command=ExibirDesativados.abre)
        
        self.btnCadDesativ = tk.Button(self.frame2)
        self.btnCadDesativ.configure(text='Desativar Equipamentos')
        self.btnCadDesativ.place(anchor='nw', relx='0.013', rely='.82', width='150', x='0', y='0')
        self.btnCadDesativ.configure(command=Desativar.abre)
        
        self.button10 = tk.Button(self.frame2)
        self.button10.configure(text='Equips em Desenv.')
        self.button10.place(anchor='nw', relx='0.013', rely='0.22', width='150', x='0', y='0')
        self.button10.configure(command=lambda:[self.limpartree(), self.equipDes_view()])
        
        self.button11 = tk.Button(self.frame2)
        self.button11.configure(text='Exibir Todos')
        self.button11.place(anchor='nw', relx='0.013', rely='.27', width='150', x='0', y='0')
        self.button11.configure(command=Exibição.abre)
        
        self.button16 = tk.Button(self.frame2)
        self.button16.configure(text='Todos Equipamentos')
        self.button16.place(anchor='nw', relx='0.013', rely='.17', width='150', x='0', y='0')
        self.button16.configure(command=lambda:[self.limpartree(), self.equip_view()])
        
        self.btnProc = tk.Button(self.frame2)
        self.btnProc.configure(text='Procurar')
        self.btnProc.place(anchor='nw', relx='0.013', rely='.32', width='150', x='0', y='0')
        self.btnProc.configure(command=self.Procurar)

        self.btnAlarmes = tk.Button(self.frame2)
        self.btnAlarmes.configure(text='Alarmes')
        self.btnAlarmes.place(anchor='nw', relx='0.013', rely='.92', width='150', x='0', y='0')
        self.btnAlarmes.configure(command=Alarmes.abre)
        
        self.label1 = ttk.Label(self.frame2)
        self.cap_PNG = tk.PhotoImage(file='logo.PNG')
        self.label1.configure(background='#a5d6ef', cursor='gumby', image=self.cap_PNG)
        self.label1.place(anchor='nw', height='100', relx='0.013', rely='0.01', width='150', x='0', y='0')
        self.label2 = ttk.Label(self.frame2)
        self.label2.configure(background='#a5d6ef', font='{eras demi itc} 36 ', text='SHProgram')
        self.label2.place(anchor='nw', relx='0.146', rely='0.02', x='0', y='0')
        self.label3 = ttk.Label(self.frame2)
        self.label3.configure(borderwidth='5', font='{arial} 20 {}', relief='groove', text='HMCC')
        self.label3.place(anchor='nw', relx='0.63', rely='0.04', x='0', y='0')
        
        self.lblCadastrante = tk.Label(self.frame2)
        self.lblCadastrante.configure(background='#a5d6ef', font='{arial} 12 {bold}', foreground='#ff0000')
        self.lblCadastrante.place(anchor='nw', relx='0.63', rely='0.00', x='0', y='0')
        self.lblCadastrante.configure(text=(Programa.logado[0]))
        
        self.frame2.configure(background='#a5d6ef', borderwidth='5', height='730', relief='sunken')
        self.frame2.configure(width='1330')
        self.frame2.place(anchor='nw', relx='0.003', rely='0.003', x='0', y='0')
        self.toplevel1.configure(background='#669bdb', borderwidth='5', height='720', relief='raised')
        self.toplevel1.configure(width='1280')
        self.toplevel1.geometry('1350x730')
        
        app_width =1350
        app_height =750

        screen_width =self.toplevel1.winfo_screenwidth()
        screen_height=self.toplevel1.winfo_screenheight()

        x = (screen_width/2)-(app_width/2)
        y = (screen_height/2)-(app_height/2)

        self.toplevel1.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

        # Main widget
        self.mainwindow = self.toplevel1

    def limpartree(self):
        self.treeview1.delete(*self.treeview1.get_children())

    def equip_view(self):
        self.label3.configure(text='Equipamentos')
        for i in self.treeview1.get_children():
            self.treeview1.delete(i)
        self.treeview1['columns']=('c1','c2','c3','c4','c5','c6','c7','c8','c9','c10','c11','c12','c13','c14','c15','c16','c17','c18','c19','c20','c21','c22','c23','c24','c25','c26','c27','c28')
        self.treeview1.column('#0',width=0)
        self.treeview1.column('c1',width=100)
        self.treeview1.column('c2',width=100)
        self.treeview1.column('c3',width=100)
        self.treeview1.column('c4',width=100)
        self.treeview1.column('c5',width=100)
        self.treeview1.column('c6',width=100)
        self.treeview1.column('c7',width=120)
        self.treeview1.column('c8',width=100)
        self.treeview1.column('c9',width=100)
        self.treeview1.column('c10',width=100)
        self.treeview1.column('c11',width=100)
        self.treeview1.column('c12',width=125)
        self.treeview1.column('c13',width=120)
        self.treeview1.column('c14',width=120)
        self.treeview1.column('c15',width=135)
        self.treeview1.column('c16',width=120)
        self.treeview1.column('c17',width=130)
        self.treeview1.column('c18',width=130)
        self.treeview1.column('c19',width=100)
        self.treeview1.column('c20',width=100)
        self.treeview1.column('c21',width=100)
        self.treeview1.column('c22',width=100)
        self.treeview1.column('c23',width=100)
        self.treeview1.column('c24',width=100)
        self.treeview1.column('c25',width=100)
        self.treeview1.column('c26',width=100)
        self.treeview1.column('c27',width=100)
        self.treeview1.column('c28',width=100)
        self.treeview1.heading('#0',text='')
        self.treeview1.heading('#1',text='Situação')
        self.treeview1.heading('#2',text='Tipo')
        self.treeview1.heading('#3',text='Nome Técnico')
        self.treeview1.heading('#4',text='Modelo')
        self.treeview1.heading('#5',text='Fabricante')
        self.treeview1.heading('#6',text='Nota Fiscal')
        self.treeview1.heading('#7',text='Número de Série')
        self.treeview1.heading('#8',text='Patrimônio')
        self.treeview1.heading('#9',text='Número Anvisa')
        self.treeview1.heading('#10',text='Acessórios')
        self.treeview1.heading('#11',text='Insumos')
        self.treeview1.heading('#12',text='Data De Recebimento')
        self.treeview1.heading('#13',text='Data de Aceitação')
        self.treeview1.heading('#14',text='Data de Instalação')
        self.treeview1.heading('#15',text='Data de Funcionamento')
        self.treeview1.heading('#16',text='Data de Desativação')
        self.treeview1.heading('#17',text='Intervalo de Calibração')
        self.treeview1.heading('#18',text='Intervalo de Preventiva')
        self.treeview1.heading('#19',text='Andar Instalado')
        self.treeview1.heading('#20',text='Setor Instalado')
        self.treeview1.heading('#21',text='Local Instalado')
        self.treeview1.heading('#22',text='Andar Atual')
        self.treeview1.heading('#23',text='Setor Atual')
        self.treeview1.heading('#24',text='Local Atual')
        self.treeview1.heading('#25',text='Treinamento')
        self.treeview1.heading('#26',text='Responsável')
        self.treeview1.heading('#27',text='Observações')
        self.treeview1.heading('#28',text='Log In')
        r1 = Programa.Todos()
        for i in r1:
            self.treeview1.insert('','end',values=(i))


    def equipDes_view(self):
        self.label3.configure(text='Equipamentos em Desenvolvimento')
        self.treeview1['columns']=('c1','c2','c3','c4','c5','c6','c7','c8','c9','c10','c11','c12','c13','c14','c15','c16')
        self.treeview1.column('#0',width=0)
        self.treeview1.column('c1',width=100)
        self.treeview1.column('c2',width=100)
        self.treeview1.column('c3',width=100)
        self.treeview1.column('c4',width=100)
        self.treeview1.column('c5',width=130)
        self.treeview1.column('c6',width=100)
        self.treeview1.column('c7',width=100)
        self.treeview1.column('c8',width=100)
        self.treeview1.column('c9',width=130)
        self.treeview1.column('c10',width=100)
        self.treeview1.column('c11',width=100)
        self.treeview1.column('c12',width=100)
        self.treeview1.column('c13',width=100)
        self.treeview1.column('c14',width=100)
        self.treeview1.column('c15',width=100)
        self.treeview1.column('c16',width=100)
        self.treeview1.heading('#0',text='')
        self.treeview1.heading('#1',text='Situação')
        self.treeview1.heading('#2',text='Nome Técnico')
        self.treeview1.heading('#3',text='Modelo')
        self.treeview1.heading('#4',text='Desenvolvedor')
        self.treeview1.heading('#5',text='Número de Registro')
        self.treeview1.heading('#6',text='Acessórios')
        self.treeview1.heading('#7',text='Insumos')
        self.treeview1.heading('#8',text='Data de Entrada')
        self.treeview1.heading('#9',text='Data de Desativação')
        self.treeview1.heading('#10',text='Andar Instalado')
        self.treeview1.heading('#11',text='Setor Instalado')
        self.treeview1.heading('#12',text='Local Instalado')
        self.treeview1.heading('#13',text='Treinamento')
        self.treeview1.heading('#14',text='Responsável')
        self.treeview1.heading('#15',text='Observações')
        self.treeview1.heading('#16',text='Log In')
        r1 = Programa.TodosDes()
        for i in r1:
            self.treeview1.insert('','end',values=(i))


    def run(self):
        self.mainwindow.mainloop()

    def sair(self):
        self.mainwindow.destroy()

    def insert(self):
        CadastroEquip.abre()

    def insertDes(self):
        CadastroEquipDes.abre()

    def insertCalibr(self):
        CadastroCalibr.abre()
        
    def insertPreventiva(self):
        CadastrarPreventiva.abre()
        
    def insertEsporadica(self):
        CadastrarEsporadica.abre()
        
    def insertReentrada(self):
        CadastrarReentrada.abre()
        
    def insertMovimentacao(self):
        CadastrarMovimentacao.abre()
        
    def insertDesativacao(self):
        CadastrarDesativacao.abre()

    def Procurar(self):
        JanelaProc.abre()

            
def abre():
    app = InicialApp()
    app.run()

#abre()

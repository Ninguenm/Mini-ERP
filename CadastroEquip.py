import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
import Programa
import AvisoSucess,AvisoNSucess

#PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
#PROJECT_UI = os.path.join(PROJECT_PATH, "CadastrarEquip.ui")

class CadastrarequipApp:
    def __init__(self, master=None):
        # build ui
        self.toplevel1 = tk.Toplevel()
        self.frame2 = tk.Frame(self.toplevel1)
        self.toplevel1.title("Cadastro de Equipamento")
        self.label2 = tk.Label(self.frame2)
        self.label2.configure(font='{arial} 16 {}', justify='left', relief='groove', takefocus=False)
        self.label2.configure(text='Cadastro de Equipamento')
        self.label2.place(anchor='nw', relx='0.315', rely='0.01', width='250', x='0', y='0')

        self.combobox4 = ttk.Combobox(self.frame2)
        self.combobox4.configure(cursor='arrow',state="readonly",values=['Equipamento','Acessório'])
        self.combobox4.place(anchor='nw', relx='0.22', rely='0.12', width='170', x='0', y='0')

        a = Programa.Todos()
        r1 = []
        r2 = []
        for i in a:
            if i[2] not in r1:
                r1.append(i[2])
        for i in a:
            if i[3] not in r2:
                r2.append(i[3])

        b = Programa.ListaFabri()
        c = Programa.TodosFabri1()
        r5 = []
        for i in b:
            if i not in r5:
                r5.append(i)
        for i in c:
            if i not in r5:
                r5.append(i)
        

        self.combobox6 = ttk.Combobox(self.frame2)
        self.combobox6.configure(cursor='arrow',values=r1)
        self.combobox6.place(anchor='nw', relx='0.692', rely='0.12', width='170', x='0', y='0')

        self.combobox7 = ttk.Combobox(self.frame2)
        self.combobox7.configure(cursor='arrow',values=Programa.TodosDale(self.combobox6.bind("<<ComboboxSelected>>",self.getSelected1)))
        self.combobox7.place(anchor='nw', relx='0.22', rely='0.19', width='170', x='0', y='0')

        self.combobox3 = ttk.Combobox(self.frame2)
        self.combobox3.configure(cursor='arrow',state="readonly",values=r5)
        self.combobox3.place(anchor='nw', relx='0.692', rely='0.19', width='170', x='0', y='0')
        
        self.entNota = tk.Entry(self.frame2)
        _text_ = ''''''
        self.entNota.delete('0', 'end')
        self.entNota.insert('0', _text_)
        self.entNota.place(anchor='nw', relx='0.22', rely='0.26', width='170', x='0', y='0')

        self.combobox5 = ttk.Combobox(self.frame2)
        self.combobox5.insert('0','Digite o N°')
        self.combobox5.configure(cursor='arrow',values=['Digite o N°','Ilegível'])
        self.combobox5.place(anchor='nw', relx='0.692', rely='0.26', width='170', x='0', y='0')
        
        self.entPatri = tk.Entry(self.frame2)
        _text_ = ''''''
        self.entPatri.delete('0', 'end')
        self.entPatri.insert('0', _text_)
        self.entPatri.place(anchor='nw', relx='0.22', rely='0.33', width='170', x='0', y='0')

        self.comboboxPatri = ttk.Combobox(self.frame2)
        self.comboboxPatri.insert('0','Digite o Patrimônio')
        self.comboboxPatri.configure(cursor='arrow',values=['Digite o Patrimônio','Branco'])
        self.comboboxPatri.place(anchor='nw', relx='0.22', rely='0.33', width='170', x='0', y='0')

        self.entAnvisa = tk.Entry(self.frame2)
        _text_ = ''''''
        self.entAnvisa.delete('0', 'end')
        self.entAnvisa.insert('0', _text_)
        self.entAnvisa.place(anchor='nw', relx='0.692', rely='0.33', width='170', x='0', y='0')
        
        self.entAcessor = tk.Entry(self.frame2)
        _text_ = ''''''
        self.entAcessor.delete('0', 'end')
        self.entAcessor.insert('0', _text_)
        self.entAcessor.place(anchor='nw', relx='0.22', rely='0.40', width='170', x='0', y='0')
        
        self.entInsumo = tk.Entry(self.frame2)
        _text_ = ''''''
        self.entInsumo.delete('0', 'end')
        self.entInsumo.insert('0', _text_)
        self.entInsumo.place(anchor='nw', relx='0.692', rely='0.40', width='170', x='0', y='0')

        self.entData_Receb = tk.Entry(self.frame2)
        _text_ = '''dd-mm-aaaa'''
        self.entData_Receb.delete('0', 'end')
        self.entData_Receb.insert('0', _text_)
        self.entData_Receb.place(anchor='nw', relx='0.22', rely='0.47', width='170', x='0', y='0')

        self.entData_Aceit = tk.Entry(self.frame2)
        _text_ = '''dd-mm-aaaa'''
        self.entData_Aceit.delete('0', 'end')
        self.entData_Aceit.insert('0', _text_)
        self.entData_Aceit.place(anchor='nw', relx='0.692', rely='0.47', width='170', x='0', y='0')

        self.entData_Inst = tk.Entry(self.frame2)
        _text_ = '''dd-mm-aaaa'''
        self.entData_Inst.delete('0', 'end')
        self.entData_Inst.insert('0', _text_)
        self.entData_Inst.place(anchor='nw', relx='0.22', rely='0.54', width='170', x='0', y='0')
        
        self.entData_Func = tk.Entry(self.frame2)
        _text_ = '''dd-mm-aaaa'''
        self.entData_Func.delete('0', 'end')
        self.entData_Func.insert('0', _text_)
        self.entData_Func.place(anchor='nw', relx='0.692', rely='0.54', width='170', x='0', y='0')

        self.entData_Fabri = tk.Entry(self.frame2)
        _text_ = '''dd-mm-aaaa'''
        self.entData_Fabri.delete('0', 'end')
        self.entData_Fabri.insert('0', _text_)
        self.entData_Fabri.place(anchor='nw', relx='0.22', rely='0.61', width='170', x='0', y='0')
        
        self.entTempCalibr = tk.Entry(self.frame2)
        _text_ = '''Em Meses!'''
        self.entTempCalibr.delete('0', 'end')
        self.entTempCalibr.insert('0', _text_)
        self.entTempCalibr.place(anchor='nw', relx='0.692', rely='0.61', width='170', x='0', y='0')
        
        self.entTempPrev = tk.Entry(self.frame2)
        _text_ = '''Em Meses!'''
        self.entTempPrev.delete('0', 'end')
        self.entTempPrev.insert('0', _text_)
        self.entTempPrev.place(anchor='nw', relx='0.22', rely='0.68', width='170', x='0', y='0')

        self.combobox2 = ttk.Combobox(self.frame2)
        self.combobox2.configure(cursor='arrow',state='readonly',values=list(Programa.ListaAndares()))
        self.combobox2.place(anchor='nw', relx='0.692', rely='0.68', width='170', x='0', y='0')
        
        self.combobox1 = ttk.Combobox(self.frame2)
        self.combobox1.configure(cursor='arrow',state='readonly',values=Programa.ListaSetores(self.combobox2.bind("<<ComboboxSelected>>",self.getSelected)))
        self.combobox1.place(anchor='nw', relx='0.22', rely='0.75', width='170', x='0', y='0')
    
        self.entLocal_Inst = tk.Entry(self.frame2)
        _text_ = ''''''
        self.entLocal_Inst.delete('0', 'end')
        self.entLocal_Inst.insert('0', _text_)
        self.entLocal_Inst.place(anchor='nw', relx='0.692', rely='0.75', width='170', x='0', y='0')
        
        self.entObs = tk.Entry(self.frame2)
        _text_ = ''''''
        self.entObs.delete('0', 'end')
        self.entObs.insert('0', _text_)
        self.entObs.place(anchor='nw', relx='0.22', rely='0.82', width='488', x='0', y='0')

        self.lblTipo = tk.Label(self.frame2)
        self.lblTipo.configure(relief='groove', takefocus=False, text='*Tipo')
        self.lblTipo.place(anchor='nw', relx='0.023', rely='0.12', width='130', x='0', y='0')
        
        self.lblNomeTec = tk.Label(self.frame2)
        self.lblNomeTec.configure(relief='groove', takefocus=False, text='*Nome Técnico')
        self.lblNomeTec.place(anchor='nw', relx='0.495', rely='0.12', width='130', x='0', y='0')
        
        self.lblModelo = tk.Label(self.frame2)
        self.lblModelo.configure(relief='groove', text='*Modelo')
        self.lblModelo.place(anchor='nw', relx='0.023', rely='0.19', width='130', x='0', y='0')
        
        self.lblFabricante = tk.Label(self.frame2)
        self.lblFabricante.configure(relief='groove', text='*Fabricante')
        self.lblFabricante.place(anchor='nw', relx='0.495', rely='0.19', width='130', x='0', y='0')

        self.lblNota = tk.Label(self.frame2)
        self.lblNota.configure(relief='groove', text='Nota Fiscal')
        self.lblNota.place(anchor='nw', relx='0.023', rely='0.26', width='130', x='0', y='0')

        self.lblNumSerie = tk.Label(self.frame2)
        self.lblNumSerie.configure(relief='groove', text='*Número de Série')
        self.lblNumSerie.place(anchor='nw', relx='0.495', rely='0.26', width='130', x='0', y='0')
        
        self.lblPatri = tk.Label(self.frame2)
        self.lblPatri.configure(relief='groove', text='*Patrimônio')
        self.lblPatri.place(anchor='nw', relx='0.023', rely='0.33', width='130', x='0', y='0')

        self.lblAnvisa = tk.Label(self.frame2)
        self.lblAnvisa.configure(relief='groove', text='Registro Anvisa')
        self.lblAnvisa.place(anchor='nw', relx='0.495', rely='0.33', width='130', x='0', y='0')
        
        self.lblAcessorios = tk.Label(self.frame2)
        self.lblAcessorios.configure(relief='groove', text='Acessórios')
        self.lblAcessorios.place(anchor='nw', relx='0.023', rely='0.40', width='130', x='0', y='0')
        
        self.lblInsumos = tk.Label(self.frame2)
        self.lblInsumos.configure(relief='groove', text='Insumos')
        self.lblInsumos.place(anchor='nw', relx='0.495', rely='0.40', width='130', x='0', y='0')

        self.lblData_Receb = tk.Label(self.frame2)
        self.lblData_Receb.configure(relief='groove', text='*Data de Recebimento')
        self.lblData_Receb.place(anchor='nw', relx='0.023', rely='0.47', width='130', x='0', y='0')
        
        self.lblData_Aceitacao = tk.Label(self.frame2)
        self.lblData_Aceitacao.configure(relief='groove', text='*Data de Aceitação')
        self.lblData_Aceitacao.place(anchor='nw', relx='0.495', rely='0.47', width='130', x='0', y='0')

        self.lblData_Inst = tk.Label(self.frame2)
        self.lblData_Inst.configure(relief='groove', text='*Data de Instalação')
        self.lblData_Inst.place(anchor='nw', relx='0.023', rely='0.54', width='130', x='0', y='0')
        
        self.lblData_Func = tk.Label(self.frame2)
        self.lblData_Func.configure(relief='groove', text='*Data de Funcionamen.')
        self.lblData_Func.place(anchor='nw', relx='0.495', rely='0.54', width='130', x='0', y='0')

        self.lblData_Fabri = tk.Label(self.frame2)
        self.lblData_Fabri.configure(relief='groove', text='*Data de Fabricação')
        self.lblData_Fabri.place(anchor='nw', relx='0.023', rely='0.61', width='130', x='0', y='0')
        
        self.lblTemp_Calibr = tk.Label(self.frame2)
        self.lblTemp_Calibr.configure(relief='groove', text='Intervalo de Calibração')
        self.lblTemp_Calibr.place(anchor='nw', relx='0.495', rely='0.61', width='130', x='0', y='0')
        
        self.lblTemp_Prev = tk.Label(self.frame2)
        self.lblTemp_Prev.configure(relief='groove', text='Intervalo de Preventiva')
        self.lblTemp_Prev.place(anchor='nw', relx='0.023', rely='0.68', width='130', x='0', y='0')
    
        self.button1 = tk.Button(self.frame2)
        self.button1.configure(font='{Arial} 12 {}', text='Cadastrar')
        self.button1.place(anchor='nw', relx='0.325', rely='0.90', width='100', x='0', y='0')
        self.button1.configure(command = self.insert)
        
        self.button2 = tk.Button(self.frame2)
        self.button2.configure(font='{Arial} 12 {}', text='Sair')
        self.button2.place(anchor='nw', relx='0.4955', rely='0.90', width='100', x='0', y='0')
        self.button2.configure(command = self.fecha)


        self.lblAndar_Inst = tk.Label(self.frame2)
        self.lblAndar_Inst.configure(relief='groove', text='*Andar Instalado')
        self.lblAndar_Inst.place(anchor='nw', relx='0.495', rely='0.68', width='130', x='0', y='0')
        
        self.lblSetor_Inst = tk.Label(self.frame2)
        self.lblSetor_Inst.configure(relief='groove', text='*Setor Instalado')
        self.lblSetor_Inst.place(anchor='nw', relx='0.023', rely='0.75', width='130', x='0', y='0')

        self.lblLocal_Inst = tk.Label(self.frame2)
        self.lblLocal_Inst.configure(relief='groove', text='Local Instalado')
        self.lblLocal_Inst.place(anchor='nw', relx='0.495', rely='0.75', width='130', x='0', y='0')
        
        self.lblObs = tk.Label(self.frame2)
        self.lblObs.configure(relief='groove', text='Observação')
        self.lblObs.place(anchor='nw', relx='0.023', rely='0.82', width='130', x='0', y='0')

        self.label3 = tk.Label(self.frame2)
        self.label3.configure(background='#a5d6ef', font='{Arial} 12 {bold}', foreground='#ff171d', text='* Campos Obrigatórios')
        self.label3.place(anchor='nw', relx='0.70', rely='0.95', x='0', y='0')
 
        self.frame2.configure(background='#a5d6ef', borderwidth='5', height='600', relief='sunken')
        self.frame2.configure(width='683')
        self.frame2.place(anchor='nw', relx='0.003', rely='0.003', x='0', y='0')
        self.toplevel1.configure(background='#669bdb', borderwidth='5', height='615', relief='raised')
        self.toplevel1.configure(width='700')

        app_width =700
        app_height =615

        screen_width =self.toplevel1.winfo_screenwidth()
        screen_height=self.toplevel1.winfo_screenheight()

        x = (screen_width/2)-(app_width/2)
        y = (screen_height/2)-(app_height/2)

        self.toplevel1.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

        # Main widget
        self.mainwindow = self.toplevel1
        #self.mainwindow.eval('tk::PlaceWindow . center')
    

    def run(self):
        self.mainwindow.mainloop()

    def fecha(self):
        self.mainwindow.destroy()

    def getSelected(self, event):
        self.combobox1['values']=Programa.ListaSetores(self.combobox2.get())
        self.combobox1.set('')

    def getSelected1(self, event):
        self.combobox7['values']=Programa.TodosDale(self.combobox6.get())
        self.combobox7.set('')
        

    def insert(self):
        try:
            Programa.cadastrarEquip(self.combobox4.get(),self.combobox6.get(), self.combobox7.get(),self.combobox3.get(),self.entNota.get(), self.combobox5.get(),self.comboboxPatri.get(),self.entAnvisa.get(),self.entAcessor.get(),self.entInsumo.get(),self.entData_Receb.get(),self.entData_Aceit.get(),self.entData_Inst.get(),self.entData_Func.get(),self.entData_Fabri.get(),self.entTempCalibr.get(),self.entTempPrev.get(),self.combobox2.get(),self.combobox1.get(),self.entLocal_Inst.get(),self.entObs.get())
            self.mainwindow.destroy()
            AvisoSucess.abre()
        except:
            AvisoNSucess.abre()
            
        
def abre():
    app = CadastrarequipApp()
    app.run()

#abre()


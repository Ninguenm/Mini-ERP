import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
import Programa

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "Alarmes.ui")

import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "Alarmes.ui")

class AlarmesApp:
    def __init__(self, master=None):
        # build ui
        self.toplevel1 = tk.Toplevel()
        self.toplevel1.title("Alarmes")
        self.frame2 = tk.Frame(self.toplevel1)
        self.cap_PNG = tk.PhotoImage(file='logo.PNG')
        self.label1 = tk.Label(self.frame2)
        self.label1.configure(background='#a5d6ef', cursor='gumby', image=self.cap_PNG)
        self.label1.place(anchor='nw', height='100', relx='0.013', rely='0.01', width='150', x='0', y='0')
        self.treeview2 = ttk.Treeview(self.frame2)
        self.treeview2.place(anchor='nw', height='150', relx='0.146', rely='0.757', width='1050', x='0', y='0')
        self.scrollbot1 = ttk.Scrollbar(self.frame2)
        self.scrollbot1.configure(orient='horizontal',command=self.treeview2.xview)
        self.scrollbot1.place(anchor='nw', relx='0.146', rely='0.977', width='1050', x='0', y='0')
        self.scrollbot = ttk.Scrollbar(self.frame2)
        self.scrollbot.configure(orient='vertical',command=self.treeview2.yview)
        self.scrollbot.place(anchor='nw', height='150', relx='0.987', rely='0.757', x='0', y='0')
        self.treeview2.configure(xscroll=self.scrollbot1.set)
        self.treeview2.configure(yscroll=self.scrollbot.set)
        
        self.label2 = ttk.Label(self.frame2)
        self.label2.configure(background='#a5d6ef', font='{eras demi itc} 36 ', text='SHProgram')
        self.label2.place(anchor='nw', relx='0.146', rely='0.02', x='0', y='0')
        self.label3 = ttk.Label(self.frame2)
        self.label3.configure(borderwidth='5', font='{arial} 24 {}', relief='groove', text='       Alarmes')
        self.label3.place(anchor='nw', relx='0.68', rely='0.03', width='250', x='0', y='0')
        
        self.btnCalibri = tk.Button(self.frame2)
        self.btnCalibri.configure(text='Calibrações')
        self.btnCalibri.place(anchor='nw', relx='0.013', rely='0.22', width='150', x='0', y='0')
        self.btnCalibri.configure(command=lambda:[self.limpartree(),self.Calibri_view()])
        
        self.btnPrev = tk.Button(self.frame2)
        self.btnPrev.configure(text='Preventivas')
        self.btnPrev.place(anchor='nw', relx='0.013', rely='0.32', width='150', x='0', y='0')
        self.btnPrev.configure(command=lambda:[self.limpartree(),self.Prevent_view()])

        self.btnManu = tk.Button(self.frame2)
        self.btnManu.configure(text='Manutenções')
        self.btnManu.place(anchor='nw', relx='0.013', rely='0.42', width='150', x='0', y='0')
        self.btnManu.configure(command=lambda:[self.limpartree(),self.insertManu_view()])

        self.btnemprest = tk.Button(self.frame2)
        self.btnemprest.configure(text='Empréstimos')
        self.btnemprest.place(anchor='nw', relx='0.013', rely='0.52', width='150', x='0', y='0')
        self.btnemprest.configure(command=lambda:[self.limpartree(),self.insertemprest_view()])
        
        self.entPatriNumSerie = ttk.Entry(self.frame2)
        _text_ = '''Patrimônio ou N° Série'''
        self.entPatriNumSerie.delete('0', 'end')
        self.entPatriNumSerie.insert('0', _text_)
        self.entPatriNumSerie.place(anchor='nw', relx='0.013', rely='0.8', width='150', x='0', y='0')
        
        self.btnLocalizar = tk.Button(self.frame2)
        self.btnLocalizar.configure(text='Localizar')
        self.btnLocalizar.place(anchor='nw', relx='0.013', rely='0.83', width='150', x='0', y='0')
        self.btnLocalizar.configure(command=self.insertLocalizar_view)
        
        self.btnLimpar = tk.Button(self.frame2)
        self.btnLimpar.configure(text='Limpar')
        self.btnLimpar.place(anchor='nw', relx='0.013', rely='0.9', width='150', x='0', y='0')
        self.btnLimpar.configure(command=self.limpartree1)
        
        self.treeview1 = ttk.Treeview(self.frame2)
        self.treeview1.place(anchor='nw', height='405', relx='0.146', rely='0.12', width='1050', x='0', y='0')
        self.scrolltop1 = ttk.Scrollbar(self.frame2)
        self.scrolltop1.configure(orient='horizontal',command=self.treeview1.xview)
        self.scrolltop1.place(anchor='nw', relx='0.146', rely='0.71', width='1050', x='0', y='0')
        self.scrolltop2 = ttk.Scrollbar(self.frame2)
        self.scrolltop2.configure(orient='vertical',command=self.treeview1.yview)
        self.scrolltop2.place(anchor='nw', height='405', relx='.987', rely='0.12', x='0', y='0')
        self.treeview1.configure(xscroll=self.scrolltop1.set)
        self.treeview1.configure(yscroll=self.scrolltop2.set)

        
        self.frame2.configure(background='#a5d6ef', borderwidth='5', height='700', relief='sunken')
        self.frame2.configure(takefocus=True, width='1260')
        self.frame2.place(anchor='nw', relx='0.003', rely='0.003', x='0', y='0')
        self.toplevel1.configure(background='#669bdb', borderwidth='5', height='668', relief='raised')
        self.toplevel1.configure(takefocus=True, width='568')
        self.toplevel1.geometry('1280x720')
        
        app_width =1280
        app_height =720

        screen_width =self.toplevel1.winfo_screenwidth()
        screen_height=self.toplevel1.winfo_screenheight()

        x = (screen_width/2)-(app_width/2)
        y = (screen_height/2)-(app_height/2)

        self.toplevel1.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

        

        # Main widget
        self.mainwindow = self.toplevel1

    def limpartree(self):
        self.treeview1.delete(*self.treeview1.get_children())

    def limpartree1(self):
        self.treeview2.delete(*self.treeview2.get_children())

    def Calibri_view(self):
        self.treeview1['columns']=('c1','c2','c3','c4','c5','c6','c7')
        self.treeview1.column('#0',width=0)
        self.treeview1.column('c1',width=150)
        self.treeview1.column('c2',width=150)
        self.treeview1.column('c3',width=150)
        self.treeview1.column('c5',width=150)
        self.treeview1.column('c5',width=200)
        self.treeview1.column('c6',width=350)
        self.treeview1.column('c7',width=800)
        self.treeview1.heading('#0',text='')
        self.treeview1.heading('#1',text='Nome Técnico')
        self.treeview1.heading('#2',text='Modelo')
        self.treeview1.heading('#3',text='Número de Série')
        self.treeview1.heading('#4',text='Patrimônio')
        self.treeview1.heading('#5',text='Atenção')
        self.treeview1.heading('#6',text='Localização')
        r1 = Programa.alarme()
        for i in r1:
            self.treeview1.insert('','end',values=(i[0],i[1],i[2],i[3],i[4],i[5], ))

    def Prevent_view(self):
        self.treeview1['columns']=('c1','c2','c3','c4','c5','c6','c7')
        self.treeview1.column('#0',width=0)
        self.treeview1.column('c1',width=150)
        self.treeview1.column('c2',width=150)
        self.treeview1.column('c3',width=150)
        self.treeview1.column('c5',width=150)
        self.treeview1.column('c5',width=200)
        self.treeview1.column('c6',width=350)
        self.treeview1.column('c7',width=800)
        self.treeview1.heading('#0',text='')
        self.treeview1.heading('#1',text='Nome Técnico')
        self.treeview1.heading('#2',text='Modelo')
        self.treeview1.heading('#3',text='Número de Série')
        self.treeview1.heading('#4',text='Patrimônio')
        self.treeview1.heading('#5',text='Atenção')
        self.treeview1.heading('#6',text='Localização')
        r1 = Programa.alarme1()
        for i in r1:
            self.treeview1.insert('','end',values=(i[0],i[1],i[2],i[3],i[4],i[5], ))

    def insertLocalizar_view(self):
            self.treeview2['columns']=('c1','c2','c3','c4','c5','c6','c7','c8')
            self.treeview2.column('#0',width=0)
            self.treeview2.column('c1',width=100)
            self.treeview2.column('c2',width=100)
            self.treeview2.column('c3',width=100)
            self.treeview2.column('c4',width=100)
            self.treeview2.column('c5',width=100)
            self.treeview2.column('c6',width=100)
            self.treeview2.column('c7',width=100)
            self.treeview2.column('c8',width=100)
            self.treeview2.heading('#0',text='')
            self.treeview2.heading('#1',text='Situação')
            self.treeview2.heading('#2',text='Nome Técnico')
            self.treeview2.heading('#3',text='Modelo')
            self.treeview2.heading('#4',text='Número de Série')
            self.treeview2.heading('#5',text='Patrimônio')
            self.treeview2.heading('#6',text='Andar Atual')
            self.treeview2.heading('#7',text='Setor Atual')
            self.treeview2.heading('#8',text='Local Atual')
            r1 =Programa.LocalizarEquip(self.entPatriNumSerie.get())
            for i in r1:
                self.treeview2.insert('','end',values=(i))

    def insertManu_view(self):
            self.treeview1['columns']=('c1','c2','c3','c4','c5')
            self.treeview1.column('#0',width=0)
            self.treeview1.column('c1',width=100)
            self.treeview1.column('c2',width=100)
            self.treeview1.column('c3',width=100)
            self.treeview1.column('c4',width=100)
            self.treeview1.column('c5',width=100)
            self.treeview1.heading('#0',text='')
            self.treeview1.heading('#1',text='Nome Técnico')
            self.treeview1.heading('#2',text='Número de Série')
            self.treeview1.heading('#3',text='Patrimônio')
            self.treeview1.heading('#4',text='Andar Atual')
            self.treeview1.heading('#5',text='Local Atual')
            r1 =Programa.manu()
            for i in r1:
                self.treeview1.insert('','end',values=(i))

    def insertemprest_view(self):
            self.treeview1['columns']=('c1','c2','c3','c4','c5')
            self.treeview1.column('#0',width=0)
            self.treeview1.column('c1',width=100)
            self.treeview1.column('c2',width=100)
            self.treeview1.column('c3',width=100)
            self.treeview1.column('c4',width=100)
            self.treeview1.column('c5',width=100)
            self.treeview1.heading('#0',text='')
            self.treeview1.heading('#1',text='Nome Técnico')
            self.treeview1.heading('#2',text='Número de Série')
            self.treeview1.heading('#3',text='Patrimônio')
            self.treeview1.heading('#4',text='Andar Atual')
            self.treeview1.heading('#5',text='Local Atual')
            r1 =Programa.emprest()
            for i in r1:
                self.treeview1.insert('','end',values=(i))

    def run(self):
        self.mainwindow.mainloop()

def abre():
    app = AlarmesApp()
    app.run()

#abre()

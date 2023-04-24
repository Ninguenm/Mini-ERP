import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
import Programa

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "AlarmesPOPUP.ui")

class AlarmespopupApp:
    def __init__(self, master=None):
        # build ui
        self.toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        self.frame2 = tk.Frame(self.toplevel1)
        self.toplevel1.title("Alarmes")
        self.treeview1 = ttk.Treeview(self.frame2)
        self.treeview1.place(anchor='nw', height='590', relx='0.01', rely='0.12', width='1050', x='0', y='0')
        self.scrollbar1 = ttk.Scrollbar(self.frame2)
        self.scrollbar1.configure(orient='horizontal',command=self.treeview1.xview)
        self.scrollbar1.place(anchor='nw', relx='0.01', rely='0.977', width='1050', x='0', y='0')
        self.scrollbar2 = ttk.Scrollbar(self.frame2)
        self.scrollbar2.configure(orient='vertical',command=self.treeview1.yview)
        self.scrollbar2.place(anchor='nw', height='590', relx='0.983', rely='0.12', x='0', y='0')
        self.treeview1.configure(xscroll=self.scrollbar1.set)
        self.treeview1.configure(yscroll=self.scrollbar2.set)
        self.label3 = ttk.Label(self.frame2)
        self.label3.configure(borderwidth='5', font='{arial} 24 {bold}', relief='groove', text='      Alarmes')
        self.label3.place(anchor='nw', height='60', relx='0.05', rely='0.02', width='250', x='0', y='0')
        self.button1 = tk.Button(self.frame2)
        self.button1.configure(text='Calibrações')
        self.button1.place(anchor='nw', height='40', relx='0.4', rely='0.033', width='200', x='0', y='0')
        self.button1.configure(command=lambda:[self.limpartree(), self.Calibri_view()])
        
        self.button2 = tk.Button(self.frame2)
        self.button2.configure(text='Preventivas')
        self.button2.place(anchor='nw', height='40', relx='0.71', rely='0.033', width='200', x='0', y='0')
        self.button2.configure(command=lambda:[self.limpartree(), self.Prevent_view()])
        
        self.frame2.configure(background='#a5d6ef', borderwidth='5', height='700', relief='sunken')
        self.frame2.configure(takefocus=True, width='1090')
        self.frame2.place(anchor='nw', relx='0.003', rely='0.003', x='0', y='0')
        self.toplevel1.configure(background='#ff0000', borderwidth='5', height='717', relief='raised')
        self.toplevel1.configure(takefocus=True, width='1109')

        app_width =1109
        app_height =717

        screen_width =self.toplevel1.winfo_screenwidth()
        screen_height=self.toplevel1.winfo_screenheight()

        x = (screen_width/2)-(app_width/2)
        y = (screen_height/2)-(app_height/2)

        self.toplevel1.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

        
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
        r2 = Programa.alarme1()
        for i in r1:
            self.treeview1.insert('','end',values=(i[0],i[1],i[2],i[3],i[4],i[5] ))
        for i in r2:
            self.treeview1.insert('','end',values=(i[0],i[1],i[2],i[3],i[4],i[5] ))
            
        # Main widget
        self.mainwindow = self.toplevel1
    
    
    def run(self):
        self.mainwindow.mainloop()

    def limpartree(self):
        self.treeview1.delete(*self.treeview1.get_children())

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
            self.treeview1.insert('','end',values=(i[0],i[1],i[2],i[3],i[4],i[5] ))

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
            self.treeview1.insert('','end',values=(i[0],i[1],i[2],i[3],i[4],i[5] ))
def abre():
    app = AlarmespopupApp()
    app.run()

#abre()

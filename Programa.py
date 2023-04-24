#from openpyxl import *
import sqlite3
from datetime import datetime
from datetime import date
from shutil import copyfile

con = sqlite3.connect('HMCC.db')
cur=con.cursor()
cur.execute('PRAGMA foreign_keys = ON')
#cur.execute("DROP TABLE IF EXISTS equipamentos")
#cur.execute("DROP TABLE IF EXISTS calibracao")
#cur.execute("DROP TABLE IF EXISTS preventiva")
#cur.execute("DROP TABLE IF EXISTS esporadica")
#cur.execute("DROP TABLE IF EXISTS movimentacao")
#cur.execute("DROP TABLE IF EXISTS desativacao")
#cur.execute("DROP TABLE IF EXISTS reentrada")
#cur.execute("DROP TABLE IF EXISTS equip_desenv")
#cur.execute("DROP TABLE IF EXISTS desativacao_des")
#cur.execute("DROP TABLE IF EXISTS fabricantes")
#cur.execute("DROP TABLE IF EXISTS treinados")
#cur.execute("DROP TABLE IF EXISTS tempos")
#cur.execute("DROP TABLE IF EXISTS andares")
#cur.execute("DROP TABLE IF EXISTS setores")

logado = []

def BackUP():
    dia_backup=date.today()
    str_dia_backup = str(dia_backup).replace('-','_')
    file_input=r"HMCC.db"
    file_output=r"BackUps"+'\\'+str_dia_backup+"_BackUp_HMCC.db"
    copyfile(file_input,file_output)

def createXesque():
    sql="""CREATE TABLE IF NOT EXISTS xesque (
           dale text PRIMARY KEY);"""

    try:
        cur = con.cursor()
        cur.execute(sql)
    except Error as e:
        print(e)

    return

createXesque()

def createEquipamentos():
    sql="""CREATE TABLE IF NOT EXISTS equipamentos (
           situacao text,
           tipo text NOT NULL,
           nometec text NOT NULL,
           modelo text NOT NULL,
           fabricante text NOT NULL,
           nota_fisc text,
           numserie text NOT NULL PRIMARY KEY,
           patri text NOT NULL UNIQUE,
           numanvisa text,
           acessorios text,
           insumos text,
           data_recebimento text NOT NULL,
           data_aceitação text NOT NULL,
           data_instalação text NOT NULL,
           data_funcionamento text NOT NULL,
           data_fabricação text,
           data_desativ text,
           temp_calibracao integer,
           temp_preventiva integer,
           andar_ins text NOT NULL,
           setor_ins text NOT NULL,
           local_ins text,
           andar_atual text,
           setor_atual text,
           local_atual text,
           treinamento text,
           obs text,
           logado text NOT NULL
           );"""

    try:
        cur = con.cursor()
        cur.execute(sql)
    except Error as e:
        print(e)

    return

def createCadastro():
    sql = """CREATE TABLE IF NOT EXISTS cadastros (
             nome text NOT NULL,
             usuario text NOT NULL,
             senha text NOT NULL,
             consenha text NOT NULL,
             rf text NOT NULL PRIMARY KEY);"""

    try:
        cur = con.cursor()
        cur.execute(sql)
    except Error as e:
        print(e)

    return

def createCalibração():  #VERIFICAR PRIMARY KEY = patrimonio ou numero de série ------- FOREIGN KEY
    sql="""CREATE TABLE IF NOT EXISTS calibracao (
           tipo text,
           patri text,
           numserie text NOT NULL,
           data_retirada text NOT NULL,
           acessorios_retirados text,
           andar_retirado text NOT NULL,
           setor_retirado text NOT NULL,
           local_retirado text,
           empresa_resp text NOT NULL,
           tecnico text NOT NULL,
           ord_serv text NOT NULL,
           enferm_resp text NOT NULL,
           obs text,
           logado text NOT NULL,
           FOREIGN KEY(patri) REFERENCES equipamentos(patri)
           FOREIGN KEY(numserie) REFERENCES equipamentos(numserie));"""

    try:
        cur = con.cursor()
        cur.execute(sql)
    except Error as e:
        print(e)

    return

def createPreventiva():
    sql="""CREATE TABLE IF NOT EXISTS preventiva (
           tipo text,
           patri text,
           numserie text NOT NULL,
           data_retirada text NOT NULL,
           acessorios_retirados text,
           andar_retirado text NOT NULL,
           setor_retirado text NOT NULL,
           local_retirado text,
           empresa_resp text NOT NULL,
           tecnico text NOT NULL,
           ord_serv text NOT NULL,
           enferm_resp text NOT NULL,
           obs text,
           logado text NOT NULL,
           FOREIGN KEY(patri) REFERENCES equipamentos(patri)
           FOREIGN KEY(numserie) REFERENCES equipamentos(numserie));"""
    
    try:
        cur = con.cursor()
        cur.execute(sql)
    except Error as e:
        print(e)

    return

def createManutençãoEsporadica():
    sql="""CREATE TABLE IF NOT EXISTS esporadica (
           tipo text,
           patri text,
           numserie text NOT NULL,
           data_retirada text NOT NULL,
           prob_relatado text NOT NULL,
           acessorios_retirados text,
           andar_retirado text NOT NULL,
           setor_retirado text NOT NULL,
           local_retirado text,
           empresa_resp text NOT NULL,
           tecnico text NOT NULL,
           ord_serv text NOT NULL,
           enferm_resp text NOT NULL,
           obs text,
           logado text NOT NULL,
           FOREIGN KEY(patri) REFERENCES equipamentos(patri)
           FOREIGN KEY(numserie) REFERENCES equipamentos(numserie));"""
    
    try:
        cur = con.cursor()
        cur.execute(sql)
    except Error as e:
        print(e)

    return

def createReentrada():
    sql="""CREATE TABLE IF NOT EXISTS reentrada(
           tipo text,
           patri text,
           numserie text NOT NULL,
           data_reentrada text NOT NULL,
           motivo text NOT NULL,
           peças_trocadas text,
           andar_dest text NOT NULL,
           setor_dest text NOT NULL,
           local_dest text,
           responsavel text NOT NULL,
           obs text,
           logado text NOT NULL,
           FOREIGN KEY(patri) REFERENCES equipamentos(patri)
           FOREIGN KEY(numserie) REFERENCES equipamentos(numserie));"""
    
    try:
        cur = con.cursor()
        cur.execute(sql)
    except Error as e:
        print(e)

    return

def createMovimentacao():
    sql="""CREATE TABLE IF NOT EXISTS movimentacao(
           tipo text,
           patri text,
           numserie text NOT NULL,
           data_mov text NOT NULL,
           andar_org text NOT NULL,
           setor_org text NOT NULL,
           local_org text,
           andar_dest text NOT NULL,
           setor_dest text NOT NULL,
           local_dest text,
           acessorios text,
           ord_serv text NOT NULL,
           obs text,
           logado text NOT NULL,
           FOREIGN KEY(patri) REFERENCES equipamentos(patri)
           FOREIGN KEY(numserie) REFERENCES equipamentos(numserie));"""

    try:
        cur = con.cursor()
        cur.execute(sql)
    except Error as e:
        print(e)

    return

def createDesativacao():
    sql="""CREATE TABLE IF NOT EXISTS desativacao(
           tipo text,
           patri text UNIQUE,
           numserie text NOT NULL PRIMARY KEY,
           data_desativ text NOT NULL,
           motivo_desativ text NOT NULL,
           num_processo text NOT NULL,
           obs text,
           logado text NOT NULL,
           carta_desc BLOB,
           FOREIGN KEY(patri) REFERENCES equipamentos(patri)
           FOREIGN KEY(numserie) REFERENCES equipamentos(numserie));"""

    try:
        cur = con.cursor()
        cur.execute(sql)
    except Error as e:
        print(e)

    return

def createDesativacaoDes():
    sql="""CREATE TABLE IF NOT EXISTS desativacao_des(
           tipo text,
           num_registro text NOT NULL PRIMARY KEY,
           data_desativ text NOT NULL,
           motivo_desativ text NOT NULL,
           num_processo text NOT NULL,
           obs text,
           logado text NOT NULL,
           carta_desc BLOB,
           FOREIGN KEY(num_registro) REFERENCES equip_desenv(num_registro));"""

    try:
        cur = con.cursor()
        cur.execute(sql)
    except Error as e:
        print(e)

    return

def createEquipamentoEmDesenvolvimento():
    sql="""CREATE TABLE IF NOT EXISTS equip_desenv(
           situacao text,
           nometec text NOT NULL,
           modelo text NOT NULL,
           desenvolvedor text NOT NULL,
           num_registro text NOT NULL PRIMARY KEY,
           acessorios text,
           insumos text,
           data_entrada text NOT NULL,
           data_desativ text,
           andar_ins text NOT NULL,
           setor_ins text NOT NULL,
           local_ins text,
           treinamento text,
           responsavel text NOT NULL,
           obs text,
           logado text NOT NULL);"""

    try:
        cur = con.cursor()
        cur.execute(sql)
    except Error as e:
        print(e)

    return

def createAndar():
    sql="""CREATE TABLE IF NOT EXISTS andares(
           andar text PRIMARY KEY
           );"""

    try:
        cur = con.cursor()
        cur.execute(sql)
    except Error as e:
        print(e)

    return

def createSetor():
    sql="""CREATE TABLE IF NOT EXISTS setores(
           andar text NOT NUll,
           setor text NOT NULL,
           FOREIGN KEY(andar) REFERENCES andares(andar));"""

    try:
        cur = con.cursor()
        cur.execute(sql)
    except Error as e:
        print(e)

    return

def createFabri():
    sql="""CREATE TABLE IF NOT EXISTS fabricantes(
           empresa text PRIMARY KEY,
           contato text NOT NULL,
           contato2 text,
           email text,
           adress text,
           cnpj text,
           autorizada1 text,
           contatoaut1 text,
           autorizada2 text,
           contatoaut2 text,
           autorizada3 text,
           contatoaut3 text);"""

    try:
        cur = con.cursor()
        cur.execute(sql)
    except Error as e:
        print(e)

    return

def createTreinados():
    sql="""CREATE TABLE IF NOT EXISTS treinados(
           nometec text NOT NULL,
           modelo text NOT NULL,
           data_trein text NOT NULL,
           turno text NOT NULL,
           img BLOB);"""

    try:
        cur = con.cursor()
        cur.execute(sql)
    except Error as e:
        print(e)

    return

def createTempCalibrPrev():
    sql="""CREATE TABLE IF NOT EXISTS tempos(
           tipo text NOT NULL,
           nometec text NOT NULL,
           modelo text NOT NULL,
           data_mod text NOT NULL,
           antigo_calibr text NOT NULL,
           novo_calibr text NOT NULL,
           antigo_prev text NOT NULL,
           novo_prev text NOT NULL,
           logado text NOT NULL);"""

    try:
        cur = con.cursor()
        cur.execute(sql)
    except Error as e:
        print(e)

    return

#----------------------------------------------------------------------------------------------------------------------------
def cadastrarXesque(Dale):
    sql = "INSERT INTO xesque(dale) VALUES(?)"
    dados = (Dale,)
    if Dale == "":
        raise
    cur = con.cursor()
    cur.execute(sql,dados)
    con.commit()
    return

def atualizarXesque(dale):
    cur.execute("""UPDATE xesque
                SET dale = ?""",(dale, ))
    con.commit()
    
    return

def ODale():
    cur.execute("SELECT * FROM xesque")
    r1=cur.fetchall()
    return r1[0][0]

def cadastrarEquip(Tipo,NomeTec,Modelo,Fabri,Nota_Fisc,NumSerie,Patri,NumAnvisa,Acessorios,Insumos,Data_Recebimento,Data_Aceitacao,Data_Inst,Data_Funcionamento,Data_Fabri,Temp_calibr,Temp_Prevent,Andar_Ins,Setor_Ins,Local_Ins,Obs):
   sql = "INSERT INTO equipamentos(situacao,tipo,nometec,modelo,fabricante,nota_fisc,numserie,patri,numanvisa,acessorios,insumos,data_recebimento,data_aceitação,data_instalação,data_funcionamento,data_fabricação,data_desativ,temp_calibracao,temp_preventiva,andar_ins,setor_ins,local_ins,andar_atual,setor_atual,local_atual,treinamento,obs,logado) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
   cur = con.cursor()
   if NumSerie == 'Digite o N°':
       NumSerie = 'Ilegível'
   if NumSerie == 'Ilegível' and Patri == 'Branco':
       raise
   if NumSerie == '' or Patri == '':
       raise
   if NumSerie == 'Ilegível':
       cur.execute("SELECT numserie FROM equipamentos")
       r2=cur.fetchall()
       r3=[]
       r4=[]
       cont=int(0)
       for i in r2:
           r3.append(i[0].split(" "))
       for i in r3:
           r4.append(i[0])
       for i in r4:
           if i=='Ilegível':
               cont+=1
       if cont != 0:
           NumSerie = NumSerie+f" {cont}"
       elif cont == 0:
           NumSerie = NumSerie
   elif NumSerie != 'Ilegível':
       pass
           
   cur.execute("SELECT patri FROM equipamentos")
   r1=cur.fetchall()
   if Patri == 'Branco':
       r5=[]
       r6=[]
       cont1=int(0)
       for i in r1:
           r5.append(i[0].split(" "))
       for i in r5:
           r6.append(i[0])
       for i in r6:
           if i=='Branco':
               cont1+=1
       if cont1 != 0:
           Patri = Patri+f" {cont1}"
       elif cont1 == 0:
           Patri = Patri
   elif Patri!='Branco':
       pass

   r7=[]
   r8=[]
   cont2=int(0)
   for j in r1:
       if j[0]==Patri and Tipo=='Equipamento':
           raise
       elif j[0]==Patri and Tipo=='Acessório':
           for i in r1:
               r7.append(i[0].split("-"))
           for i in r7:
               r8.append(i[0])
           for i in r8:
               if i==Patri:
                   cont2+=1
   if cont2 != 0:
       Patri = Patri+f"-{cont2}"
   elif cont2 == 0:
       Patri = Patri

   try:
       datetime.strptime(Data_Inst,"%d-%m-%Y")
       datetime.strptime(Data_Aceitacao,"%d-%m-%Y")
       dt=datetime.strptime(Data_Recebimento,"%d-%m-%Y")
       dt1=datetime.now() - dt
       dt3 = float(dt1.days)
       if dt3 < 0:
           raise
   except:
       raise
   try:
       dt=datetime.strptime(Data_Funcionamento,"%d-%m-%Y")
       dt1=datetime.now() - dt
       dt4 = float(dt1.days)
       if dt4 < 0:
           raise
       if dt3 < dt4:
           raise
   except:
       raise
   if Temp_calibr=='' or Temp_calibr=='Em Meses!' or Temp_calibr==0:
       Temp_calibr = 2000
   if Temp_Prevent=='' or Temp_Prevent=='Em Meses!' or Temp_Prevent==0:
       Temp_Prevent = 2000
   if  NomeTec== '' or Modelo== '' or Fabri== '' or NumSerie== '' or Data_Aceitacao== '' or Data_Funcionamento== '' or Andar_Ins== ''or Setor_Ins== '':
       raise
    
   dados =('Ativo',Tipo,NomeTec,Modelo,Fabri,Nota_Fisc,NumSerie,Patri,NumAnvisa,Acessorios,Insumos,Data_Recebimento,Data_Aceitacao,Data_Inst,Data_Funcionamento,Data_Fabri,'',Temp_calibr,Temp_Prevent,Andar_Ins,Setor_Ins,Local_Ins,Andar_Ins,Setor_Ins,Local_Ins,'Não',Obs,logado[0])
   cur.execute(sql,dados)
   con.commit()
   return

#cadastrarEquip('Equipamento','Monitor','A','GlobalTech','0012','1122','Branco','0','','','20-05-2020','20-05-2020','20-05-2020','20-05-2020','12','12','1° Andar','UTI Adulto','leit1','daniel','')
#cadastrarEquip('Equipamento','Monitor','002','GlobalTech','0012','11','HM11','0','','','20-05-2020','20-05-2020','20-05-2020','20-05-2020','12','12','1° Andar','UTI Adulto','leit1','daniel','')
#cadastrarEquip('Equipamento','Monitor','002','GlobalTech','0012','12','HM12','0','','','20-05-2020','20-05-2020','20-05-2020','20-05-2020','12','12','1° Andar','UTI Adulto','leit1','daniel','')
#cadastrarEquip('Equipamento','Monitor','002','GlobalTech','0012','13','HM13','0','','','20-05-2020','20-05-2020','20-05-2020','20-05-2020','12','12','1° Andar','UTI Adulto','leit1','daniel','')

#cadastrarEquip('Acessório','Fonte','001','GlobalTech','0012','10','HM1','0','','','20-05-2020','20-05-2020','20-05-2020','20-05-2020','12','12','1° Andar','UTI Adulto','leito1','daniel','')
#cadastrarEquip('Equipamento','Bomba','001','GlobalTech','0012','3','HM1','0','','','20-05-2020','20-05-2020','20-05-2020','20-05-2020','12','12','1° Andar','UTI Adulto','leito1','daniel','')
#cadastrarEquip('Equipamento','Monitor','001','GlobalTech','0012','4','','0','','','20-05-2020','20-05-2020','20-05-2020','20-05-2020','12','12','1° Andar','UTI Adulto','leito1','daniel','')
#cadastrarEquip('Equipamento','Monitor','001','GlobalTech','0012','5','','0','','','20-05-2020','20-05-2020','20-05-2020','20-05-2020','12','12','1° Andar','UTI Adulto','leito1','daniel','')



def cadastrar(Nome,Usuario,Senha,ConSenha,RF):
   sql = "INSERT INTO cadastros(nome,usuario,senha,consenha,rf)VALUES(?,?,?,?,?)"
   dados =(Nome,Usuario,Senha,ConSenha,RF)
   if Nome  == '' or Usuario == ''  or Senha == '' or ConSenha == '' or RF == '':
       raise
   if Senha != ConSenha:
       raise
   elif Senha == ConSenha:
       cur = con.cursor()
       cur.execute(sql,dados)
       con.commit()
   return

def cadastrarEquipDes(NomeTec,Modelo,Desenv,NumRegistro,Acessorios,Insumos,Data_Entrada,Andar_Ins,Setor_Ins,Local_Ins,Treinamento,Responsavel,Obs):
   sql = "INSERT INTO equip_desenv(situacao,nometec,modelo,desenvolvedor,num_registro,acessorios,insumos,data_entrada,data_desativ,andar_ins,setor_ins,local_ins,treinamento,responsavel,obs,logado) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
   dados =('Ativo',NomeTec,Modelo,Desenv,NumRegistro,Acessorios,Insumos,Data_Entrada,'',Andar_Ins,Setor_Ins,Local_Ins,Treinamento,Responsavel,Obs,logado[0])
   try:
       dt=datetime.strptime(Data_Entrada,"%d-%m-%Y")
       dt1=datetime.now() - dt
       dt3 = float(dt1.days)
       if dt3 < 0:
           raise
   except:
       raise
   if NomeTec == '' or Modelo == '' or Desenv =='' or NumRegistro =='' or Setor_Ins =='' or Responsavel == '':
       raise
   cur = con.cursor()
   cur.execute(sql,dados)
   con.commit()
   return

def cadastrarCalibracao(Patri,NumSerie,Data_Retirada,Acessorios_ret,andar_retirado, setor_retirado, local_retirado,Empresa_resp,Tecnico,Ord_serv,Enferm_resp,Obs):
    sql = ("INSERT INTO calibracao(tipo,patri,numserie,data_retirada,acessorios_retirados,andar_retirado, setor_retirado, local_retirado,empresa_resp,tecnico,ord_serv,enferm_resp,obs,logado) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)")
    cur = con.cursor()
    try:
       dt=datetime.strptime(Data_Retirada,"%d-%m-%Y")
       dt1=datetime.now() - dt
       dt3 = float(dt1.days)
       if dt3 < 0:
           raise
    except:
        raise
    if Patri=='' and NumSerie=='':
        raise
    if andar_retirado ==''  or setor_retirado =='' or Empresa_resp=='' or Tecnico=='' or Ord_serv=='' or Enferm_resp =='':
        raise
    cur.execute("""SELECT situacao FROM equipamentos WHERE numserie = ? OR patri = ? """,(NumSerie,Patri, ))
    r1=cur.fetchall()
    if r1[0][0] == 'Ativo':
        cur.execute("SELECT numserie FROM equipamentos WHERE patri=?",(Patri, ))
        r4=cur.fetchall()
        cur.execute("SELECT patri FROM equipamentos WHERE numserie=?",(NumSerie, ))
        r2=cur.fetchall()

        if Patri != '' and NumSerie != '':
            if Patri == r2[0][0] and NumSerie == r4[0][0]:
                pass
            elif Patri != r2[0][0] and NumSerie != r4[0][0]:
                raise

        if Patri!='':
            NumSerie = r4[0][0]
        elif NumSerie!='':
            Patri = r2[0][0]
            
        dados = ('Calibração',Patri,NumSerie,Data_Retirada,Acessorios_ret,andar_retirado, setor_retirado, local_retirado,Empresa_resp,Tecnico,Ord_serv,Enferm_resp,Obs,logado[0])
        cur.execute(sql,dados)

        cur.execute("""UPDATE equipamentos
                    SET andar_atual = 'Em Calibração!'
                    WHERE equipamentos.numserie = ?""",(NumSerie, ))
        cur.execute("""UPDATE equipamentos
                    SET setor_atual = 'Em Calibração!'
                    WHERE equipamentos.numserie = ?""",(NumSerie, ))
        cur.execute("""UPDATE equipamentos
                    SET local_atual = 'Em Calibração!'
                    WHERE equipamentos.numserie = ?""",(NumSerie, ))
        
        con.commit()
    else:
        raise('Equipamento Desativado')
    return
#cadastrarCalibracao('HM10','10','25-06-2021','','1° Andar','UTI Adulto','','GlobalTech','erik','12312312','paula','')
def cadastrarPreventiva(Patri,NumSerie,Data_Retirada,Acessorios_ret,andar_retirado, setor_retirado, local_retirado,Empresa_resp,Tecnico,Ord_serv,Enferm_resp,Obs):
    sql = ("INSERT INTO preventiva(tipo,patri,numserie,data_retirada,acessorios_retirados,andar_retirado, setor_retirado, local_retirado,empresa_resp,tecnico,ord_serv,enferm_resp,obs,logado) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)")
    cur = con.cursor()
    try:
       dt=datetime.strptime(Data_Retirada,"%d-%m-%Y")
       dt1=datetime.now() - dt
       dt3 = float(dt1.days)
       if dt3 < 0:
           raise
    except:
        raise
    if Patri=='' and NumSerie=='':
        raise
    if andar_retirado ==''  or setor_retirado =='' or Empresa_resp=='' or Tecnico=='' or Ord_serv=='' or Enferm_resp =='':
        raise
    cur.execute("""SELECT situacao FROM equipamentos WHERE numserie = ? OR patri = ? """,(NumSerie,Patri, ))
    r1=cur.fetchall()
    if r1[0][0] == 'Ativo':
        cur.execute("SELECT numserie FROM equipamentos WHERE patri=?",(Patri, ))
        r4=cur.fetchall()
        cur.execute("SELECT patri FROM equipamentos WHERE numserie=?",(NumSerie, ))
        r2=cur.fetchall()

        if Patri != '' and NumSerie != '':
            if Patri == r2[0][0] and NumSerie == r4[0][0]:
                pass
            elif Patri != r2[0][0] and NumSerie != r4[0][0]:
                raise

        if Patri!='':
            NumSerie = r4[0][0]
        elif NumSerie!='':
            Patri = r2[0][0]
            
        dados = ('Preventiva',Patri,NumSerie,Data_Retirada,Acessorios_ret,andar_retirado, setor_retirado, local_retirado,Empresa_resp,Tecnico,Ord_serv,Enferm_resp,Obs,logado[0])
        cur.execute(sql,dados)

        cur.execute("""UPDATE equipamentos
                    SET andar_atual = 'Em Preventiva!'
                    WHERE equipamentos.numserie = ?""",(NumSerie, ))
        cur.execute("""UPDATE equipamentos
                    SET setor_atual = 'Em Preventiva!'
                    WHERE equipamentos.numserie = ?""",(NumSerie, ))
        cur.execute("""UPDATE equipamentos
                    SET local_atual = 'Em Preventiva!'
                    WHERE equipamentos.numserie = ?""",(NumSerie, ))

        con.commit()
    else:
        raise('Equipamento Desativado')
    return

def cadastrarEsporadica(Patri,NumSerie,Data_Retirada,Prob_Relatado,Acessorios_ret,andar_retirado, setor_retirado, local_retirado,Empresa_resp,Tecnico,Ord_serv,Enferm_resp,Obs):
    sql = ("INSERT INTO esporadica(tipo,patri,numserie,data_retirada,prob_relatado,acessorios_retirados,andar_retirado, setor_retirado, local_retirado,empresa_resp,tecnico,ord_serv,enferm_resp,obs,logado) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)")
    cur = con.cursor()
    try:
       dt=datetime.strptime(Data_Retirada,"%d-%m-%Y")
       dt1=datetime.now() - dt
       dt3 = float(dt1.days)
       if dt3 < 0:
           raise
    except:
        raise
    if Patri=='' and NumSerie=='':
        raise
    if andar_retirado ==''  or setor_retirado =='' or Empresa_resp=='' or Tecnico=='' or Ord_serv=='' or Enferm_resp =='':
        raise
    cur.execute("""SELECT situacao FROM equipamentos WHERE numserie = ? OR patri = ? """,(NumSerie,Patri, ))
    r1=cur.fetchall()
    if r1[0][0] == 'Ativo':
        cur.execute("SELECT numserie FROM equipamentos WHERE patri=?",(Patri, ))
        r4=cur.fetchall()
        cur.execute("SELECT patri FROM equipamentos WHERE numserie=?",(NumSerie, ))
        r2=cur.fetchall()

        if Patri != '' and NumSerie != '':
            if Patri == r2[0][0] and NumSerie == r4[0][0]:
                pass
            elif Patri != r2[0][0] and NumSerie != r4[0][0]:
                raise

        if Patri!='':
            NumSerie = r4[0][0]
        elif NumSerie!='':
            Patri = r2[0][0]
            
        dados = ('Manutenção Esporádica',Patri,NumSerie,Data_Retirada,Prob_Relatado,Acessorios_ret,andar_retirado, setor_retirado, local_retirado,Empresa_resp,Tecnico,Ord_serv,Enferm_resp,Obs,logado[0])
        cur.execute(sql,dados)

        cur.execute("""UPDATE equipamentos
                    SET andar_atual = 'Em Manutenção Esporádica!'
                    WHERE equipamentos.numserie = ?""",(NumSerie, ))
        cur.execute("""UPDATE equipamentos
                    SET setor_atual = 'Em Manutenção Esporádica!'
                    WHERE equipamentos.numserie = ?""",(NumSerie, ))
        cur.execute("""UPDATE equipamentos
                    SET local_atual = 'Em Manutenção Esporádica!'
                    WHERE equipamentos.numserie = ?""",(NumSerie, ))
        
        con.commit()
    else:
        raise('Equipamento Desativado')
    return

def cadastrarReentrada(Patri,NumSerie,Data_reentrada,Motivo,Pecas_Trocadas,Andar_Dest,Setor_Dest,Local_Dest,Responsavel,Obs):
    sql = ("INSERT INTO reentrada(tipo,patri,numserie,data_reentrada,motivo,peças_trocadas,andar_dest,setor_dest,local_dest,responsavel,obs,logado) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)")
    cur = con.cursor()
    try:
       dt=datetime.strptime(Data_reentrada,"%d-%m-%Y")
       dt1=datetime.now() - dt
       dt3 = float(dt1.days)
       if dt3 < 0:
           raise
    except:
        raise
    if Patri=='' and NumSerie=='':
        raise
    if Data_reentrada ==''  or Motivo =='' or Andar_Dest=='' or Setor_Dest=='' or Responsavel=='':
        raise
    cur.execute("""SELECT situacao FROM equipamentos WHERE numserie = ? OR patri = ? """,(NumSerie,Patri, ))
    r1=cur.fetchall()
    if r1[0][0] == 'Ativo':
        cur.execute("SELECT numserie FROM equipamentos WHERE patri=?",(Patri, ))
        r4=cur.fetchall()
        cur.execute("SELECT patri FROM equipamentos WHERE numserie=?",(NumSerie, ))
        r2=cur.fetchall()

        if Patri != '' and NumSerie != '':
            if Patri == r2[0][0] and NumSerie == r4[0][0]:
                pass
            elif Patri != r2[0][0] and NumSerie != r4[0][0]:
                raise

        if Patri!='':
            NumSerie = r4[0][0]
        elif NumSerie!='':
            Patri = r2[0][0]
            
        dados = ('Retorno',Patri,NumSerie,Data_reentrada,Motivo,Pecas_Trocadas,Andar_Dest,Setor_Dest,Local_Dest,Responsavel,Obs,logado[0])
        cur.execute(sql,dados)

        cur.execute("""UPDATE equipamentos
                    SET andar_atual = ?
                    WHERE equipamentos.numserie = ?""",(Andar_Dest,NumSerie, ))
        cur.execute("""UPDATE equipamentos
                    SET setor_atual = ?
                    WHERE equipamentos.numserie = ?""",(Setor_Dest,NumSerie, ))
        cur.execute("""UPDATE equipamentos
                    SET local_atual = ?
                    WHERE equipamentos.numserie = ?""",(Local_Dest,NumSerie, ))
        
        con.commit()
    else:
        raise('Equipamento Desativado')
    return

def cadastrarMovimentacao(Patri,NumSerie,Data_Mov,Andar_Dest,Setor_Dest,Local_Dest,Acessorios,Ord_Serv,Obs):
    cur = con.cursor()
    sql = ("INSERT INTO movimentacao(tipo,patri,numserie,data_mov,andar_org,setor_org,local_org,andar_dest,setor_dest,local_dest,acessorios,ord_serv,obs,logado) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)")
    try:
       dt=datetime.strptime(Data_Mov,"%d-%m-%Y")
       dt1=datetime.now() - dt
       dt3 = float(dt1.days)
       if dt3 < 0:
           raise
    except:
       raise
    if Patri=='' and NumSerie=='':
        raise
    if  Data_Mov== '' or Andar_Dest== '' or Setor_Dest== '' or Ord_Serv== '' :
      raise
    cur.execute("""SELECT situacao FROM equipamentos WHERE numserie = ? OR patri = ? """,(NumSerie,Patri, ))
    r1=cur.fetchall()
    if r1[0][0] == 'Ativo':
        cur.execute("SELECT numserie FROM equipamentos WHERE patri=?",(Patri, ))
        r4=cur.fetchall()
        cur.execute("SELECT patri FROM equipamentos WHERE numserie=?",(NumSerie, ))
        r2=cur.fetchall()

        if Patri != '' and NumSerie != '':
            if Patri == r2[0][0] and NumSerie == r4[0][0]:
                pass
            elif Patri != r2[0][0] and NumSerie != r4[0][0]:
                raise

        if Patri!='':
            NumSerie = r4[0][0]
        elif NumSerie!='':
            Patri = r2[0][0]

        cur.execute("""SELECT andar_atual,setor_atual,local_atual FROM equipamentos WHERE numserie=? """,(NumSerie, ))
        r5=cur.fetchall()
        Andar_Org=r5[0][0]
        Setor_Org=r5[0][1]
        Local_Org=r5[0][2]

        dados = ("Movimentação",Patri,NumSerie,Data_Mov,Andar_Org,Setor_Org,Local_Org,Andar_Dest,Setor_Dest,Local_Dest,Acessorios,Ord_Serv,Obs,logado[0])
        cur.execute(sql,dados)
        
        cur.execute("""UPDATE equipamentos
                    SET andar_atual = ?
                    WHERE equipamentos.numserie = ?""",(Andar_Dest,NumSerie, ))
        cur.execute("""UPDATE equipamentos
                    SET setor_atual = ?
                    WHERE equipamentos.numserie = ?""",(Setor_Dest,NumSerie, ))
        cur.execute("""UPDATE equipamentos
                    SET local_atual = ?
                    WHERE equipamentos.numserie = ?""",(Local_Dest,NumSerie, ))
        
        con.commit()
    else:
        raise('Equipamento Desativado')
    return

def procisso(NumSerie,Patri):
    if NumSerie == '' and Patri == '':
        raise
    else:
        cur.execute("""SELECT situacao FROM equipamentos WHERE numserie = ? OR patri = ? """,(NumSerie,Patri, ))
        r1=cur.fetchall()
        if r1[0][0] == 'Ativo':
            cur.execute("SELECT numserie FROM equipamentos WHERE patri=?",(Patri, ))
            r4=cur.fetchall()
            cur.execute("SELECT patri FROM equipamentos WHERE numserie=?",(NumSerie, ))
            r2=cur.fetchall()

            if Patri != '' and NumSerie != '':
                if Patri == r2[0][0] and NumSerie == r4[0][0]:
                    pass
                elif Patri != r2[0][0] and NumSerie != r4[0][0]:
                    raise

            if Patri!='':
                NumSerie = r4[0][0]
            elif NumSerie!='':
                Patri = r2[0][0]

            cur.execute("""SELECT andar_atual,setor_atual,local_atual FROM equipamentos WHERE numserie=? """,(NumSerie, ))
            r5=cur.fetchall()
    return r5

def cadastrarDesativacao(Patri,NumSerie,Data_Desativ,Motivo_Desativ,Num_Processo,Obs,Carta):
    sql = ("INSERT INTO desativacao(tipo,patri,NumSerie,data_desativ,motivo_desativ,num_processo,obs,logado,carta_desc) VALUES(?,?,?,?,?,?,?,?,?)")
    if Carta != '':
        CartaConvert = convertToBinaryData(Carta)
    else:
        CartaConvert = Carta
    dados = ('Desativação',Patri,NumSerie,Data_Desativ,Motivo_Desativ,Num_Processo,Obs,logado[0],CartaConvert)
    cur = con.cursor()
    try:
       dt=datetime.strptime(Data_Desativ,"%d-%m-%Y")
       dt1=datetime.now() - dt
       dt3 = float(dt1.days)
       if dt3 < 0:
           raise
    except:
        raise
    if  Patri== '' or NumSerie == '' or Data_Desativ== '' or Motivo_Desativ== '' or Num_Processo== '':
        raise
    cur.execute("""SELECT situacao FROM equipamentos WHERE numserie = ? OR patri = ? """,(NumSerie,Patri, ))
    r1=cur.fetchall()
    if r1[0][0] == 'Ativo':
        cur.execute("""UPDATE equipamentos
                             SET situacao ='Desativado'
                             WHERE equipamentos.patri=?""",(Patri, ))
        cur.execute("""UPDATE equipamentos
                             SET data_desativ = ?
                             WHERE equipamentos.patri=?""",(Data_Desativ,Patri, ))
        cur.execute(sql,dados)
        cur.execute("""UPDATE equipamentos
                    SET andar_atual = 'Desativado'
                    WHERE equipamentos.numserie = ?""",(Patri, ))
        cur.execute("""UPDATE equipamentos
                    SET setor_atual = 'Desativado'
                    WHERE equipamentos.numserie = ?""",(Patri, ))
        cur.execute("""UPDATE equipamentos
                    SET local_atual = 'Desativado'
                    WHERE equipamentos.numserie = ?""",(Patri, ))
        con.commit()
    else:
        raise('Equipamento Desativado')
    return

def cadastrarDesativacaoDes(Num_Registro,Data_Desativ,Motivo_Desativ,NumProcesso,Obs,Carta):
    sql = ("INSERT INTO desativacao_des(tipo,num_registro,data_desativ,motivo_desativ,num_processo,obs,logado,carta_desc) VALUES(?,?,?,?,?,?,?,?)")
    if Carta != '':
        CartaConvert = convertToBinaryData(Carta)
    else:
        CartaConvert = Carta
    dados = ('Desativação',Num_Registro,Data_Desativ,Motivo_Desativ,NumProcesso,Obs,logado[0],CartaConvert)
    cur = con.cursor()
    try:
       dt=datetime.strptime(Data_Desativ,"%d-%m-%Y")
       dt1=datetime.now() - dt
       dt3 = float(dt1.days)
       if dt3 < 0:
           raise
    except:
        raise
    if  Num_Registro == '' or Data_Desativ== '' or Motivo_Desativ== '' or NumProcesso== '':
        raise
    cur.execute("""UPDATE equip_desenv
                         SET situacao ='Desativado'
                         WHERE equip_desenv.num_registro=?""",(Num_Registro, ))
    cur.execute("""UPDATE equip_desenv
                         SET data_desativ = ?
                         WHERE equip_desenv.num_registro=?""",(Data_Desativ,Num_Registro, ))
    cur.execute(sql,dados)
    con.commit()
    return

def cadastrarTreinados(Nometec,Modelo,Data_Trein,Turno,Img):
    cur = con.cursor()
    sql = ("INSERT INTO treinados(nometec,modelo,data_trein,turno,img) VALUES(?,?,?,?,?)")
    ImgConvert = convertToBinaryData(Img)
    dados=(Nometec,Modelo,Data_Trein,Turno,ImgConvert)
    cur.execute(""" SELECT nometec,modelo,data_trein,turno FROM treinados WHERE nometec=? AND modelo=?""",(Nometec,Modelo, ))
    r1=cur.fetchall()
    for i in r1:
        if i[0]==Nometec and i[1]==Modelo and i[2]==Data_Trein and i[3]==Turno:
            raise
    cur.execute(sql,dados)
    cur.execute("""UPDATE equipamentos
                         SET treinamento ='Sim'
                         WHERE nometec=? AND modelo=?""",(Nometec,Modelo, ))
    con.commit()
    return

def cadastrarTempCalibrPrev(Nometec,Modelo,Data_Mod,Antigo_Calibr,Novo_Calibr,Antigo_Prev,Novo_Prev):
    sql=("INSERT INTO tempos(tipo,nometec,modelo,data_mod,antigo_calibr,novo_calibr,antigo_prev,novo_prev,logado)VALUES(?,?,?,?,?,?,?,?,?)")
    dados = ('Alteração de Intervalos',Nometec,Modelo,Data_Mod,Antigo_Calibr,Novo_Calibr,Antigo_Prev,Novo_Prev,logado[0])
    cur=con.cursor()
    try:
       dt=datetime.strptime(Data_Mod,"%d-%m-%Y")
       dt1=datetime.now() - dt
       dt3 = float(dt1.days)
       if dt3 < 0:
           raise
    except:
        raise
    if Nometec == '' or Modelo=='' or Data_Mod=='':
        raise
    if Novo_Calibr == '':
        Novo_Calibr = 2000
    if Novo_Prev == '':
        Novo_Prev = 2000
    cur.execute("""UPDATE equipamentos
                         SET temp_calibracao =?
                         WHERE equipamentos.nometec=? AND equipamentos.modelo=?""",(Novo_Calibr,Nometec,Modelo, ))
    cur.execute("""UPDATE equipamentos
                         SET temp_preventiva = ?
                         WHERE equipamentos.nometec=? AND equipamentos.modelo=?""",(Novo_Prev,Nometec,Modelo, ))
    cur.execute(sql,dados)
    con.commit()
    return

createTempCalibrPrev()
#cadastrarTempCalibrPrev('Monitor','A','25-06-2021','',24,'',24)

def login(RF,Senha):
    cur.execute("SELECT senha FROM cadastros WHERE rf = ?",(RF, ))
    r1 = cur.fetchall()
    if Senha == r1[0][0]:
        pass
    else:
        raise
    cur.execute("SELECT nome FROM cadastros WHERE rf =  ?",(RF, ))
    r2 =  cur.fetchall()
    r3=[]
    for i in r2:
        r3.append(i[0])
    return r3

def ForgotPassword(Usuario,NovaSenha,ConNovaSenha,RF):
    if Usuario == ''  or NovaSenha == '' or ConNovaSenha=='' or RF == '' or NovaSenha!= ConNovaSenha:
        raise
    else:
        cur.execute("SELECT senha  FROM cadastros WHERE rf = ? AND usuario = ?",(RF,Usuario, ))
        r1=cur.fetchall()
        cur.execute("""UPDATE cadastros SET senha = ?,consenha = ?
                    WHERE rf = ? AND usuario = ?""",(NovaSenha,ConNovaSenha,RF,Usuario, ))
        con.commit()
        cur.execute("SELECT senha  FROM cadastros WHERE rf = ? AND usuario = ?",(RF,Usuario, ))
        r2=cur.fetchall()
        
    if r1 == r2:
        raise
    return

def AlterarFabri(Empresa,Contato,Contato2,Email,Adress,CNPJ,Aut1,CtAt1,Aut2,CtAt2,Aut3,CtAt3):
    cur=con.cursor()
    if Contato!='':
        cur.execute("""UPDATE fabricantes
                       SET contato = ?
                       WHERE empresa = ?""",(Contato,Empresa, ))
    if Contato2!='':
        cur.execute("""UPDATE fabricantes
                       SET contato2 = ?
                       WHERE empresa = ?""",(Contato2,Empresa, ))
    if Email!='':
        cur.execute("""UPDATE fabricantes
                       SET email = ?
                       WHERE empresa = ?""",(Email,Empresa, ))
    if Adress!='':
        cur.execute("""UPDATE fabricantes
                       SET adress = ?
                       WHERE empresa = ?""",(Adress,Empresa, ))
    if CNPJ!='':
        cur.execute("""UPDATE fabricantes
                       SET cnpj = ?
                       WHERE empresa = ?""",(CNPJ,Empresa, ))
    if Aut1!='':
        cur.execute("""UPDATE fabricantes
                       SET autorizada1 = ?
                       WHERE empresa = ?""",(Aut1,Empresa, ))
    if CtAt1!='':
        cur.execute("""UPDATE fabricantes
                       SET contatoaut1 = ?
                       WHERE empresa = ?""",(CtAt1,Empresa, ))
    if Aut2!='':
        cur.execute("""UPDATE fabricantes
                       SET autorizada2 = ?
                       WHERE empresa = ?""",(Aut2,Empresa, ))
    if CtAt2!='':
        cur.execute("""UPDATE fabricantes
                       SET contatoaut2 = ?
                       WHERE empresa = ?""",(CtAt2,Empresa, ))
    if Aut3!='':
        cur.execute("""UPDATE fabricantes
                       SET autorizada3 = ?
                       WHERE empresa = ?""",(Aut3,Empresa, ))
    if CtAt3!='':
        cur.execute("""UPDATE fabricantes
                       SET contatoaut3 = ?
                       WHERE empresa = ?""",(CtAt3,Empresa, ))
    con.commit()
    return

def importarExcel():
    cur.execute("DROP TABLE IF EXISTS CAMA")
    excel = load_workbook('CAMA.xlsx')
    plan1=excel['CAMA']

    for i in plan1:
        l1=i[0].value
        l2=i[1].value
        l3=i[2].value
        l4=i[3].value
        l5=i[4].value
        l6=i[5].value
        l7=i[6].value
        l8=i[7].value
        l9=i[8].value
        l10=i[9].value
        l11=i[10].value
        l12=i[11].value
        l13=i[12].value
        l14=i[13].value
        l15=i[14].value
        l16=i[15].value
        l17=i[16].value
        l18=i[17].value
        l19=i[18].value
        l20=i[19].value
        l21=i[20].value
        print(i)
        cadastrarEquip(l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18,l19,l20,l21)
    
#importarExcel()
       
def importarExcelPrev():
    cur.execute("DROP TABLE IF EXISTS CAMAPREV")
    excel = load_workbook('CAMAPREV.xlsx')
    plan1=excel['CAMAPREV']

    for i in plan1:
        l1=i[0].value
        l2=i[1].value
        l3=i[2].value
        l4=i[3].value
        l5=i[4].value
        l6=i[5].value
        l7=i[6].value
        l8=i[7].value
        l9=i[8].value
        l10=i[9].value
        l11=i[10].value
        l12=i[11].value
        print(i)
        cadastrarPreventiva('',l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12)
        
#importarExcelPrev()

def importarExcelPrev2():
    cur.execute("DROP TABLE IF EXISTS LOCADOPREV")
    excel = load_workbook('LOCADOPREV.xlsx')
    plan1=excel['LOCADOPREV']

    for i in plan1:
        l1=i[0].value
        l2=i[1].value
        l3=i[2].value
        l4=i[3].value
        l5=i[4].value
        l6=i[5].value
        l7=i[6].value
        l8=i[7].value
        l9=i[8].value
        l10=i[9].value
        l11=i[10].value
        l12=i[11].value
        print(i)
        cadastrarPreventiva('',l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12)
        
#importarExcelPrev2()
        
def importarExcelCali():
    cur.execute("DROP TABLE IF EXISTS LOCADOCALI")
    excel = load_workbook('LOCADOCALI.xlsx')
    plan1=excel['LOCADOCALI']

    for i in plan1:
        l1=i[0].value
        l2=i[1].value
        l3=i[2].value
        l4=i[3].value
        l5=i[4].value
        l6=i[5].value
        l7=i[6].value
        l8=i[7].value
        l9=i[8].value
        l10=i[9].value
        l11=i[10].value
        l12=i[11].value
        print(i)
        cadastrarCalibracao('',l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12)
#importarExcelCali()

def importarExcelCali2():
    cur.execute("DROP TABLE IF EXISTS CALI2")
    excel = load_workbook('CALI2.xlsx')
    plan1=excel['CALI2']

    for i in plan1:
        l1=i[0].value
        l2=i[1].value
        l3=i[2].value
        l4=i[3].value
        l5=i[4].value
        l6=i[5].value
        l7=i[6].value
        l8=i[7].value
        l9=i[8].value
        l10=i[9].value
        l11=i[10].value
        l12=i[11].value
        print(i)
        cadastrarCalibracao(l1,'',l3,l4,l5,l6,l7,l8,l9,l10,l11,l12)
#importarExcelCali2()
        
def convertToBinaryData(filename):
    with open(filename,'rb') as file:
        blobData = file.read()
    return blobData


def writeTofile(data,filename):
    with open(filename, 'wb') as file:
        file.write(data)

def exibirFotos(x,y,z,a):
    cur = con.cursor()
    cur.execute("SELECT * FROM treinados WHERE nometec=? AND modelo=? AND data_trein=? AND turno=? ",(x,y,z,a ))
    r1=cur.fetchall()
    for i in r1:
        name = i[0]
        name1 = i[1]
        name2=i[2]
        name3=i[3]
        photo = i[4]
     
    photoPath = r"Imagem\\" + name + name1 +"_"+ name2 +"_"+ name3 +"_treinados.PNG"
    writeTofile(photo,photoPath)
    return photoPath

def exibirTreinados(x,y):
    cur.execute("SELECT nometec,modelo,data_trein,turno FROM treinados WHERE nometec=? AND modelo=?",(x,y, ))
    r1=cur.fetchall()
    r2=[]
    r3=[]
    r4=[]
    for i in r1:
        r2.append(i)
        r3.append(i[2])
    r3.sort(key=lambda date: datetime.strptime(date, "%d-%m-%Y"))
    for i in r3:
        for j in r2:
            if i==j[2] and j not in r4:
                r4.append(j)
    r4.reverse()
    return r4
    
def exibirFotosDesativ(x):
    cur = con.cursor()
    cur.execute("SELECT * FROM desativacao WHERE numserie = ? OR patri = ?",(x,x, ))
    r1=cur.fetchall()
    for i in r1:
        name = i[2]
        photo = i[8]
    
    photoPath = r"Imagem\\" + name + "_Carta_Descontinuidade.png"
    writeTofile(photo,photoPath)
    return photoPath

def exibirFotosDesativDes(x):
    cur = con.cursor()
    cur.execute("SELECT * FROM desativacao_des WHERE num_registro=?",(x, ))
    r1=cur.fetchall()
    for i in r1:
        name = i[1]
        photo = i[7]
    
    photoPath = r"Imagem\\" + name + "_Carta_Descontinuidade.png"
    writeTofile(photo,photoPath)
    return photoPath

def cadastrarAndar(Andar):
    sql = ("INSERT INTO andares(andar) VALUES(?)")
    dados = (Andar,)
    
    if Andar == '':
        raise
    cur = con.cursor()
    cur.execute(sql,dados)
    con.commit()
    return

#cadastrarAndar('SUBSOLO')
#cadastrarAndar('TÉRREO')
#cadastrarAndar('1º ANDAR')
#cadastrarAndar('2º ANDAR')
#cadastrarAndar('3º ANDAR')
#cadastrarAndar('4º ANDAR')
#cadastrarAndar('5º ANDAR')
#cadastrarAndar('6º ANDAR')
#cadastrarAndar('7º ANDAR')
#cadastrarAndar('8º ANDAR')
#cadastrarAndar('9º ANDAR')
#cadastrarAndar('10º ANDAR')
#cadastrarAndar('ANEXO')
#cadastrarAndar('EXTERNO')

def cadastrarSetor(Andar,Setor):
    sql = ("INSERT INTO setores(andar,setor) VALUES(?,?)")
    dados = (Andar,Setor)
    
    if Andar == '' or Setor == '':
        raise
    cur = con.cursor()
    cur.execute(sql,dados)
    con.commit()
    return

def cadastrarFabri(Fabricante,Contato,Contato2,Email,Adress,CNPJ,Autorizada,CtAutorizada,Autorizada2,Ct2Autorizada,Autorizada3,Ct3Autorizada):
    sql = ("INSERT INTO fabricantes(empresa,contato,contato2,email,adress,cnpj,autorizada1,contatoaut1,autorizada2,contatoaut2,autorizada3,contatoaut3) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)")
    dados = (Fabricante,Contato,Contato2,Email,Adress,CNPJ,Autorizada,CtAutorizada,Autorizada2,Ct2Autorizada,Autorizada3,Ct3Autorizada)
    
    if Fabricante == '' or Contato == '':
        raise
    cur = con.cursor()
    cur.execute(sql,dados)
    con.commit()
    return

def ProcNomeTec(x):
    cur.execute("""SELECT situacao,nometec,modelo,patri,numserie,andar_atual, setor_atual ,local_atual
                          FROM equipamentos
                          WHERE nometec = ?""",(x, ))
    r1=cur.fetchall()
    return r1

def ProcPatri(x):
    cur.execute("""SELECT *
                   FROM equipamentos
                   WHERE patri = ? OR numserie = ?""",(x,x, ))
    r1=cur.fetchall()
    cur.execute("SELECT * FROM equipamentos WHERE tipo='Acessório'")
    r2=cur.fetchall()
    r3=[]
    r5=[]
    r6=[]
    for i in r2:
        r3.append(i[7].split('-'))
    for i in r3:
        if i[0]==x:
            x1=i[0]+'-'+i[1]
            cur.execute("""SELECT *
                   FROM equipamentos
                   WHERE patri = ? OR numserie = ?""",(x1,x, ))
            r4=cur.fetchall()
            r1.append(r4[0])
    return r1

def ProcFabri(x):
    cur.execute("""SELECT situacao,fabricante,nometec,patri,numserie,andar_atual, setor_atual ,local_atual
                          FROM equipamentos
                          WHERE fabricante = ?""",(x, ))
    r1=cur.fetchall()
    return r1

def CalibrPatriNumSerie(x):
    cur.execute("""SELECT * FROM calibracao
                   WHERE patri = ? OR numserie = ?""",(x,x, ))
    r1=cur.fetchall()
    
    cur.execute("""SELECT * FROM reentrada
                   WHERE motivo='Calibração' AND patri = ? OR motivo='Calibração' AND numserie = ?""",(x,x, ))
    r2=cur.fetchall()
    r3=[]
    r4=[]
    r5=[]
    for i in r1:
        r3.append(i)
        r4.append(i[3])
    for i in r2:
        r3.append(i)
        r4.append(i[3])
    r4.sort(key=lambda date: datetime.strptime(date, "%d-%m-%Y"))
    for i in r4:
        for j in r3:
            if i==j[3] and j not in r5:
                r5.append(j)
    r5.reverse()
    return r5

def PrevPatriNumSerie(x):
    cur.execute("""SELECT * FROM preventiva
                   WHERE patri = ? OR numserie = ?""",(x,x, ))
    r1=cur.fetchall()
    
    cur.execute("""SELECT * FROM reentrada
                   WHERE motivo='Preventiva' AND patri = ? OR motivo='Preventiva' AND numserie = ?""",(x,x, ))
    r2=cur.fetchall()
    r3=[]
    r4=[]
    r5=[]
    for i in r1:
        r3.append(i)
        r4.append(i[3])
    for i in r2:
        r3.append(i)
        r4.append(i[3])
    r4.sort(key=lambda date: datetime.strptime(date, "%d-%m-%Y"))
    for i in r4:
        for j in r3:
            if i==j[3] and j not in r5:
                r5.append(j)
    r5.reverse()
    return r5

def EsporaPatriNumSerie(x):
    cur.execute("""SELECT * FROM esporadica
                   WHERE patri = ? OR numserie = ?""",(x,x, ))
    r1=cur.fetchall()
    
    cur.execute("""SELECT * FROM reentrada
                   WHERE motivo='Esporádica' AND patri = ? OR motivo='Esporádica' AND numserie = ?""",(x,x, ))
    r2=cur.fetchall()
    r3=[]
    r4=[]
    r5=[]
    for i in r1:
        r3.append(i)
        r4.append(i[3])
    for i in r2:
        r3.append(i)
        r4.append(i[3])
    r4.sort(key=lambda date: datetime.strptime(date, "%d-%m-%Y"))
    for i in r4:
        for j in r3:
            if i==j[3] and j not in r5:
                r5.append(j)
    r5.reverse()
    return r5

def MovPatriNumSerie(x):
    cur.execute("""SELECT * FROM movimentacao
                   WHERE patri = ? OR numserie = ?""",(x,x, ))
    r1=cur.fetchall()
    r3=[]
    r4=[]
    r5=[]
    for i in r1:
        r3.append(i)
        r4.append(i[3])
    r4.sort(key=lambda date: datetime.strptime(date, "%d-%m-%Y"))
    for i in r4:
        for j in r3:
            if i==j[3] and j not in r5:
                r5.append(j)
    r5.reverse()
    return r5

def LocalizarEquip(x):
    cur.execute("""SELECT situacao,nometec,modelo,numserie,patri,andar_atual,setor_atual,local_atual
                   FROM equipamentos
                   WHERE numserie =? OR patri = ?""",(x,x, ))
    r1=cur.fetchall()
    return r1

def LocalizarEquipAndar(x):
    cur.execute("""SELECT *
                   FROM equipamentos
                   WHERE andar_atual = ?""",(x, ))
    r1=cur.fetchall()
    return r1

def LocalizarEquipSetor(x):
    cur.execute("""SELECT *
                   FROM equipamentos
                   WHERE setor_atual = ?""",(x, ))
    r1=cur.fetchall()
    return r1

def LocalizarEquipLocal(x):
    cur.execute("""SELECT *
                   FROM equipamentos
                   WHERE local_atual = ?""",(x, ))
    r1=cur.fetchall()
    return r1


def  Historico(x):
    cur.execute("""SELECT nometec,modelo,numserie,patri
                   FROM equipamentos
                   WHERE numserie =? OR patri = ?""",(x,x, ))
    r1 = cur.fetchall()
    
    cur.execute("""SELECT calibracao.*
                   FROM calibracao
                   WHERE numserie =? OR patri = ?""",(x,x, ))
    r2 = cur.fetchall()
    
    cur.execute("""SELECT preventiva.*
                   FROM preventiva
                   WHERE numserie =? OR patri = ?""",(x,x, ))
    r3 = cur.fetchall()
    
    cur.execute("""SELECT esporadica.*
                   FROM esporadica
                   WHERE numserie =? OR patri = ?""",(x,x, ))
    r4 = cur.fetchall()
    
    cur.execute("""SELECT movimentacao.*
                   FROM movimentacao
                   WHERE numserie =? OR patri = ?""",(x,x, ))
    r5 = cur.fetchall()
    
    cur.execute("""SELECT reentrada.*
                   FROM reentrada
                   WHERE numserie =? OR patri = ?""",(x,x, ))
    r6 = cur.fetchall()
    
    cur.execute("""SELECT tempos.*
                   FROM tempos
                   WHERE nometec = ? AND modelo=?""",(r1[0][0],r1[0][1] ))
    r10 = cur.fetchall()
    
    r7 = []
    r8 = []
    r9 = []
    for i in r2:
        r7.append(i)
        r8.append(i[3])
    for i in r3:
        r7.append(i)
        r8.append(i[3])
    for i in r4:
        r7.append(i)
        r8.append(i[3])
    for i in r5:
        r7.append(i)
        r8.append(i[3])
    for i in r6:
        r7.append(i)
        r8.append(i[3])
    for i in r10:
        r7.append(i)
        r8.append(i[3])
    r8.sort(key=lambda date: datetime.strptime(date, "%d-%m-%Y"))
    for i in r8:
        for j in r7:
            if i==j[3] and j not in r9:
                r9.append(j)
    r9.reverse()
    print(r9)
    return r9

def delete():
    x = input("Insira o patrimônio")
    cur.execute("SELECT * FROM equipamentos WHERE patri = ?",(x, ))
    r1=cur.fetchall()
    y = input(f"Este é o equipamento que deseja deletar? 's' para SIM e 'n' para NÃO \n{r1}")
    if y == 's':
        cur.execute("DELETE FROM equipamentos WHERE patri = ?",(x, ))
        con.commit()
    if y == 'n':
        delete()

def manu():
    cur.execute("SELECT nometec,numserie,patri,andar_atual,setor_atual FROM equipamentos WHERE andar_atual='Em Calibração!' OR andar_atual='Em Preventiva!' OR andar_atual='Em Manutenção Esporádica!'")
    r1=cur.fetchall()
    return r1

def emprest():
    cur.execute("SELECT nometec,numserie,patri,andar_atual,setor_atual FROM equipamentos WHERE setor_atual='Emprestado!'")
    r1=cur.fetchall()
    return r1

def alarme():
    r1=[]
    cur.execute("SELECT numserie,patri,situacao FROM equipamentos")
    y = cur.fetchall()
    for i in y:
        if i[2]=='Ativo':
            cur.execute("""SELECT data_retirada FROM calibracao
                           WHERE numserie = ? OR patri = ?""",(i[0],i[1], ))
            q = cur.fetchall()
            if q == []:
                tempo=0
                cur.execute("""SELECT data_aceitação FROM equipamentos
                               WHERE numserie = ? OR patri = ?""",(i[0],i[1], ))
                x = str(cur.fetchall())
                dt=datetime.strptime(x,"[('%d-%m-%Y',)]")
                tempo=(datetime.now()-dt)
                meses=float(tempo.days/30.41)
            if q != []:
                cur.execute("""SELECT data_retirada FROM calibracao
                               WHERE numserie = ? OR patri = ?""",(i[0],i[1], ))
                f = cur.fetchall()
                u = str(f[(len(f)-1)])
                tempo=0
                dt=datetime.strptime(u,"('%d-%m-%Y',)")
                tempo=(datetime.now()-dt)
                meses=float(tempo.days/30.41)
            cur.execute("""SELECT temp_calibracao FROM equipamentos
                           WHERE numserie = ? OR patri = ?""",(i[0],i[1], ))
            g = cur.fetchall()

            cur.execute("""SELECT nometec, numserie,andar_atual,setor_atual,local_atual,patri,modelo FROM equipamentos
                               WHERE numserie = ? OR patri = ?""",(i[0],i[1], ))
            j = cur.fetchall()
            if meses > g[0][0]:
                r1.append(((j[0][0]),(j[0][6]),(j[0][1]),(j[0][5]),("Calibração Vencida"),(f"{j[0][2]},  {j[0][3]},  {j[0][4]}")))
            elif meses > (g[0][0]-1):
                r1.append(((j[0][0]),(j[0][6]),(j[0][1]),(j[0][5]),("Calibração próxima do vencimento"),(f"{j[0][2]},  {j[0][3]},  {j[0][4]}")))
    return r1
def alarme1():
    r1=[]
    cur.execute("SELECT numserie,patri,situacao FROM equipamentos")
    y = cur.fetchall()
    for i in y:
        if i[2]=='Ativo':
            cur.execute("""SELECT data_retirada FROM preventiva
                           WHERE numserie = ? OR patri = ?""",(i[0],i[1], ))
            q = cur.fetchall()
            if q == []:
                tempo=0
                cur.execute("""SELECT data_aceitação FROM equipamentos
                               WHERE numserie = ? OR patri = ?""",(i[0],i[1], ))
                x = str(cur.fetchall())
                dt=datetime.strptime(x,"[('%d-%m-%Y',)]")
                tempo=(datetime.now()-dt)
                meses=float(tempo.days/30.41)
            if q != []:
                cur.execute("""SELECT data_retirada FROM preventiva
                               WHERE numserie = ? OR patri = ?""",(i[0],i[1], ))
                f = cur.fetchall()
                u = str(f[(len(f)-1)])
                tempo=0
                dt=datetime.strptime(u,"('%d-%m-%Y',)")
                tempo=(datetime.now()-dt)
                meses=float(tempo.days/30.41)
            cur.execute("""SELECT temp_preventiva FROM equipamentos
                           WHERE numserie = ? OR patri = ?""",(i[0],i[1], ))
            g = cur.fetchall()

            cur.execute("""SELECT nometec, numserie,andar_atual,setor_atual,local_atual,patri,modelo FROM equipamentos
                               WHERE numserie = ? OR patri = ?""",(i[0],i[1], ))
            j = cur.fetchall()
            if meses > g[0][0]:
                r1.append(((j[0][0]),(j[0][6]),(j[0][1]),(j[0][5]),("Preventiva Vencida"),(f"{j[0][2]},  {j[0][3]},  {j[0][4]}")))
            elif meses > (g[0][0]-1):
                r1.append(((j[0][0]),(j[0][6]),(j[0][1]),(j[0][5]),("Preventiva próxima do vencimento"),(f"{j[0][2]},  {j[0][3]},  {j[0][4]}")))
    return r1

def Todos():
    cur.execute("SELECT * FROM equipamentos WHERE situacao = 'Ativo'")
    r1=cur.fetchall()
    r1.reverse()
    return r1

def TodosDale(x):
    cur.execute("SELECT nometec,modelo FROM equipamentos WHERE nometec=?",(x, ))
    r1=cur.fetchall()
    r2=[]
    r3=[]
    for i in r1:
        if i not in r2:
            r2.append(i)
    for i in r2:
        r3.append(i[1])
    return r3

def NomeTecTreinados():
    cur.execute("SELECT * FROM treinados")
    r1=cur.fetchall()
    return r1

def  ModeloTreinados(x):
    cur.execute("SELECT nometec,modelo FROM treinados WHERE nometec=?",(x, ))
    r1=cur.fetchall()
    r2=[]
    r3=[]
    for i in r1:
        if i not in r2:
            r2.append(i)
    for i in r2:
        r3.append(i[1])
    return r3

def TodosDes():
    cur.execute("SELECT * FROM equip_desenv")
    r1=cur.fetchall()
    return r1

def TodosCalibr():
    cur.execute("SELECT * FROM calibracao")
    r1=cur.fetchall()
    r2=[]
    r3=[]
    r4=[]
    for i in r1:
        r2.append(i)
        r3.append(i[3])
    r3.sort(key=lambda date: datetime.strptime(date, "%d-%m-%Y"))
    for i in r3:
        for j in r2:
            if i==j[3] and j not in r4:
                r4.append(j)
    r4.reverse()
    return r4

def TodosPreventiva():
    cur.execute("SELECT * FROM preventiva")
    r1=cur.fetchall()
    r2=[]
    r3=[]
    r4=[]
    for i in r1:
        r2.append(i)
        r3.append(i[3])
    r3.sort(key=lambda date: datetime.strptime(date, "%d-%m-%Y"))
    for i in r3:
        for j in r2:
            if i==j[3] and j not in r4:
                r4.append(j)
    r4.reverse()
    return r4
    

def TodosEsporadica():
    cur.execute("SELECT * FROM esporadica")
    r1=cur.fetchall()
    r2=[]
    r3=[]
    r4=[]
    for i in r1:
        r2.append(i)
        r3.append(i[3])
    r3.sort(key=lambda date: datetime.strptime(date, "%d-%m-%Y"))
    for i in r3:
        for j in r2:
            if i==j[3] and j not in r4:
                r4.append(j)
    r4.reverse()
    return r4

def TodosMovimentacao():
    cur.execute("SELECT * FROM movimentacao")
    r1=cur.fetchall()
    r2=[]
    r3=[]
    r4=[]
    for i in r1:
        r2.append(i)
        r3.append(i[3])
    r3.sort(key=lambda date: datetime.strptime(date, "%d-%m-%Y"))
    for i in r3:
        for j in r2:
            if i==j[3] and j not in r4:
                r4.append(j)
    r4.reverse()
    return r4

def TodosReentrada():
    cur.execute("SELECT * FROM reentrada")
    r1=cur.fetchall()
    r2=[]
    r3=[]
    r4=[]
    for i in r1:
        r2.append(i)
        r3.append(i[3])
    r3.sort(key=lambda date: datetime.strptime(date, "%d-%m-%Y"))
    for i in r3:
        for j in r2:
            if i==j[3] and j not in r4:
                r4.append(j)
    r4.reverse()
    return r4

def TodosDesativados():
    cur.execute("SELECT tipo,patri,numserie,data_desativ,motivo_desativ,num_processo,obs,logado FROM desativacao")
    r1=cur.fetchall()
    return r1            

def TodosFabri():
    cur.execute("SELECT * FROM fabricantes")
    r1=cur.fetchall()
    return r1

def TodosFabri1():
    cur.execute("SELECT fabricante FROM equipamentos")
    r1=cur.fetchall()
    r2=[]
    for i in r1:
        if i[0] not in r2:
            r2.append(i[0])
    return r2

def ProcDesativados(x):
    cur.execute("""SELECT tipo,patri,numserie,data_desativ,motivo_desativ,num_processo,obs,logado
                   FROM desativacao
                   WHERE numserie = ? OR patri = ?""",(x,x, ))
    r1=cur.fetchall()
    return r1 

def TodosDesativadosDes():
    cur.execute("SELECT tipo,num_registro,data_desativ,motivo_desativ,num_processo,obs,logado FROM desativacao_des")
    r1=cur.fetchall()
    return r1

def ProcDesativadosDes(x):
    cur.execute("""SELECT tipo,num_registro,data_desativ,motivo_desativ,num_processo,obs,logado
                   FROM desativacao_des
                   WHERE num_registro = ?""",(x, ))
    r1=cur.fetchall()
    return r1 

def ListaAndares():
    cur.execute("SELECT andar FROM andares")
    r1 = cur.fetchall()
    r2=[]
    for i in r1:
        r2.append(i[0])
    return r2

def ListaSetores1():
    cur.execute("SELECT setor FROM setores")
    r1 = cur.fetchall()
    r2=[]
    for i in r1:
        r2.append(i[0])
    return r2

def ListaSetores(x):
    cur.execute("SELECT setor FROM setores WHERE andar = ?",(x, ))
    r1 = cur.fetchall()
    r2=[]
    for i in r1:
        r2.append(i[0])
    return r2

def ListaFabri():
    cur.execute("SELECT empresa FROM fabricantes")
    r1 = cur.fetchall()
    r2=[]
    for i in r1:
        r2.append(i[0])
    return r2

createEquipamentos()
createCalibração()
createPreventiva()
createManutençãoEsporadica()
createReentrada()
createMovimentacao()
createDesativacao()
createDesativacaoDes()
createEquipamentoEmDesenvolvimento()
createCadastro()
createAndar()
createSetor()
createFabri()
createTreinados()

def shutdown():
    con.close()

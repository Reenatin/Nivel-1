
from math import*
from string import* 
import datetime 

lcliente=[]
lagente=[]
lagentename = [] 
ltel=[]
lligacoes = []

  
cliente=0
agente=0 
agentename=0
tel=0 
codagente = 0

 



#A função que ira ser usada 
def menu (): 
    print('')
    print ('Menu:') 
    print ('1 - Cadastrar Cliente') 
    print ('2 - Cadastrar Agente') 
    print ('3 - Fazer ligação') 
    print ('4 - Receber ligação') 
    print ('5 - Mostrar Clientes') 
    print ('6 - Mostrar Agentes') 
    print ('7 - Mostrar Ligações') 
    print ('0 - Sair') 
    print('')
    opt = input('> ') 
    return opt 
  
def cadastrar_cliente ():
    cliente = str(input("Informe o nome do cliente:"))
    cliente=cliente.upper()
    if cliente in lcliente:
        print('Cliente já cadastrado')
    else:
        lcliente.append(cliente)
        t1 = 0
        while (t1 == 0):

          try:  
            tel=int(input("Informe o telefone do cliente:"))
            ltel.append(tel)

            t1 = 1
    
          except:
            print("Número de telefone incorreto!")
            t1 = 0


        print('Cadastro realizado com sucesso!') 
    pass 


def cadastrar_agente ():
    t2 = 0
    while (t2 == 0):
    
      try:
        agente = int(input("Informe o Código do Agente:"))
    
        if agente in lagente:
          print('Cliente já cadastrado')
        else:
          lagente.append(agente)
          
          agentename = str(input("Informe o Nome do Agente:"))
          agentename=agentename.upper()
          lagentename.append(agentename)


          print('Cadastro realizado com sucesso!') 
        t2 = 1

      except:
        print("Código deve ser um número!")
        t2 = 0
        
    pass 
      





  
def fazer_ligacao ():

  codagente = int(input("Informe o código do agente que está realizando a discagem:"))
  teldestino = int(input("Informe o telefone de destino:"))



  if (codagente in lagente):

    num = 0
    num_max = len(lagente)

    while (num <= num_max):
      posicao = lagente[num]

      if (posicao == codagente):
        name = lagentename[num]

        num = num_max + 1

      else:
        num = num+1

  else: 
    print('Não existe agente com o código '+str(codagente))


  if (teldestino in ltel):
    num1 = 0
    num_max1 = len(ltel)

    while (num1 <= num_max1):
      posicao1 = ltel[num1]

      if (posicao1 == teldestino):
        namedestinocli = lcliente[num1]
        num1 = num_max1 + 1

      else:
        num1 = num1+1    
  else:
  
  
  
    print("Não existe o telefone "+str(teldestino)+" cadastrado para discagem ..." )

  try:
    print('Agente '+str(name)+' realizou uma ligação para Cliente '+str(namedestinocli) )
    len_ligacoes = len(lligacoes)
  
    now = datetime.datetime.now()
    dia = now.day
    mes = now.month
    ano = now.year
    hora = now.hour
    minutos = now.minute
    segundos = now.second

    script = ('Ligação '+str(len_ligacoes)+' - Feita por '+str(name)+'para '+str(teldestino)+' - Data:'+str(dia)+'/'+str(mes)+'/'+str(ano)+' - Hora: '+str(hora)+':'+str(minutos)+':'+str(segundos))

    lligacoes.append(script)
  
  except:
    print('')






def receber_ligacao ():
  number_recep = int(input("Informe o telefone que está ligando para a empresa: "))

  if (number_recep not in ltel):
    print('Telefone '+str(number_recep)+' realizou uma chamada para a empresa!')
    len_ligacoes = len(lligacoes)
  
    now = datetime.datetime.now()
    dia = now.day
    mes = now.month
    ano = now.year
    hora = now.hour
    minutos = now.minute
    segundos = now.second

    script = ('Ligação '+str(len_ligacoes)+' - Recebida de '+str(number_recep)+' - Data:'+str(dia)+'/'+str(mes)+'/'+str(ano)+' - Hora '+str(hora)+':'+str(minutos)+':'+str(segundos))

    lligacoes.append(script)


  else:
    recept_num = 0
    recept_num_max = len(ltel)

    while (recept_num <= recept_num_max):
      posicao_tel = ltel[recept_num]

      if (posicao_tel == number_recep):
        tel_recept = lcliente[recept_num]

        recept_num = recept_num_max + 1

      else:
        recept_num = recept_num+1

    print ('Cliente '+str(tel_recept)+' realizou uma chamada para a empresa!')
    
    len_ligacoes = len(lligacoes)
  
    now = datetime.datetime.now()
    dia = now.day
    mes = now.month
    ano = now.year
    hora = now.hour
    minutos = now.minute
    segundos = now.second

    script = ('Ligação '+str(len_ligacoes)+' - Recebida de '+str(tel_recept)+' - Data:'+str(dia)+'/'+str(mes)+'/'+str(ano)+' - Hora: '+str(hora)+':'+str(minutos)+':'+str(segundos))

    lligacoes.append(script)



def mostrar_clientes():
  num_mostrar = 0
  num_mostrar_max = len(lcliente)

  try:
    while (num_mostrar <= num_mostrar_max):
      namecliente_mostrar = lcliente[num_mostrar]
      telcliente_mostrar = ltel[num_mostrar]

      print('Cliente: '+str(namecliente_mostrar)+' - Telefone: '+str(telcliente_mostrar))
      num_mostrar = num_mostrar + 1
  except:
    print('')

def mostrar_agentes():
  num_mostrar_agentes = 0
  num_mostrar_agentes_max = len(lagente)

  try:
    while (num_mostrar_agentes <= num_mostrar_agentes_max):
      codagente_mostrar = lagente[num_mostrar_agentes]
      nameagente_mostrar = lagentename[num_mostrar_agentes]

      print('Agente: '+str(nameagente_mostrar)+'- Código: '+str(codagente_mostrar))
      num_mostrar_agentes = num_mostrar_agentes + 1 
  except:
    print('')


def mostrar_ligacoes():
  num_ligacoes = 0
  num_ligacoes_max = len(lligacoes)
  
  while (num_ligacoes <= num_ligacoes_max):
    script_mostrar = lligacoes[num_ligacoes]

    print(script_mostrar)
    num_ligacoes = num_ligacoes + 1 




opcao = menu() 
while opcao != '9': 
    if opcao == '1': 
        cadastrar_cliente() 
    elif opcao == '2':  
        cadastrar_agente() 
    elif opcao == '3':  
        fazer_ligacao() 
    elif opcao == '4':  
        receber_ligacao() 
    elif opcao == '5':  
        mostrar_clientes() 
    elif opcao == '6':  
        mostrar_ligacoes()
    elif opcao == '7':
        le_diario()
 
  
    opcao = menu() 
  

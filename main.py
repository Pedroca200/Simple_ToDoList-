import os
def clean():
    os.system('clear')


def criartask(a):    
    try:
        b = input("Nome da nova tarefa:\n")           
        a.append(b)

    except KeyboardInterrupt:
        print("Erro, tente novamente")
    
    clean()
    Mainpage(a)

def DeleteTask(a, b = None):
    
    if b == None:
        try:
            Mostrar(a)
            b = int(input("Qual a tarefa a ser removid: "))
            a.pop(b - 1)
            Mainpage(a)

        except (KeyboardInterrupt, TypeError):
            print("Digite apenas os número do indice")
        
    else:
        a.pop(b - 1)
        Mainpage(a)

#Função responsavel por mostrar a lista
def Mostrar(a = None):
    if a is None:
        a = []

    if len(a) == 0: # Verifica se a lista esta vazia 
        print ("A lista está vazia!")
    else:
        for i in range (len(a)):
            print(f"{i+1}. {a[i]}")
    

# Essa função só serve
def Mainpage(a):

    while True:
        clean()
        Mostrar(a)

        print('\n')
        print("Opções:")   
        print("1. Adicionar")
        print("2. Remover")
        print("3. Sair"+"\n")

        choice = input("Escolha a sua opção")

        if int(choice) == 1:
            clean()
            criartask(a)


        elif int(choice) == 2:
            clean()
            DeleteTask(a)

        elif int(choice) == 3:
            clean()
            print("saindo...")
            break
        else:
            clean()
            print("Algo deu errado"+"\n"*3)

tasklist = []
Mainpage(tasklist)


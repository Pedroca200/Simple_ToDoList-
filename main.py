# Eu podia ter deixado em arquivos .py separados, mas vivia dando problema :P

import os
# Essa função limpa o terminal
def clean():
    os.system('clear')

# Essa função é responsavel para adicionar uma tarefa nova na lista
def criartask(a):    
    try:
        b = input("Nome da nova tarefa:\n")           
        a.append(b)
        save(a)

    except KeyboardInterrupt:
        print("Erro, tente novamente")
    
    clean()
    Mainpage(a)

# Responsavel por remover uma tarefa
def DeleteTask(a, b = None):
    
    if b == None:
        try:
            Mostrar(a)
            b = int(input("Qual a tarefa a ser removida: "))
            a.pop(b - 1)
            save(a)
            Mainpage(a)

        except (KeyboardInterrupt, TypeError):
            print("Digite apenas os número do indice")
        
    else:
        a.pop(b - 1)
        Mainpage(a)

# Função responsavel para salvar a lista depois de modificações
def save(a):
    with open('task.txt',"w") as tasklist:
        for task in a:
            tasklist.write(task + '\n')

#Função responsavel por mostrar a lista
def Mostrar(a = None):
    if a is None:
        a = []

    if len(a) == 0: # Verifica se a lista esta vazia 
        print ("A lista está vazia!")
    else:
        for i in range (len(a)):
            print(f"{i+1}. {a[i]}")
    

# Essa função só serve para mostrar uma tela inicial
def Mainpage(a):

    while True:
        clean()
        Mostrar(a)

        print('\n')
        print("Opções:")   
        print("1. Adicionar")
        print("2. Remover")
        print("3. Sair"+"\n")

        choice = input("Escolha a sua opção: \n")

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

try:
    with open('task.txt', 'r') as tasklist:
        task = [line.strip() for line in tasklist.readlines()]
except FileNotFoundError:
    task = []

Mainpage(task)


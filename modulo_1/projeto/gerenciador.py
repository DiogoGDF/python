import os
import time
lista_tarefas = []

def strike(text):
    return '\u0336'.join(text) + '\u0336'

def imprimir_tarefas(contagem):
    print("\n--- Tarefas ---")
    if contagem:
        for cont in range(len(lista_tarefas)):
            print(f'\n{cont + 1} - {lista_tarefas[cont][0]} {lista_tarefas[cont][1]}')
        tarefa = int(input("\nDigite o número da tarefa: ")) - 1
        print('\n')
        return tarefa
        
    else: 
        for tarefa in lista_tarefas:
            print(f'\n {tarefa[0]} {tarefa[1]}')
        print('\n')

def adicionar_tarefa():
    inpt = input("Digite a tarefa: ")
    tarefa = ["[ ]", inpt]
    lista_tarefas.append(tarefa)

def atualizar_tarefa():
    tarefa_update = imprimir_tarefas(True)
    tarefa = input("Digite a tarefa atualizada: ")
    lista_tarefas[tarefa_update][1] = tarefa

def completar_tarefa():
    tarefa_completa = imprimir_tarefas(True)
    lista_tarefas[tarefa_completa] = [lista_tarefas[tarefa_completa][0].replace(" ", "✓", 1), strike(lista_tarefas[tarefa_completa][1])]
    os.system("clear")
    imprimir_tarefas(False)
    time.sleep(0.6)

def remover_tarefas():
    imprimir_tarefas(False)
    time.sleep(0.4)
    remover = []
    for index in range(len(lista_tarefas)):
        if lista_tarefas[index][0][1] == "✓":
            remover.insert(0, index)

    for index in remover:
        lista_tarefas.pop(index)

    os.system("clear")
    imprimir_tarefas(False)
    time.sleep(0.5)

while True:
    os.system("clear")

    print("\nMenu do Gerenciador de Lista de tarefas:\n")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar Tarefas")
    print("4. Completar Tarefas")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    escolha = input("\nDigite a sua escolha: ")
    os.system("clear")

    if escolha == "1":
        adicionar_tarefa()

    elif escolha == "2":
        imprimir_tarefas(False)
        input("\nPrecione enter para voltar ")

    elif escolha == "3":
        atualizar_tarefa()

    elif escolha == "4":
        completar_tarefa()

    elif escolha == "5":
        remover_tarefas()

    elif escolha == "6":
        break

os.system("clear")
print("Programa finalizado")
time.sleep(0.6)
os.system("clear")
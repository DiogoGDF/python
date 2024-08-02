import os
import time
lista_tarefas = []


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
        tarefa = input("Digite a tarefa: ")
        lista_tarefas.append("[ ] " + tarefa)

    elif escolha == "2":
        print("\n--- Tarefas ---")
        print("\n".join(lista_tarefas))

        input("\nPrecione enter para voltar ")

    elif escolha == "3":
        print("\n--- Tarefas ---")

        for count in range(len(lista_tarefas)):
            print(str(count + 1) + " - " + lista_tarefas[count])
        
        tarefa_update = int(input("\nDigite o número da tarefa a ser atualizada: ")) - 1
        tarefa = input("Digite a tarefa atualizada: ")
        lista_tarefas[tarefa_update] = "[ ] " + tarefa

    elif escolha == "4":
        print("\n--- Tarefas ---")
        for count in range(len(lista_tarefas)):
            print(str(count + 1) + " - " + lista_tarefas[count])

        tarefa_completa = int(input("\nDigite o número da tarefa a completada: ")) - 1
        lista_tarefas[tarefa_completa] = lista_tarefas[tarefa_completa].replace(" ", "x", 1)
        os.system("clear")
        print("\n--- Tarefas ---")
        print("\n".join(lista_tarefas))
        time.sleep(0.6)

    elif escolha == "5":
        print("\n--- Tarefas ---")
        print("\n".join(lista_tarefas))
        time.sleep(0.4)
        remover = []
        for index in range(len(lista_tarefas)):
            if lista_tarefas[index][1] == "x":
                remover.insert(0, index)

        for index in remover:
            lista_tarefas.pop(index)

        os.system("clear")
        print("\n--- Tarefas ---")
        print("\n".join(lista_tarefas))
        time.sleep(0.5)


    elif escolha == "6":
        break

os.system("clear")
print("Programa finalizado")
time.sleep(0.6)
os.system("clear")
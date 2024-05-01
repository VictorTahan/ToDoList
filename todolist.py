todolist = []
def exibir_tarefas():
    print("Você possui as seguintes tarefas: ")
    for itens in todolist:
        indice = todolist.index(itens) + 1
        print(f"Tarefa {indice} {itens['tarefa']}:, Horário: {itens['hora']}, Status: {itens['status']}")

while True:
    menu = int(input("Digite 1 para cadastrar tarefas.\nDigite 2 para ver todas as tarefas.\nDigite 3 para editar ou remover tarefas.\nDigite qualquer outro número para sair. "))
    if menu == 1:
        qtd_tarefas = int(input("Digite a quantidade de tarefas a serem feitas: "))
        for i in range (qtd_tarefas):
            tarefa = {}
            tarefa['tarefa'] = input("Insira um nome para a tarefa: ")
            tarefa['hora'] = input("Insira um horário para realização da tarefa: ")
            status = int(input("Digite 1 para marcar como 'Concluída'.\nDigite qualquer outro número para marcar como 'Pendente'"))
            if status == 1:
                status = "Concluída"
            else:
                status = "Pendente"
            tarefa['status'] = status
            todolist.append(tarefa)
        exibir_tarefas()
    elif menu == 2:
        exibir_tarefas()

    elif menu == 3:
        escolha = int(input("Digite 1 para editar uma tarefa\nDigite 2 para remover uma tarefa\nDigite qualquer outro número para retornar ao menu anterior."))
        if escolha == 1:
            exibir_tarefas()
            editar = int(input("Digite o número da tarefa que deseja editar: "))
            if 1<= editar <= len(todolist):
                tarefa = todolist[editar -1]
                selecttoedit = int(input("Digite 1 para alterar o nome da tarefa.\nDigite 2 para alterar o horário da tarefa.\nDigite 3 para alterar o status da tarefa."))
                if selecttoedit == 1:
                    tarefa['tarefa'] = input("Digite o novo nome da tarefa: ")
                    print("Tarefa editada com sucesso!")
                elif selecttoedit == 2:
                    tarefa['hora'] = input("Digite o novo horário da tarefa: ")
                    print("Tarefa editada com sucesso!")
                elif selecttoedit == 3:
                    status = int(input(
                        "Digite 1 para marcar como 'Concluída'.\nDigite qualquer outro número para marcar como 'Pendente'"))
                    if status == 1:
                        status = "Concluída"
                    else:
                        status = "Pendente"
                    tarefa['status'] = status
                    print("Tarefa editada com sucesso!")
                else:
                    print("Opção inválida!")
                    print(selecttoedit)
            else:
                print("Número da tarefa inválido!")
        elif escolha == 2:
            exibir_tarefas()
            remover = int(input("Digite o número da tarefa que deseja remover: "))
            if 1 <= remover <= len(todolist):
                tarefa_rem = todolist[remover -1]
                todolist.remove(tarefa_rem)
            print("Tarefa removida com sucesso!")
        else:
            print(menu)
    else:
        print("Programa finalizado!")
        break






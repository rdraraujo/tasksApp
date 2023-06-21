tasks = []
resp = "A"
def addTask(tasks):
    print("TAREFA ", len(tasks)+1)
    tasks.append(input("--> "))
def taskConc():
    while True:
        try:
            check = int(input("Qual tarefa foi concluída? "))
            if check <= 0 or check > len(tasks):
                print("Tarefa inválida!")
                continue
            break
        except ValueError:
            print("Entrada inválida! Digite um número inteiro válido.")
    del tasks[check-1]
def menu (resp):
    resp = input("\n(A) para adicionar tarefa\n"
                 "(C) para marcar tarefa como concluída\n"
                 "(N) para finalizar o programa: ").upper()
    return resp
def exibirTarefas(tasks):
    cont = 1
    print("\nLISTA DE TAREFAS")
    for itens in tasks:
        print("Tarefa ", cont, "\n" , itens)
        cont = cont + 1

addTask(tasks)
resp = menu(resp)
while resp != "N":
    exibirTarefas(tasks)
    while resp != "A" and resp != "C":
        print("\nINPUT INVÁLIDO")
        resp = menu(resp)
    if resp == "A":
        exibirTarefas(tasks)
        addTask(tasks)
        resp = menu(resp)
    elif resp == "C":
        exibirTarefas(tasks)
        taskConc()
        exibirTarefas(tasks)
        resp = menu(resp)

if len(tasks) > 0:
    print("\nVocê deixou tarefas por concluir!\nPROGRAMA FINALIZADO")
else:
    print("\nVocê concluiu todas as tarefas!\nPROGRAMA FINALIZADO")
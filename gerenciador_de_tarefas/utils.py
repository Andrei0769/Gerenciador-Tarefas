import json
from tarefa import Tarefa  # Adicione esta linha para importar a classe Tarefa

def carregar_tarefas():
    try:
        with open('tarefas.json', 'r') as f:
            tarefas = json.load(f)
            return [Tarefa(**tarefa) for tarefa in tarefas]  # Aqui usamos a classe Tarefa
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas):
    with open('tarefas.json', 'w') as f:
        json.dump([tarefa.__dict__ for tarefa in tarefas], f)

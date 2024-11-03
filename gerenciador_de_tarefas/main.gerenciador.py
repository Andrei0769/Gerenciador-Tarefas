from tarefa import Tarefa
from utils import carregar_tarefas, salvar_tarefas

class GerenciadorDeTarefas:
    def __init__(self):
        self.tarefas = carregar_tarefas()

    def adicionar_tarefa(self, titulo, descricao):
        tarefa = Tarefa(titulo, descricao)
        self.tarefas.append(tarefa)
        salvar_tarefas(self.tarefas)

    def mostrar_tarefas(self):
        for i, tarefa in enumerate(self.tarefas, start=1):
            print(f"\n{i}. {tarefa.titulo} - {tarefa.descricao} {'(Concluída)' if tarefa.concluida else ''}")

    def concluir_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice].concluida = True
            salvar_tarefas(self.tarefas)

if __name__ == "__main__":
    gerenciador = GerenciadorDeTarefas()
    gerenciador.adicionar_tarefa("Estudar Python", "Revisar POO e testes unitários.")
    gerenciador.mostrar_tarefas()

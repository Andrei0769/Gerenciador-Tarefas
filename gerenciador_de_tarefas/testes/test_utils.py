import unittest
from utils import salvar_tarefas, carregar_tarefas
import os

class TestUtils(unittest.TestCase):
    def test_salvar_carregar_tarefas(self):
        tarefas = [Tarefa("Tarefa de Teste", "Esta é uma tarefa de teste")]
        salvar_tarefas(tarefas)
        tarefas_carregadas = carregar_tarefas()
        self.assertEqual(len(tarefas_carregadas), 1)
        self.assertEqual(tarefas_carregadas[0].titulo, "Tarefa de Teste")

    def tearDown(self):
        if os.path.exists('tarefas.json'):
            os.remove('tarefas.json')

if __name__ == "__main__":
    unittest.main()

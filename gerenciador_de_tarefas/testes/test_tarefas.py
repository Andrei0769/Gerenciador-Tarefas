import unittest
from tarefa import Tarefa

class TestTarefa(unittest.TestCase):
    def test_criacao_tarefa(self):
        tarefa = Tarefa("Tarefa de Teste", "Esta é uma tarefa de teste")
        self.assertEqual(tarefa.titulo, "Tarefa de Teste")
        self.assertEqual(tarefa.descricao, "Esta é uma tarefa de teste")
        self.assertFalse(tarefa.concluida)

if __name__ == "__main__":
    unittest.main()

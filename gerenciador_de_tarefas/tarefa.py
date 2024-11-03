class Tarefa:
    def __init__(self, titulo, descricao, concluida=False):
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = concluida  # Agora aceita o argumento concluida

    def __repr__(self):
        return f"Tarefa(titulo='{self.titulo}', descricao='{self.descricao}', concluida={self.concluida})"

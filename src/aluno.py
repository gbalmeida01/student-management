class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def media(self):
        return sum(self.notas) / len(self.notas)

    def situacao(self):
        return "Aprovado" if self.media() >= 7 else "Reprovado"

    def __str__(self):
        return f"{self.nome} - Média: {self.media():.2f} - Situação: {self.situacao()}"

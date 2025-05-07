from aluno import Aluno

class GerenciadorAlunos:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, nome, notas):
        aluno = Aluno(nome, notas)
        self.alunos.append(aluno)

    def listar_alunos(self):
        if not self.alunos:
            print("Nenhum aluno cadastrado.")
        for aluno in self.alunos:
            print(aluno)

    def salvar_em_arquivo(self, caminho):
        with open(caminho, "w") as arquivo:
            for aluno in self.alunos:
                arquivo.write(str(aluno) + "\n")
        print(f"Alunos salvos em {caminho}")

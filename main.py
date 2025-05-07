from gerenciamento import GerenciadorAlunos

def main():
    sistema = GerenciadorAlunos()
    sistema.adicionar_aluno("Gabriel", [8, 7, 9])
    sistema.adicionar_aluno("Julia", [5, 6, 6])
    sistema.adicionar_aluno("Lucas", [10, 9, 10])

    print("\n--- Lista de Alunos ---")
    sistema.listar_alunos()

    sistema.salvar_em_arquivo("alunos.txt")

if __name__ == "__main__":
    main()

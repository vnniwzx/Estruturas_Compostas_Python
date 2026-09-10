personagens = []
 
def criar_personagem():
    nome = input("Nome do personagem: ")
    classe = input("Classe do personagem: ")
    nivel = int(input("Nível do personagem: "))
    personagem = {
        "nome": nome,
        "classe": classe,
        "nivel": nivel
    }
 
    personagens.append(personagem)
    print("--- Dados do personagem criado ---")
    print("Nome:", personagem["nome"])
    print("Classe:", personagem["classe"])
    print("Nível:", personagem["nivel"])
 
criar_personagem()
 
alunos = []
 
def cadastrar_aluno():
    nome = input("Nome do aluno: ")
    idade = int(input("Idade do aluno: "))
    nota = int(input("Nota do aluno: "))
    aluno = {
        "nome": nome,
        "idade": idade,
        "nota": nota
    }
 
    alunos.append(aluno)
    print("--- Dados do personagem criado ---")
    print("Nome:", aluno["nome"])
    print("Classe:", aluno["idade"])
    print("Nível:", aluno["nota"])
 
cadastrar_aluno()

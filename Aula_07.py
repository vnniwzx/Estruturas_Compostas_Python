personagens = []

def criar_personagem():
    nome = input("Digite o nome do personagem: ")
    classe = input("Digite a classe do seu personagem: ")
    nivel = int(input("Digite o nivel do seu personagem: "))
    item = input("Digite um item para seu personagem: ")

    personagem = {
        "nome": nome,
        "classe": classe,
        "nivel": nivel,
        "inventario": item
    }

    personagens.append(personagem)
    
    for personage in personagens:
        print("\n--- Personagem Criado! ---")
        print("Nome:", personage["nome"])
        print("Classe:", personage["classe"])
        print("Nivel:", personage["nivel"])
        print("Item:", personage["inventario"])
        print()

opcao = input("\nDeseja criar um personagem? S/N: ")

while opcao != "N" or "n":
    criar_personagem()

    opcao = input("Deseja criar outro personagem? S/N: ")

print("Inicializando...")

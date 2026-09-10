personagens = [
    {"nome": "Arthos", "classe": "Guerreiro", "nivel": 1},
    {"nome": "Luna", "classe": "Maga", "nivel": 2}
]

for personagem in personagens:
    print("Nome:", personagem["nome"])
    print("Classe:", personagem["classe"])
    print("Nível:", personagem["nivel"])
    print()
    
produtos = [
    {"nome": "Notebook Gamer", "preco": 4500, "quantidade": 5},
    {"nome": "Mouse Sem Fio", "preco": 120, "quantidade": 15},
    {"nome": "Teclado Mecânico", "preco": 350, "quantidade": 8}
]

for produto in produtos:
    print("Produto:", produto["nome"])
    print("Preço", produto["preco"])
    print("Estoque: R$", produto["quantidade"])
    print()

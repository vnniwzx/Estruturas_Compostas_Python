personagens = [
    {
        "nome": "Arthos",
        "classe": "Guerreiro",
        "nivel": 1,
        "inventario": [
            ("Espada", "arma"),
            ("Poção", "poção")
        ]
    },
    {
        "nome": "Enzo",
        "classe": "Arqueiro",
        "nivel": 10,
        "inventario": [
            ("arco", "arma"),
            ("suco", "poção")
        ]
    }
]
 
for personagem in personagens:
    print("Nome:", personagem["nome"])
    print("Classe:", personagem["classe"])
    print("Nível:", personagem["nivel"])
    print("Inventário:")
 
 
    for item in personagem["inventario"]:
        print("-", item[0], "(" + item[1] + ")")
    print()

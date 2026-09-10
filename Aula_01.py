jogos = [
    ["Minecraft", "Fortnite", "Roblox"],
    ["FIFA", "God of War", "Spider-Man"],
    ["Mario Kart", "Zelda", "Pokémon"]
]

print("Jogos por plataforma:\n")

print("PC:")
for jogo in jogos[0]:
    print("-", jogo)
        
print("\nPlayStation:")
for jogo in jogos[1]:
    print("-", jogo)
    
print("\nNintendo:")
for jogo in jogos[2]:
    print("-", jogo)

catalogo_filmes = [
    ["Mad Max: Estrada da Fúria", "John Wick", "Duro de Matar", "Gladiador"],
    ["Orgulho e Preconceito", "Como Eu Era Antes de Você", "Diário de uma Paixão", "La La Land"],
    ["O Exorcista", "Invocação do Mal", "Hereditário", "O Iluminado"]
]

print("Filmes por categoria:\n")

print("Ação:")
for filme in catalogo_filmes[0]:
    print("-", filme)

print("Romance:")
for filme in catalogo_filmes[1]:
    print("-", filme)
    
print("Terror:")
for filme in catalogo_filmes[2]:
    print("-", filme)

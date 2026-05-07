produto_mais_caro = 0
media_de_precos = 0
quantos_produtos_custam_mais_de_100 = 0
total_de_produtos_cadastrados = 0
    
while True:
    produto = input("Digite o nome do produto (ou 'sair' para sair): ")
    preco = float(input("Digite o preço do produto: "))
    if produto == "sair":
        break

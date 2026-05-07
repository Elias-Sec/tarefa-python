produto_mais_caro = 0
media_de_precos = 0
quantos_produtos_custam_mais_de_100 = 0
total_de_produtos_cadastrados = 0
    
while True:
    produto = input("Digite o nome do produto (ou 'sair' para sair): ")
    preco = float(input("Digite o preço do produto: "))
    if produto == "sair":
        break
    if preco > produto_mais_caro:
        produto_mais_caro = preco
        media_de_precos += preco
    if preco > 100:
        quantos_produtos_custam_mais_de_100 += 1
    total_de_produtos_cadastrados += 1

if total_de_produtos_cadastrados > 0:
    media_de_precos /= total_de_produtos_cadastrados

print(f"O produto mais caro custa: R${produto_mais_caro:.2f}")
print(f"A média de preços dos produtos é: R${media_de_precos:.2f}")
print(f"Quantidade de produtos que custam mais de R$100: {quantos_produtos_custam_mais_de_100}")
print(f"Total de produtos cadastrados: {total_de_produtos_cadastrados}")
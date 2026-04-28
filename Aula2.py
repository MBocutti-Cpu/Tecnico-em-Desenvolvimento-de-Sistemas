print("=== Lanchonete do Fudencio === ")

print("-"*5, "cardapio", "-"*5)
nome_cliente= input("Por favor digite seu nome: ")

print(f"Olá {nome_cliente}! É um prazer atender você")
print("-"*26)

# Exibindo cardapio
print("-"*5, "cardapio", "-"*5)
print("1. Hamburguer Classico - R$ 25,00")
print("2. Hamburguer Gourmet - R$ 35,00")
print("3. Hamburguer Premium - R$ 45,00")
print("4. Refrigerante - R$ 5,00")

print("="*34)
# aqui começa o pedido
print("\nFaça o Seu Pedido: ")
qtd_hamburguer = int(input("Quantos Hamburgueres Classicos?"))
qtd_hamburguergourmet = int(input("quantos gourmet?"))
qtd_hamburguerpremium = int(input("quantos premium?"))
qtd_refri = int( input("Quantos refrigerantes você deseja?"))

# processamento
total_hamburguer = qtd_hamburguer * 25.00 + qtd_hamburguergourmet * 35.00 + qtd_hamburguerpremium * 45.00
total_refri = qtd_refri * 5.00
total_conta = total_hamburguer + total_refri
#  Fechamento de Pedido
print("\n" + "="*34)
print(" "*10, "CUPOM FISCAL", " "*10)
print("="*34)
print(f"cliente: {nome_cliente}")
print(f"Total de Hamburgueres: R$ {total_hamburguer}")
print(f"Total de refrigerantes: R$ {total_refri}")
print("-"*25)
print(f"VALOR TOTAL A PAGAR: R$ {total_conta}")
print(":)"* 10, "MUITO OBRIGADO PELA PREFERENCIA", ":)"* 10)
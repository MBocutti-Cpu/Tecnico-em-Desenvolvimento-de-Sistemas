nome = input("Digite seu nome:").strip()

while nome == "":
    print("Você não digitou o seu nome!")
    nome = input("Por favor, digite o seu nome: ")

print(f"Olá, {nome}! Tudo bem?")

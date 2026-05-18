idade = int(input("Digite a sua Idade:"))
cnh = input("Tem CNH? (SIM/NÃO): ")
if idade >= 18 and cnh == "sim":
    print ("você pode dirigir")
else:
    print("não pode dirigir")


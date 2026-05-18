procurar = input("Pesquisar peça:")
estoque = ["Prego", "Porca", "Arruela", "Parafuso", "Mola"]
for item in estoque:
    if item == procurar:
        print("Item encontrado no estoque!")
        break #interrompe o laço imrdiatamente
else:
        print("Item não encontrado após varredura completa.")
        
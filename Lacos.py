idade = int(input("Idade:")) 
if idade < 13:
    print ("criança")
elif idade < 18:
    print("adolescente")
elif idade < 65:
    print("adulto")
else:
    print("idoso")
    
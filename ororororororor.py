estudante = input("você é estudante sim ou não?")
idoso = int(input("você é idoso sim ou não,qual sua idade?"))


if estudante == "sim" or idoso >= 65 :
    print ("pode entrar")
else:
    print("não pode entrar")


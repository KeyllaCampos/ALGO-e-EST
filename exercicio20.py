idade=int(input("insira sua idade"))
membro=input("voce é um membro? ")
acompanhado=input(" voce esta acompanhado?")

if idade>=18:
    if membro=="sim":
        print("bem vindo")
    else:
        if acompanhado=="sim":
            print("pagar meia entrada")
        else:
            print("pagar ingresso")
            if acompanhado=="nao":
                print("pagar ingresso")

        
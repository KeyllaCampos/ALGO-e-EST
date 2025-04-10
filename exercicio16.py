nota1=int(input("digite a primeira nota"))
nota2=int(input("digite a segunda nota"))
nota3=int(input("digite a segundo nota"))
md=(nota1+nota3)/3
if md>=7:
    print("aprovado")
elif md<7 and md  >5:
    print("recuperação")
else:
    print("reprovado")
idade=int(input(" digite sua idade: "))
genero=input(" digite seu genero: ")
atleta=input("você é atleta? (sim) ou (nao)")

if idade<15:
    print(" artigos infantis")
elif idade>15 and idade<21 and genero=="feminino" :
     print("maquiagem e moda")
elif idade>15 and idade<32 and genero=="masculino" and atleta=="sim":
     print("artigos esportivos")
elif idade>15 and idade<21 and genero=="masculino" and atleta=="nao":
     print("videogames")
elif idade>21 and idade<32 and genero=="masculino" and atleta=="nao":
     print("livros, jardinagem e eletrodomestico")
elif idade>22 and idade<35 and genero=="feminino":
else: 
    print("não ha anuncio para esse publico")
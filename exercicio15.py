nome_produto=input("digite o nome do produto: ")
quantidade=int (input ("insira a quantidade comprada: "))
preco=float(input("digite o preço unitario: "))
total= quantidade * preco
desconto = total -  total *0.5
if total <=100:
    print(f"total com desconto R${total-desconto}")
else:
    print(f"total:  R${total}")




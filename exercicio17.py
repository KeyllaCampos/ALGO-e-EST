anonasci=int(input("digite seu ano de nascimento: "))
ano_atual =int(input(" digite o ano atual")) 
if anonasci > ano_atual:
    print("O ano atual não pode ser menor que o ano de nascimento, execute o programa novamente")
idade = ano_atual - anonasci

if idade >= 18:
    print(" Você é maior de idade", idade, "anos")

else:
    print("voê é menor de idade", idade, " anos")

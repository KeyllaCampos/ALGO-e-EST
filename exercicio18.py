salario=int(input(" digite seu salario: "))
horas_extras=int(input("digite as horas extras trabalhadas: "))
valor_hora_extra=int(input(" qual é o valor pago pela hora extra?"))

total_extra = horas_extras * valor_hora_extra
total = salario + total_extra
print("o total do seu salario com a hora extra é ", total)



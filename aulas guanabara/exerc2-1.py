valor_c = int(input("qual o valor da casa?"))
sala = int(input("qual o seu salario?"))
anos = int(input("por quantos anos irá pagar?"))

anos = anos * 12
prest = valor_c / anos 

sala_perc = sala/100*30

if prest <= sala_perc:
    print("seu emprestimo foi aprovado")
else:
    print("seu emprestimo foi negado, pois a prestacao ultrapassa 30 por cento do seu salario")
num1 =num2=res=0#variaveis globais. podem ser acessadas em qualquer lugar do codigo

def cn():#### ISSO É UMA FUNCÃOOOO
    canal="Cfb curso"##nao tem escopo global

    global canal2 ##PRimeiro defina como global e na proxima linha, defina o valor da variavel
    canal2 = "CFB global"

    print(canal)

cn()##isso chama a funcao

print(canal2)

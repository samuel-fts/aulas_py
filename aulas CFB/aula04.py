x=1 #int
x="cfb curso" #string
x=15.6 #float
x-True #bool
n1=5;n2=2;x=complex(n1,n2)
print(x.real)
print(x.imag)
# x=["carro","aviao","navio", 1, 58.3, True]#List/array
# x=("carro","aviao","navio", 1, 58.3, True)#tupla. sap arrayd que nao se pode mudar

# x=range(0,100,1)#lista de um parametro ao outro
x={
    "canal":"cfb cursos"
}

print("valor:" + x["canal"])

# x[0]="forro"

x={5,7,4,5,7}#set
x=frozenset({5,7,4,5,7})#set que nao se pode ser alterado

print("valor: " +str(x))
print(type(x))#retorna o tipo da variavel
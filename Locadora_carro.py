print ("----- TABELA DE PREÇOS -----")
print (" Preço diaria: R$ 90")
print (" Valor por km: R$ 0,20")
print ("-----------------------------")

qtkm = float(input("Digite a quilometragem percorrida: "))
dias = int(input("Digite quantos dias o carro ficou alugado: "))
diaria = 90
valorkm = 0.20
totalpag = (dias*diaria)+ (qtkm*valorkm)

print ("---------- RECIBO ----------")
print (f"valor diarias: R$ {dias*diaria}")
print (f"Valor km percorrido: R$ {qtkm*valorkm}")
print (f"Total a pagar: R$ {totalpag}")
print ("-----------------------------")
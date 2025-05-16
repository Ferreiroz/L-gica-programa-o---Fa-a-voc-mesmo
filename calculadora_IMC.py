# CALCULADORA DE IMC
nome= (input("Informe o seu nome: "))
peso =(float(input ("Informe o seu peso: ")))
altura =(float(input("informe a sua altura:")))
imc = peso/(altura*altura)
print(f"O seu IMC é: {imc:.2f}")

if imc<18.5:
    print( "Classificação: Abaixo do peso!")
elif imc>=25.0 and imc<=29.9:
    print("Classificação: Sobrepeso!")
elif imc>=18.5 and imc<=24.9:
    print("Classificação: Peso normal!")
else:
    print("Classificação: Obesidade!")
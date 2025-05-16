print ("---- CONVERSOR DE TEMPERATURA----")
print ("1- Fahrenheit")
print ("2- Kelvin")
print ("3- Sair")
print ("------------------------------")
temperatura= float(input("Informe a temperatura: "))
opcao =0

fahrenheit= (temperatura*9/5)+32
kelvin= temperatura+273.15

while opcao!=3:
   
    opcao=int(input("Escolha uma opção: "))
    if opcao ==1:
        print ("Você escolheu Fahrenheit")
        print (f" O resultado da conversão de Celsius para Fahrenheit é: {fahrenheit}")
    elif opcao ==2:
        print ("Você escolheu Kelvin")
        print (f" O resultado da conversão de Celsius para Kelvin é: {kelvin}")
    elif opcao ==3:
        print ("Finalizado.")
   
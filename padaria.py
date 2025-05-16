frances=0
doce=0
forma=0
integral=0
farofa=0

print("------- CARDÁPIO -------")
print("1- Pão Francês")
print("2- Pão Doce")
print("3- Pão Forma")
print("4- Pão Integral")
print("5- Pão Doce Farofa")
print("6- Finalizar Pedido")
print("-------------------------")

opcao =0
while opcao!=6:
    opcao= int(input("Escolha uma opção: "))
    if opcao ==1:
        frances= int(input(" Você escolheu pão frances,informe quantos pães vai querer:"))
        valorfrances=frances*1.2
    elif opcao ==2:
        doce= int(input(" Você escolheu pão doce,informe quantos pães vai querer:"))
        valordoce=doce*1.08
    elif opcao ==3:
        forma= int(input(" Você escolheu pão de forma,informe quantos pães vai querer:"))
        valorforma=forma*0.95
    elif opcao ==4:
        integral= int(input(" Você escolheu pão integral,informe quantos pães vai querer:"))
        valorintegral=integral*1.04
    elif opcao ==5:
        farofa= int(input(" Você escolheu pão de doce farofa,informe quantos pães vai querer:"))
        valorfarofa=farofa*1.11
    elif opcao ==6:
        print ("Saindo do cardápio.")
        break

print("------- RECIBO -------")
if frances>0:
    print(f"1- Pão Francês = {frances} - Valor: R$ {valorfrances}")
if doce>0:
    print(f"2- Pão Doce = {doce} - Valor: R$ {valordoce}")
if forma>0:
    print(f"3- Pão Forma = {forma} - Valor: R$ {valorforma}")
if integral>0:
    print(f"4- Pão Integral = {integral} - Valor: R$ {valorintegral}")
if farofa>0:
    print(f"5- Pão Doce Farofa = {farofa} - Valor: R$ {valorfarofa}")
print("-----------------------")



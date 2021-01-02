import matplotlib.pyplot as plt
import os
from produto import Produto

# Desenvolvido e arquitetado por Gustavo Lemos dos Santos 

#Variável auxiliar:
aux = 0
#Listas:
listProducts = []
listResults = []
listResultsNames = []

#Quantificando variedade de estoque:
print("\t\t\tANÁLISE DE DADOS DE ESTOQUE\n")
productNumber = float(input("Insira a quantidade dos tipos de produtos existentes:\t"))

#Registrando os objetos produto:
while (aux < productNumber):

    aux = aux + 1

    if (listProducts == []):
        print("Insira as informações dos produtos:\n")
    else:
        print("Insira as informações dos produtos restantes:\n")
    
    #Adicionando atributos do objeto:
    idNumber = aux
    name = input("Insira o nome do produto: \t")
    bruteValue = input("Insira o valor bruto do produto: \t")
    finalValue = input("Insira o valor pelo qual o produto é vendido: \t")
    productSolds = input("Qual a quantidade deste produto vendida neste mês: \t")

    #Construindo objeto
    dados = Produto(idNumber, name, float(bruteValue), float(finalValue), int(productSolds))
    
    #Produto de maior lucro:
    result = dados.productSolds * dados.profit
    maxProfit = 0

    if result > maxProfit:
        maxProfit = result

    #Adicionando elementos nas listas:
    listProducts.append(dados)
    listResults.append(result)
    listResultsNames.append(name)

#switchCases 
def cases(option):
    #Lista de produtos
    if option=="1":
        print("Lista de Produtos:\n [ \n")  
        for produto in listProducts:
            print("{\n")
            print(('\t"id":''"{op}",\n').format(op=produto.idNumber))
            print(('\t"name":''"{op}",\n').format(op=produto.name))
            print(('\t"bruteValue":''"{op}",\n').format(op=produto.bruteValue))
            print(('\t"finalValue":''"{op}",\n').format(op=produto.finalValue))
            print(('\t"profit":''"{op}",\n').format(op=produto.profit))
            print(('\t"productSolds":''"{op}"\n').format(op=produto.productSolds))
            print("\t}\n\a")    
        print("]") 

    #Gráfico de Resultado:    
    elif option=="2":
        print(("A soma total dos lucros é igual a {op1}").format(op1=sum(listResults)))

        #Plotagem do gráfico de produto x lucro:
        plt.title("Resultado dos Lucros Mensal")
        plt.plot(listResultsNames, listResults, 'k--', color="BLACK")
        plt.plot(listResultsNames, listResults, 'go')
        plt.xlabel("Produtos")
        plt.ylabel("Lucro")
        plt.ylim(10.00, 500.00)
        plt.show()

    #Listando sugestões
    elif option=="3":
        balance = sum(listResults)
        totalBruteValue = 0 
        listDesc = sorted(listResults, reverse=True)
        hierarchyNames = []
        aux = 0

        #Neste código são usados 3 arrays que se relacionam com as informações dos produtos
        #para criar uma hierarquia decrescente de sugestões para investimento de estoque do produto mais lucrativo até o menos lucrativo:  
        
        for i in listProducts:
            totalBruteValue = totalBruteValue + (i.bruteValue * i.productSolds)
            x = i.profit * i.productSolds

            for j in listResults:
                if x == j:
                    hierarchyNames.insert( 0 ,i.name)


        #Listando sugestões decrescente:            
        print("\nSujetões de investimento:\n")
        for r in listDesc:
            indexList = aux + 1
            print(("\t{op1} : {op2} com {op3} de lucro!\n").format(op1=indexList,op2= hierarchyNames[aux],op3=r)) 
            aux  = aux + 1

        totalCash = totalBruteValue + balance
        print( ("O total do capital adquirido este mês é de {op1} reais com lucro de {op2}!\n ").format(op1=totalCash,op2=sum(listResults)))    

    #Localizando produto:
    elif option=="4":
        nameFilter = input("\nDigite o nome do produto:\t")
        
        for i in listProducts:
            if i.name == nameFilter :
                print("{\n")
                print(('\t"id":''"{op}",\n').format(op=i.idNumber))
                print(('\t"name":''"{op}",\n').format(op=i.name))
                print(('\t"bruteValue":''"{op}",\n').format(op=i.bruteValue))
                print(('\t"finalValue":''"{op}",\n').format(op=i.finalValue))
                print(('\t"profit":''"{op}",\n').format(op=i.profit))
                print(('\t"productSolds":''"{op}"\n').format(op=i.productSolds))
                print("\t}\n\a")

    #Finalizando programa
    elif option=="5":
        return "Obrigado!"
        
#Loop de menu:
while ( aux != "5"):
    aux = input("\nDigite:\n\t 1-Para visualizar a lista completa de produtos;\n\t 2-Para visualizar informações dos lucros;\n\t 3-Para sugestões de investimento de estoque;\n\t 4-Localizar produto;\n\t 5- Fechar programa. \nOpção: ")
    cases(aux)
    os.system("PAUSE")
    
         
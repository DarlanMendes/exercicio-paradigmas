##Programa desenvolvido por Dedson Darlan
def questao1():
    numero = 10
    print("Questão 01 \n")
    print("Tabela de multiplicação dos números de 1 a 10 \n")
    for i in range(1, numero+1):
        print(f' Tabuada do número {i}')
        for j in range(1, 10+1):
            resultado = i * j
            print(f' - {i} x {j} = {resultado} \n')
def questao2():
    numero_informado = input("Digite um numero inteiro \n")
    qtd_digitos= len(numero_informado)
    print(f' A quantidade de digitos do número informado é {qtd_digitos}')
def questao3():
    numero_informado= int(input("Digite o numero desejado \n"))
    lista= [0,1]
    Fn=1
    for n in range(numero_informado+1):

        if  numero_informado>1 and n > 1:
            Fn = lista[n-1]+lista[n-2]
            lista.append(Fn)
            print(f' o Fn atual é {Fn} ')
        
        if numero_informado<2 and n == numero_informado:
            print(f'O Fn atual é igual a {numero_informado}')

def questao4():
    numero = int(input("Digite o número que deseja obter os números divisores \n"))
    qtd_div=0
    for i in range(1, numero+1):
        eh_div = numero%i
        if eh_div == 0:
            print(f'{i} é divisor de {numero}')
            qtd_div= qtd_div+1
    if qtd_div == 2:
        print(f'Número {numero} é um número primo')
def questao5():
    deseja_continuar= 'S'
    valor_investido = int(input("Digite o valor a ser investido \n"))
    taxa_juros = float(input("Digite a taxa de juros em % \n"))
    taxa_juros = taxa_juros*0.01
    ano = 1
    while deseja_continuar =='S':
         for i in range(12):
            valor_investido = valor_investido+ valor_investido*taxa_juros
         valor_investido = float("{:.2f}".format(valor_investido))
         print(f'Saldo do investimento após {ano} ano(s) é de R$ {valor_investido}')
         deseja_continuar= input("Deseja continuar?(S/N)\n")
         deseja_continuar = deseja_continuar.upper()
         ano+=1

if __name__=="__main__":
    print("Programa desenvolvido por Dedson Darlan \n")
    questao = int(input("Digite a questao que deseja executar \n"))
    if questao ==1:
        questao1()
    elif questao == 2:
        questao2()
    elif questao == 3:
        questao3()
    elif questao == 4:
        questao4()
    else:
        questao5()

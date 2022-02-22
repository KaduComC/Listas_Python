# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja 
# realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

#     par ou ímpar;
#     positivo ou negativo;
#     inteiro ou decimal. 
def checa():
    if result >= 0:
        print('positivo')
        if result % 2 == 0:
            print('par')
            if result % 1 == 0:
                print('inteiro')
            else:
                print('decimal')
        elif result % 2 == 1:
            print('impar')
    elif result < 0:
        print('negativo')

        
nums = input('Valores: ').split()
n1, n2 = map(int, nums)

opcao = str(input('Opções:\n+ - soma\n- - subtração\n/ - divisão\n* - multiplicação\nEscolha: '))

if opcao == '+':
    result = n1 + n2
    print(f'\n{result} {checa()}')
elif opcao == '-':
    result = n1 - n2
    print(f'\n{result} {checa()}')
elif opcao == '*':
    result = n1 * n2
    print(f'\n{result} {checa()}')
elif opcao == '/':
    result = n1 / n2
    print(f'\n{result} {checa()}')
else:
    print('Inválido')




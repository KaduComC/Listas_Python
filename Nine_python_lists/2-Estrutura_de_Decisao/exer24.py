# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja 
# realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

#     par ou ímpar;
#     positivo ou negativo;
#     inteiro ou decimal. 
def operacoes(n1, opcao, n2):
    if opcao == '+':
        return n1 + n2
    elif opcao == '-':
        return n1 - n2
    elif opcao == '*':
        return n1 * n2
    elif opcao == '/':
        return n1 / n2
    else:
        return 'Inválido'

def checa():
    if operacoes() >= 0:
        print('positivo')
        if operacoes() % 2 == 0:
            print('par')
            if operacoes() % 1 == 0:
                print('inteiro')
            else:
                print('decimal')
        elif operacoes() % 2 == 1:
            print('impar')
    elif operacoes() < 0:
        print('negativo')
        
nums = input('Valores: ').split()
n1, n2 = map(int, nums)

opcao = str(input('Opções:\n+ - soma\n- - subtração\n/ - divisão\n* - multiplicação'))
op = operacoes(n1, opcao, n2)
print



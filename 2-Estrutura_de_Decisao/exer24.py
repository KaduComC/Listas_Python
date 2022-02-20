# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja 
# realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

#     par ou ímpar;
#     positivo ou negativo;
#     inteiro ou decimal. 
nums = input('Valores: ').split()
n1, n2 = map(int, nums)

opcao = str(input('Opções:\n+ - soma\n- - subtração\n/ - divisão\n* - multiplicação'))

if opcao == '-':
    r = n1 - n2
    if r % 2 == 0:
        if r >= 0:
            if r % 1 == 0:
                print(f'{n1} - {n2} = {r}\n{r} é par, positivo e inteiro')
            else:
                
# Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando 
# outros símbolos em lugar das letras, como números por exemplo. 
# A própria palavra leet admite muitas variações, como l33t ou 1337. 
# O uso do leet reflete uma subcultura relacionada ao mundo dos jogos de computador e internet, 
# sendo muito usada para confundir os iniciantes e afirmar-se como parte de um grupo. 
# Pesquise sobre as principais formas de traduzir as letras. Depois, faça um programa que 
# peça uma texto e transforme-o para a grafia leet speak.

alfabeto_leet = (('a', '4'), ('b', '3'), ('c', '['), ('d', '|)'), ('e', '&'), ('f', '|='), ('g', '6'), 
    ('h', '|-|'), ('i', '!'), ('j', '_|'), ('k', '|{'), ('l', '1'), ('m', '|v|'), ('n', '//'), 
    ('o', '()'), ('p', '|*'), ('q', '9'), ('r', '|2'), ('s', 'Z'), ('t', '7'), ('u', '|_|'), 
    ('v', '<'), ('w', '\^/'), ('x', '}{'), ('y', '‘/'), ('z','2'))

palavra = str(input('Informe uma palavra ou um texto: '))
nova_palavra = palavra

for letra, leet in alfabeto_leet:
    nova_palavra = nova_palavra.replace(letra, leet)

print(f'\n{nova_palavra}')
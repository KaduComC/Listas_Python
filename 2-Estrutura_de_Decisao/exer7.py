# Faça um Programa que leia três números e mostre o maior e o menor deles. 
nums = []
for i in range(3):
    nums.append(int(input(f'{i + 1} numero: ')))

nums.sort()
print(f'Maio valor é: {nums[2]}\nMenor valor é: {nums[0]}')
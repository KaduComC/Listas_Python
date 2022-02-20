# Faça um Programa que leia três números e mostre-os em ordem decrescente. 
nums = []
for i in range(3):
    nums.append(int(input(f'{i + 1} numero: ')))

nums.sort(reverse = True)
print(nums)
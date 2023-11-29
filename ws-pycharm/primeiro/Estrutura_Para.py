n = int(input("Quantos numeros serao digitados: "))

soma = 0
for i in range(0, n):
    x = int(input("Digite um numero: "))
    soma = soma + x

print("SOMA = ", soma)
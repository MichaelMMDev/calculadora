num1=[int(input('Digite um numero;')),int(input('Digite mais um numero;')),int(input('Digite mais um numero;')),int(input('Digite mais um numero;')),int(input('Digite mais um numero;'))]

num2=input("Digite outro número: ")

if num2 in num1:
    print('ERRO, digite um número que você ainda  não digitou. ')

else:
    print(num1.append(num2))



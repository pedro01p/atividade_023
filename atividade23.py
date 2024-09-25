# Crie um programa que receba um número do usuário e exiba a tabuada desse número de 1 a 10.
n=int(input("digite seu numero"))

for T in range(11):
  print(F"{n} x {T} = {n*T}")
time_1 = input("Digite o nome do primeiro time: ")
time_2 = input("Digite o nome do segundo time: ")
gols_time_1 = int(input("Digite o número de gols que o primeiro time marcou: "))
gols_time_2 = int(input("Digete o número de gols que o segundo time marcou: "))

if gols_time_1 > gols_time_2:
    print(f"o {time_1} ganhou")
elif gols_time_1 < gols_time_2:
    print(f"o {time_2} ganhou")
else:
    print("Deu empate!")

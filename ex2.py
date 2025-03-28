gols_a = int(input("Gols do time A: "))
gols_b = int(input("Gols do time B: "))

if gols_a > gols_b:
    print(f"o time A ganho: {gols_a} x {gols_b}")
elif gols_a < gols_b:
    print(f"Time B ganhou: {gols_a} x {gols_b}")
else:
    print(f"Os dois times empataram {gols_a} x {gols_b}")


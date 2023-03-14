throws = int(input("Введите колличество бросков: "))
eagles = 0
tails = 0
for i in range(throws):
    res = int(input("Введите 0, если выпал орел и 1, если выпала решка: "))
    if res == 0:
        eagles += 1
    else:
        tails += 1
print(f"Необходимо перевернуть {[eagles, tails][tails < eagles]} монет(ы)")
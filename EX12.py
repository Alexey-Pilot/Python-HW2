s, p = int(input("Веедите сумму чисел: ")), int(input("Введите произведение чисел: "))
for i in range(1, p//2):
    if s - i == p / i:
        print(i, s - i)


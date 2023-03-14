s, p = int(input("Веедите сумму чисел: ")), int(input("Введите произведение чисел: "))
for i in range(p//2):
    if i * (s - i) == p:
        print(i, s - i)


numbers = [-5, 3, -2, 8, -1, 4, 10, -3]

for num in numbers:
    if num > 0:
        print("Первый положительный:", num)
        break

last_neg = None
for num in numbers:
    if num < 0:
        last_neg = num

print("Последний отрицательный:", last_neg)
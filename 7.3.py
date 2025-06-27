numbers = [5, 15, -20, 25, 10, -5, 30, 99, 7, 45]

two_digit = []
for num in numbers:
    if 10 <= num <= 99:
        two_digit.append(num)

two_digit.sort()

print("Двузначные положительные числа:", two_digit)
names = ["Анна", "Борис", "Алексей", "Мария", "Арина", "Дмитрий", "Алиса", "Сергей", "Андрей", "Ольга"]

result = []
for name in names:
    if name[0] == 'А':
        result.append(name)

print("Имена на А:", result)
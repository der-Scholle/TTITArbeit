C = 'a'
A = ["apple", "banana", "ana", "cat", "dog", "aha", "aa"]

count = 0
for word in A:
    if len(word) > 1 and word[0] == C and word[-1] == C:
        count += 1

print("Количество подходящих слов:", count)
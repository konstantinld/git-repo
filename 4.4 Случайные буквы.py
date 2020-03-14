# Случайные буквы
# Демонстрирует индексацию строк
import random
word = "индекс"
print("В переменной word хранится слово: ", word, "\n")
hign = len(word)
low = -len(word)
for i in range(10):
    position = random.randrange(low, hign)
    print("word[", position, "]\t", word[position])
input("\n\nНажмите Enter, чтобы выйти.")

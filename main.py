#Ввод
string = input("Введите слово или число: ")
#Разбиваем строку на слова
words = string.split() 
#Разворачиваем слово и добавляем в строку
#Пустая строка
reversed_words = ''
for word in words:
    reversed_words += word[::-1] + ' '
#Удаляем пробелл
print(reversed_words.strip())
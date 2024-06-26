# /* Бинарный поиск работает только в том случае, если список отсортирован.
# Напри мер, и мена в телефонной книге хранятся в алфавитном порядке, и вы
# можете воспользоваться бинарным поиском . А что произойдет, если имена
# не будут отсортированы? */

def binary_search(list, item):  # В переменных low и high хранятся границы той
    # части списка, в которой выполняется поиск
    low = 0
    high = len(list) - 1

    while low <= high:       #Пока эта часть не сократится до одного элемента....
        mid = (low + high)   #...проверяем средний элемент
        guess = list[mid]
        if guess == item:    # Значение найдено
            return mid
        if guess > item:     # Много
            high = mid - 1
        else:                # Мало
            low = mid + 1
    return None              # Значения не существует

my_list = [1, 3, 5, 7, 9]    # ПРОТЕСТИРУЕМ ФУНКЦИЮ!

print(binary_search(my_list, 3))  # => 1     /* Вспомните: нумерация элементов начинается с 0.
#Второй ячейке соответствует индекс 1 */
print (binary_search(my_list, -1) )    # => None  /*None в Python означает "ничто". Это признак
#того, что элемент не найден */

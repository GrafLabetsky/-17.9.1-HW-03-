chain = list(map(int, input("Напишите последовательность чисел через пробел ").split()))

number = int(input("Введите любое число "))

if number % 1 != 0:
   raise ValueError("Введены некорректные  данные. Введите корректное целое число.")

chain.append(number)

for i in range(1, len(chain)):
    n = chain[i]
    idn = i
    while idn > 0 and chain[idn-1] > n:
        chain[idn] = chain[idn-1]
        idn -= 1
    chain[idn] = n
print("Последовательность чисел по возрастанию:", chain)

if number < chain[1]:
    raise ValueError("Введены некорректные данные. Нет числа меньше.")
if number >= chain[-1]:
    raise ValueError("Введены некорректные данные. Нет числа больше.")

def binary_search(chain, number, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if chain[middle] == number:
        return middle
    elif number < chain[middle]:

        return binary_search(chain, number, left, middle - 1)
    else:
        return binary_search(chain, number, middle + 1, right)

print("Номер позиции элемента, который меньше введенного пользователем числа:", (binary_search(chain, number, 0, len(chain)-1))-1)
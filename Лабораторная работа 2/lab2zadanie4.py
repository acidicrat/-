n = int(input("Введите длину списка: "))
index = []
for i in range(0, n):
    index.append(int(input("Введите " + str(i) + " элемент списка: ")))
print(index)
index = [x for x in index if x % 2 != 0]
for k in range(2):
        index.append(int(input("Введите новый элемент списка: ")))
print(index)
a = int(input("Введи число а"+"\n"))
b = int(input("Введи число b"+"\n"))
c = int(input("Введи число c"+"\n"))
d = int(input("Введи число d"+"\n"))
k = int(input("Введи число k"+"\n"))
if b != 0 and a != 0:
    print(abs((a ** 2 - b ** 3 - c ** 3 * a ** 2) * (b - c + c * (k - d / b ** 3)) - ((k / b - k / a) * c) ** 2 - 20000))
else:
    print("На 0 делить нельзя!!!!Замените числа")
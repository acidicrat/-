data = "Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса;_" \
       "Иванов;Семен;" \
       "Игоревич;22 года;Студент 2 курса;"
data = data.split(';_')
for i in range(0, len(data)):
    stroka = data[i]
    stroka = stroka.split(";")
    print(stroka[0]+" "+stroka[1]+" "+stroka[2]+"   "+stroka[3]+"   "+stroka[4])

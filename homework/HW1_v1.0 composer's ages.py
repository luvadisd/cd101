n = int(input("О скольких композиторах Вы хотите узнать? "))
first_name = []
last_name = []
birth = []
death = []
age = []
for i in range(n):
    composer_data = input("Введите имя композитора, его фамилию, дату рождения и смерти через запятую: ").split(", ")
    first_name.append(composer_data[0])
    last_name.append(composer_data[1])
    birth.append(composer_data[2])
    death.append(composer_data[3])

    if int(composer_data[3]) <= 2021:
        continue
    else:
        print("К счастью, композитор жив :)")
        break

for i in range(n):
    count_age = int(death[i]) - int(birth[i])
    print(f"Имя: {first_name[i]}, Фамилия: {last_name[i]}, Возраст {count_age}")
    age.append(count_age)

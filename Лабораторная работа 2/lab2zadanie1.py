slovo = "Митяй, литий, Кирилл, картошечка, лицо, Литва, Рыжик, Ликёр"
slovo = slovo.split(', ')
for i in range(0, len(slovo)):
    if slovo[i][0] == 'Л' and slovo[i][1] == 'и':
        print(slovo[i])
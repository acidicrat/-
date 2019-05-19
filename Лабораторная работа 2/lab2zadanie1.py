slovo = "Митяй, литий, Кирилл, картошечка,Л,ли, лицо, Литва, Рыжик, Ликёр"
slovo = slovo.split(', ')
for i in range(0, len(slovo)):
    if len(slovo) >= 2 and slovo[i][0] == 'Л' and slovo[i][1] == 'и':
        print(slovo[i])
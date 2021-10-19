#39202294215 - 29 февраля 1994
#39202304215 - 30 февраля 1994 !
isik = ''
arvud = []
ikoodid = []

while len(isik) != 11 or isik.isdigit() != True or int(list(isik)[0]) not in [1,2,3,4,5,6]:
    try:
        isik = input('Введите свой личный код: ')
    except:
        ValueError
               
print('Анализ личного кода:'.center(50,' '))

ik_list = list(isik)

#год ik_list[1], ik_list[2]
#месяц ik_list[3], ik_list[4]
#день ik_list[5], ik_list[6]
print('Проверяем месяц: ')
month = int(ik_list[3]+ik_list[4])
day = int(ik_list[5]+ik_list[6])
if month not in range(0,13):
    print(f'{ik_list[3]+ik_list[4]} - месяц неверный')
else:
    print(f'{ik_list[3]+ik_list[4]} - месяц правильный')

    #1,3,5,7,8,10,12 - 31 day
    #2,4,6,9,11 28-29, 30 day
    #1,2 - *18*, 3,4 - *19*, 5,6 - *20* + ik_list[1], ik_list[2]
    if int(ik_list[0]) == 1 or int(ik_list[0]) == 2:
        year = int(f'18{ik_list[1]+ik_list[2]}')
    elif int(ik_list[0]) == 3 or int(ik_list[0]) == 4:
        year = int(f'19{ik_list[1]+ik_list[2]}')
    elif int(ik_list[0]) == 5 or int(ik_list[0]) == 6:
        year = int(f'20{ik_list[1]+ik_list[2]}')

    if month in [1,3,5,7,8,10,12] and day>0 and day<32:
        print(f'{ik_list[5]+ik_list[6]} - правильный день')
    elif (month in [4,6,9,11] and day>0 and day<31) or (month == 2 and day>0 and day<29):
        print(f'{ik_list[5]+ik_list[6]} - правильный день')
    elif year % 4==0 and month == 2 and day>0 and day<30:
        print(f'{ik_list[5]+ik_list[6]} - правильный день, 29 февраля')
    else:
        print(f'{ik_list[5]+ik_list[6]} - неверный день')

    #summa = 1*3 + 2*7 + 3*6 + 4*0 + 5*5 + 6*0 + 7*3 + 8*0 + 9*2 + 1*9
    Summa=0
    for i in range(1,11):
        if i<10:
            Summa+=i*int(ik_list[i-1])
        else:
            Summa+=(i-9)*int(ik_list[i-1])
    print(f'Сумма: {Summa}')
    jaak=Summa//11
    if jaak==10: #II astme kaal: 3 4 5 6 7 8 9 1 2 3
        Summa=0
        for i in range(3,13):
            if i<=9:
                Summa+=(i+2)*int(ik_list[i-3])
            else:
                Summa+=(i-9)*int(ik_list[i-3])
        jaak=Summa//11
    jaak=Summa-jaak*11
    print(f"Контрольный номер: {jaak}")
    if jaak == int(ik_list[10]):
        print('Личный код верный')
    else:
        print('Личный код неверный')
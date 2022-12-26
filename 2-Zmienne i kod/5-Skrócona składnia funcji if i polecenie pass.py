
# Zad 1
price = 123
bonus = 23
bonus_granted = True

print(price - bonus) if bonus_granted else print(price)

# Zad 2
rating = 5
print('very good') if rating == 5 else print('good') if rating == 4 else print('weak')

# Zad 3
today_weekday = 'niedziela'

if today_weekday == 'poniedziałek':
    print('Pomagam mamie')
elif today_weekday == 'wtorek' or today_weekday == 'środa':
    print('Ona ma pranie')
elif today_weekday == 'czwartek':
    print('Mam dyżur')
elif today_weekday == 'piątek':
    print('Mam dwa zebrania')
elif today_weekday == 'sobota':
    print('Ona ma lekcje')
else:
    print('Niedziela jest nasza!')

print('Pomagam mamie') if today_weekday == 'poniedziałek' else \
    print('Ona ma pranie') if today_weekday == 'wtorek' or today_weekday == 'środa' else \
    print('Mam dyżur') if today_weekday == 'czwartek' else print('Mam dwa zebrania') if today_weekday == 'piątek' else \
    print('Ona ma lekcje') if today_weekday == 'sobota' else \
    print('Niedziela jest nasza!')

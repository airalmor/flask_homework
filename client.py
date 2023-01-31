import requests

print('Запрашиваем пока ничего не создано)')
response = requests.get('http://127.0.0.1:5000/adverts/1')

print()

print('Создаем первое объявление')
response = requests.post('http://127.0.0.1:5000/adverts/',
                         json={'advert_title': 'first_advert',
                               'advert_text': 'text of first advert',
                               'owner_name': 'first_owner'},
                         )
print()

print('Запрашиваем опять первое объявление')

response = requests.get('http://127.0.0.1:5000/adverts/1')

print()

print('Создаем второе объявление')

response = requests.post('http://127.0.0.1:5000/adverts/',
                         json={'advert_title': 'user car',
                               'advert_text': 'vw for sale',
                               'owner_name': 'driver'},
                         )
print()

print('Запрашиваем все объявления')
for a in range(5):
    response = requests.get(f'http://127.0.0.1:5000/adverts/{a}')
    print(response.json())
print()
print('Удаляем 1ое объявление')
response = requests.delete('http://127.0.0.1:5000/adverts/1')
print()
print(' Запрашиваем все объявления')
for a in range(5):
    response = requests.get(f'http://127.0.0.1:5000/adverts/{a}')
    print(response.json())

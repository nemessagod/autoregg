import requests
from bs4 import BeautifulSoup

registration_url = 'https://www.njuskalo.hr/registracija/kupac/' 

payload = {
    'username': 'Pedik1120', 

    'email': 'your_email@example.com', 

    'password': '1828281991@@', 
}

with requests.Session() as session:
   
    response = session.get(registration_url)
    

    # soup = BeautifulSoup(response.text, 'html.parser')
    # csrf_token = soup.find('input', {'name': 'csrf_token'})['value']
    # payload['csrf_token'] = csrf_token 
   
    response = session.post(registration_url, data=payload)

    if response.status_code == 200:
        print('Регистрация прошла успешно!')
    else:
        print('Ошибка при регистрации:', response.status_code)
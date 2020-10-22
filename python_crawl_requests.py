import requests
import json

sesions = requests.session()
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
reponse = sesions.post('https://masothue.vn/Ajax/Token',
                       data={'r': '3afxey'},
                       headers=headers)
token = json.loads(reponse.text)['token']
reponse = sesions.post('https://masothue.vn/Ajax/Search',
                       headers=headers,
                       data={'q': '152008390', 'token': token})
print(reponse.text)




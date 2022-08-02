# requests 사용 예시 2

import requests


URL = 'https://api.agify.io?name=michael&country_id=KR' # 뒤에 name=value 쌍으로 보냄. 여러개보낼 때는 & 사용
response = requests.get(URL).json()

# params = {
#     'name': 'michael',
#     'country_id': 'KR',
# }

# response = requests.get(URL, params=params).json()

print(response)

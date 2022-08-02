import requests
from pprint import pprint


def credits(title):
    pass 
    # 여기에 코드를 작성합니다.
    try:  
        URL = 'https://api.themoviedb.org/3/search/movie'
        params = {
        'api_key': 'd22723de725ed26097abc1505eb3c74c',
        'language': 'ko',
        'query': title
        }
        response = requests.get(URL,params=params).json()
        movie_id = response['results'][0]['id']
        URL_2 = f'https://api.themoviedb.org/3/movie/{movie_id}/credits'
        params = {
        'api_key': 'd22723de725ed26097abc1505eb3c74c',
        'language': 'ko',
        }
        response_2 = requests.get(URL_2,params=params).json()

        
        return {'cast':[person['name'] for person in response_2['cast'] if person['cast_id']<10], 'directing':[person['name'] for person in response_2['crew'] if person['department']=='Directing']}

    except:
        return None

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None

import requests


def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
    URL = 'https://api.themoviedb.org/3/movie/popular'

    params = {
    'api_key': 'd22723de725ed26097abc1505eb3c74c',
    'language': 'ko',
    'page': '1'
    }
    response = requests.get(URL,params=params).json()
    return len(response['results'])

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20

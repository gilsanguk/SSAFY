import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.  

    new_data = []
    for k in range(len(movies)):
        genre_names = [] 
        for j in range(len(movies[k]['genre_ids'])):
            for i in genres:
                if i['id'] == movies[k]['genre_ids'][j]:
                    genre_names.append(i['name'])
        data = {
        'id': movies[k].get('id'),
        'title': movies[k].get('title'),
        'poster_path': movies[k].get('poster_path'),
        'vote_average': movies[k].get('vote_average'),
        'overview': movies[k].get('overview'),
        'genre_names' : genre_names
        }
        new_data.append(data)
    return new_data  

        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))

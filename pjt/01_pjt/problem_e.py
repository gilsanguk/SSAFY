import json


def dec_movies(movies):
    pass 
    # 여기에 코드를 작성합니다.  
    dec_lst=[]
    for movie in movies:
        id = movie.get('id')
        data = open(f'data/movies/{id}.json', encoding='utf-8')
        new_data = json.load(data)
        revenue_dct = {'title': new_data.get('title'),'release_date': new_data.get('release_date')}
        if revenue_dct['release_date'][5:7] == '12':
            dec_lst.append(revenue_dct['title'])
    return dec_lst

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))

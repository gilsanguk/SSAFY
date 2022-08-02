import json


def max_revenue(movies):
    pass 
    # 여기에 코드를 작성합니다.  
    max_value= 0
    for movie in movies:
        id = movie.get('id')
        data = open(f'data/movies/{id}.json', encoding='utf-8')
        new_data = json.load(data)
        revenue_dct = {'title': new_data.get('title'),'revenue': new_data.get('revenue')}
        if revenue_dct['revenue'] > max_value:
            max_value = revenue_dct['revenue']
            movie_title = revenue_dct
    return movie_title['title']
 
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))

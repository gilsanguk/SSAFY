# open 및 json 모듈 사용예시

import json
from pprint import pprint

movie = open('sample.json', encoding='utf-8')
movie_detail = json.load(movie)
file = open('newfile.json', 'w', encoding='utf-8')
json.dump(movie_detail, file)
pprint(movie_detail)

import codecs
from search_engine.parser import *

parsers = (
    (head_hunter, 'https://persianovskiy.hh.ru/search/vacancy?text=python&from=suggest_post&area=1'),
    (habr_career, 'https://career.habr.com/vacancies?locations%5B%5D=c_726&q=java&type=all')
)

jobs, errors = [], []

for func, url in parsers:
    j, e = func(url)
    jobs += j
    errors += e

file_handler = codecs.open('vacancies.txt', 'w', 'utf-8')
file_handler.write(str(jobs))
file_handler.close()

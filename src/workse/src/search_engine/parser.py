from bs4 import BeautifulSoup as BS
import requests
import codecs
from random import choice

__all__ = ('head_hunter', 'habr_career')

headers = [
    {'User-Agent': 'Mozilla/7.0 (Windows 7; rv:61) Gecko/30125361 Firefox/61.0',
     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 'Google/14.0 (Windows 11.1; rv:141) Adamonica/15168293 Chrome/141.2',
     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 'KIPA BROWSER/14.88 (KIPA OS 13.37; rv:1488) BipolarOchka/15168293 Chrome/14.88',
     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 'Amigo/3.0 (Windows XP; rv:15) Amigo/15168293 Amigo/15',
     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
]


# TODO: Memory clean.
def head_hunter(url, city=None, specialization=None):
    jobs = []
    errors = []

    if url:
        resp = requests.get(url, headers=choice(headers))

        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            div_list = soup.find('div', attrs={'class', 'vacancy-serp-content'})
            if div_list:
                vacancy_card = soup.find_all('div', attrs={'class': 'serp-item'})
                for card in vacancy_card:
                    title = card.find('h3')
                    href = title.a['href']
                    company = card.find('div', attrs={'class': 'vacancy-serp-item__meta-info-company'})
                    description = card.find('div', attrs={'class': 'g-user-content'})
                    if description:
                        jobs.append({
                            'title': title.text,
                            'company': company.text,
                            'description': description.text,
                            'url': href,
                            'city_id': city,
                            'specialization_id': specialization
                        })
                    else:
                        jobs.append({
                            'title': title.text,
                            'company': company.text,
                            'description': '???????????????? ??????????????????????',
                            'url': href,
                            'city_id': city,
                            'specialization_id': specialization
                        })
            else:
                errors.append({
                    'error_text': '???? ???????????? ?????????????? div',
                    'is_redirect': resp.is_redirect,
                    'time': resp.headers['Set-Cookie'].split(';')[4][0:38],
                    'connection_method': resp.request,
                    'url': resp.url,
                })
        else:
            errors.append({
                'error_code': resp.status_code,
                'error_text': '???????????????? ???? ????????????????',
                'time': resp.headers['Set-Cookie'].split(';')[4][0:38],
                'connection_method': resp.request,
                'url': resp.url,
            })

    return jobs, errors


# TODO: Memory clean.
def habr_career(url, city=None, specialization=None):
    domain = 'https://career.habr.com'
    jobs = []
    errors = []

    resp = requests.get(url, headers=choice(headers))

    if url:
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            new_vacancies = soup.find('div', attrs={'class': 'no-content'})
            if not new_vacancies:
                div_list = soup.find('div', attrs={'class', 'section-group section-group--gap-medium'})
                if div_list:
                    vacancy_card = soup.find_all('div', attrs={'class': 'vacancy-card'})
                    for card in vacancy_card:
                        title = card.find('a', attrs={'class': 'vacancy-card__title-link'})
                        href = title['href']
                        company = card.find('a', attrs={'class': 'link-comp link-comp--appearance-dark'})
                        # TODO: ???????????????? ???? ???????????????? ???????????????? ?? ?????????? ???????????? ????????????????.
                        description_list = card.find_all('a', attrs={'class': 'link-comp link-comp--appearance-dark'})
                        description_list.pop(0)
                        description = ''
                        for el in description_list:
                            description += ' | ' + el.text

                        jobs.append({
                            'title': title.text,
                            'company': company.text,
                            'description': description,
                            'url': domain + href,
                            'city_id': city,
                            'specialization_id': specialization
                        })

                else:
                    errors.append({
                        'error_text': '???? ???????????? ?????????????? div',
                        'is_redirect': resp.is_redirect,
                        'time': resp.headers['Set-Cookie'].split(';')[4][0:38],
                        'connection_method': resp.request,
                        'url': resp.url,
                    })
            else:
                errors.append({
                    'error_text': '???????????????? ?????????? (?????? ???????????????? ???? ???????????? ????????????????)',
                    'connection_method': resp.request,
                    'url': resp.url,
                })
        else:
            errors.append({
                'error_code': resp.status_code,
                'error_text': '???????????????? ???? ????????????????',
                'time': resp.headers['Set-Cookie'].split(';')[4][0:38],
                'connection_method': resp.request,
                'url': resp.url,
            })

    return jobs, errors


if __name__ == '__main__':
    url = 'https://hh.ru/search/vacancy?text=Javascript+developer&from=suggest_post&salary=&clusters=true' \
          '&ored_clusters=true&enable_snippets=true '
    jobs, errors = head_hunter(url)

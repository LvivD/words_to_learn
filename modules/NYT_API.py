def get_an_article_url():
    from urllib import request
    import json

    sections = 'arts, automobiles, books, business, fashion, food, health, home, insider, magazine, movies, national, nyregion, obituaries, opinion, politics, realestate, science, sports, sundayreview, technology, theater, tmagazine, travel, upshot, world'.split(', ')

    for elem in sections:
        print(elem)  # should be replaced

    chosen_section = input('Chose the section you want: ')
    api_key = 'HPlFltAhd0Lj1Q4XYUvH644w1cPk2XDz'

    url = '''https://api.nytimes.com/svc/topstories/v2/{0}.json?api-key={1}'''.format(chosen_section, api_key)

    r = request.urlopen(url)
    data = r.read().decode()
    # print(type(data))

    with open('tests/nyt_example.json', 'w', encoding='utf-8') as file:
        file.write(data)

    data = json.loads(data)

    url_list = []
    for i in range(10):
        url_list.append(data['results'][i]['url'])
    return url_list
if __name__ == '__main__':
    print(get_an_article_url())

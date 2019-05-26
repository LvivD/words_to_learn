def get_articles_url():
    """
    Function gets list of urls (two url from every category of NYT magazine).
    :return: list of urls
    :rtype: list
    """
    from urllib import request
    import json
    from time import sleep

    # All sections in NYT
    sections = 'arts, ' \
               'automobiles, ' \
               'books, ' \
               'business, ' \
               'fashion, ' \
               'food, ' \
               'health, ' \
               'home, ' \
               'insider, ' \
               'magazine, ' \
               'movies, ' \
               'national, ' \
               'nyregion, ' \
               'obituaries, ' \
               'opinion, ' \
               'politics, ' \
               'realestate, ' \
               'science, ' \
               'sports, ' \
               'sundayreview, ' \
               'technology, ' \
               'theater, ' \
               'tmagazine, ' \
               'travel, ' \
               'upshot, ' \
               'world'.split(', ')

    # Personal API-key
    api_key = 'HPlFltAhd0Lj1Q4XYUvH644w1cPk2XDz'
    url_list = []

    for chosen_section in sections:
        print('got a url list')
        # Should do that not to have TooManyResponsesError
        sleep(5)

        url = '''https://api.nytimes.com/svc/topstories/v2/{0}.json?api-key={1}'''.format(chosen_section, api_key)

        try:
            r = request.urlopen(url)
            data = r.read().decode()
            data = json.loads(data)
        except Exception as exc:
            print(exc)
            data = ''

        for i in range(2):                            # Getting 2 articles of each category.
            url_list.append(data['results'][i]['url'])
    return url_list


if __name__ == '__main__':
    print(get_articles_url())

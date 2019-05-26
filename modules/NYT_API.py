def get_an_article_url(section=None, num_of_articles_to_study=1):
    """

    :param section:
    :param num_of_articles_to_study:
    :return:
    """
    from urllib import request
    import json

    # To input section manually.
    if section is None:

        # All sections available at NTY
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

        for elem in sections:
            print(elem)

        chosen_section = input('Chose the section you want: ')
    else:
        chosen_section = section

    # This part was copied from NYT API documentation examples.

    # Personal API-key
    api_key = 'HPlFltAhd0Lj1Q4XYUvH644w1cPk2XDz'

    url = '''https://api.nytimes.com/svc/topstories/v2/{0}.json?api-key={1}'''.format(chosen_section, api_key)

    r = request.urlopen(url)
    data = r.read().decode()
    data = json.loads(data)

    url_list = []
    for i in range(num_of_articles_to_study):
        url_list.append(data['results'][i]['url'])
    return url_list


if __name__ == '__main__':
    print(get_an_article_url())

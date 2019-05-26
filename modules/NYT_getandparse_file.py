import modules.NYT_API as NYT_API
from urllib import request
from classes.HTMLparse import MyHTMLParser


def parse_article(url):
    """
    Function that is parsing the article and creating a list of all it's words.

    :param url: article url.
    :type url: str
    :return: list of words
    :rtype: list
    """
    resp = request.urlopen(url)
    if resp.code == 200:
        data = resp.read().decode()

        # deleting useless parts
        data = data[data.index('<body>'): data.index('</body>')]
        data = data[:data.index('<script>')]
        if 'A version of this article appears in print on' in data:
            data = data[:data.index('A version of this article appears in print on')]
        elif ('Advertisement' in data) and ('Advertisement' in data[:data.index('Advertisement')]):
            data = data[:(data[::-1].index('tnemesitrevdA') * (-1) - 1)]

        parser = MyHTMLParser()
        parser.feed(data)

        # To make lower all words an the beginning of the sentences.
        article = str(parser.container) \
            .replace('. ', ' .') \
            .replace('\n', '\n.') \
            .replace('! ', ' .') \
            .replace('? ', ' .') \
            .replace('; ', ' .') \
            .replace(',', '') \
            .replace(':', '') \
            .replace('—', '') \
            .replace('|', '')

        article = article.split()
        for word_num in range(len(article)):
            if article[word_num]:
                first_char = article[word_num][0]
                if first_char == '.':
                    article[word_num] = article[word_num][1:].lower()
    else:
        print(resp.code)
        article = []

    return article


def get_words(sphere, num_of_articles_to_study=1):
    """
    Function to get one list of words for all articles that should be read.

    :param sphere: topic on which articles should be parsed. (One od NYT spheres)
    :type sphere: str
    :param num_of_articles_to_study: number of articles to parse
    :type num_of_articles_to_study: int
    :return: list of all words
    :rtype: list
    """
    article_list = NYT_API.get_an_article_url(sphere, num_of_articles_to_study)
    word_list = []

    for article_url in article_list:
        word_list += parse_article(article_url)

    return word_list

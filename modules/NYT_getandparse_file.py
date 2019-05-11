def get_words():
    import NYT_API
    from urllib import request
    from html.parser import HTMLParser
    
    class MyHTMLParser(HTMLParser):

        container = ''
        separator = '\n'
        def handle_starttag(self, tag, attrs):
            if tag == 'a':
                self.separator = ' '
            else:
                self.separator = '\n'
            # print("Encountered a start tag:", tag)

        def handle_endtag(self, tag):
            pass
            # print("Encountered an end tag :", tag)

        def handle_data(self, data):
            self.container += data + self.separator
            # print("Encountered some data  :", data)

    def parse_article(url):
        resp = request.urlopen(url)
        # print(resp.code)
        if resp.code == 200:
            data = resp.read().decode()

            # just to look at article
            # with open('tests/nyt_article_example.html', 'w', encoding='utf-8') as file:
            #     file.write(data)

            # deleting useless parts
            data = data[data.index('<body>'): data.index('</body>')]
            data = data[:data.index('<script>')]
            if 'A version of this article appears in print on' in data:
                data = data[:data.index('A version of this article appears in print on')]
            elif ('Advertisement' in data) and ('Advertisement' in data[:data.index('Advertisement')]):
                data = data[:(data[::-1].index('tnemesitrevdA')*(-1) - 1)]

            parser = MyHTMLParser()
            parser.feed(data)
            # only to see results
            # with open('tests/nyt_data.txt', 'w', encoding='utf-8') as file:
            #     file.write(parser.container)

            article = str(parser.container)\
                .replace('. ', ' .')\
                .replace('\n', '\n.')\
                .replace('! ', ' .')\
                .replace('? ', ' .')\
                .replace('; ', ' .')\
                .replace(',', '')\
                .replace(':', '')\
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

        return article

    article_list = NYT_API.get_an_article_url()
    print('got_arcticles_list')
    word_list = []

    i = 1
    for article_url in article_list:
        print(i)
        word_list += parse_article(article_url)
        i+=1

    return word_list

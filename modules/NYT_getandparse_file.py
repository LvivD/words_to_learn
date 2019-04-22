import NYT_API

from urllib import request

resp = request.urlopen(NYT_API.get_an_article_url())
# print(resp.code)
if resp.code == 200:
    data = resp.read().decode()


with open('tests/nyt_article_example.html', 'w', encoding='utf-8') as file:
    file.write(data)

data = data[data.index('<body>'): data.index('</body>')]
data = data[:data.index('<script>')]
if 'A version of this article appears in print on' in data:
    data = data[:data.index('A version of this article appears in print on')]
elif ('Advertisement' in data) and ('Advertisement' in data[:data.index('Advertisement')]):
    data = data[:(data[::-1].index('tnemesitrevdA')*(-1) - 1)]

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    conteiner = ''
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
        self.conteiner += data + self.separator
        # print("Encountered some data  :", data)

parser = MyHTMLParser()
parser.feed(data)
with open('tests/nyt_data.txt', 'w', encoding='utf-8') as file:
    file.write(parser.conteiner)
# print(parser.conteiner)

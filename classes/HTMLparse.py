from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    """
    Simple class to parse html pages.
    Copied from html.parser documentation example.
    """
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
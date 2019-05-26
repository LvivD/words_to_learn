from modules.get_most_used_words.get_articles_url import get_articles_url
from modules.NYT_getandparse_file import parse_article
from classes.dict_class import WordsDict
import time


def main():
    """
    Function parse 52 articles on different to get most used words and save them.

    Creates most_used_words.list in 'files' folder.
    """
    num_of_words = 0
    t = time.time()

    # Creating the dictionaries.
    dictionary = WordsDict()

    i = 1
    for url in get_articles_url():
        tt = time.time()
        print("Articles number ", i)
        i += 1
        list_of_words = parse_article(url)
        num_of_words += len(list_of_words)

        print(time.time() - tt)
        for word in list_of_words:
            dictionary.append(word)
        print('Words in article:', len(list_of_words))
        print('Time spend to parse article:', time.time() - tt, time.time() - t)

    print(time.time() - t)
    print(num_of_words)
    print(len(dictionary))

    with open('files/most_used_words.list', 'w') as write_file:
        for word in dictionary.get_list_of_n_words(1000):
            write_file.write(word + '\n')

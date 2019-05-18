from dict_class import WordsDict
import NYT_getandparse_file


def get_dict(sphere, words_to_return=100, num_of_articles_to_study=1):
    """
    The function get the words from articles
    :param sphere:
    :param words_to_return:
    :return:
    """
    words = NYT_getandparse_file.get_words(sphere, num_of_articles_to_study)
    word_dict = WordsDict(words)

    list_of_words = []
    for word in word_dict:
        try:
            if not word[0].isupper():
                list_of_words.append(word)
            else:
                print(word)
        except IndexError:
            pass

    return list_of_words[:words_to_return]

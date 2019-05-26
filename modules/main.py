from classes.dict_class import WordsDict
import modules.NYT_getandparse_file as NYT_getandparse_file


def get_dict_from_NYT(sphere, num_of_words_to_return=100, num_of_articles_to_study=1):
    """
    The function gets the words from articles on specific theme, pares it, filter mainly known words
     and returns the number of words which occur most often and weren't deleted.

    :param sphere: the sphere on which articles should be read.
    :type sphere: str
    :param num_of_words_to_return: the number of words that should be returned
    :type num_of_words_to_return: int
    :param num_of_articles_to_study: the number of articles that should be read
    :type num_of_articles_to_study: int
    :return: list of words
    :rtype: list
    """

    def last_check(lst):
        """
        Deletes all words that have not alphabetic signs.

        :param lst: list of words.
        :type lst: list
        :return: list of only alphabetic words
        :rtype: list
        """
        i = 0
        while len(lst) > i:
            if not lst[i].isalpha():
                lst.pop(i)
            else:
                i += 1

        return lst

    words = NYT_getandparse_file.get_words(sphere, num_of_articles_to_study)

    # Deleting all well known words.
    with open('files/most_used_words.list', 'r') as most_used_words_file:
        m_u_w = []
        for line in most_used_words_file:
            m_u_w.append(line[:-1])

    word_dict = WordsDict()
    for word in words:
        word_dict.append(word)
    print(m_u_w[:20])
    word_dict = word_dict - m_u_w
    print(word_dict[:10])
    list_of_words = []
    for word in word_dict:
        try:
            if not word[0].isupper():
                list_of_words.append(word)
            else:
                pass
        except IndexError:
            pass

    list_of_words = last_check(list_of_words)

    return list_of_words[:num_of_words_to_return]

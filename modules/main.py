from dict_class import WordsDict
import NYT_getandparse_file

words = NYT_getandparse_file.get_words()
word_dict = WordsDict(words)
# print(word_dict.get_first_n_words(100))

list_of_words = []
for word in word_dict:
    list_of_words.append(word)

print(list_of_words[:100])

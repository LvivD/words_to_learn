from dict_class import WordsDict, Word

from unittest import TestCase, main


class TestPoint(TestCase):

    def setUp(self):
        self.word1 = Word('baby')
        self.word2 = Word('cow')
        self.word3 = Word('cow')
        self.word3.amount = 100500
        self.dict1 = WordsDict()
        self.dict2 = WordsDict(['a', 'b', 'c', 'd'])
        self.dict3 = WordsDict(['a', 'b', 'c', 'd', 'a', 'a', 'b'])

    def test_word_type(self):
        self.assertEqual(type(self.word1), Word, "Wrong type of the word")
        self.assertEqual(type(Word('')), Word, "Wrong type of the word")

    def test_word_amount(self):
        self.assertTrue(self.word1.amount == 1, "Wrong number of words")
        self.assertTrue(Word('').amount == 1, "Wrong number of words")
        word3 = Word('abc')
        word3.amount += 1
        self.assertTrue(word3.amount == 2, "Wrong number of words")

    def test_word_eq(self):
        self.assertFalse(self.word1 == self.word2, "Different words are equal")
        self.assertTrue(self.word1 == Word('baby'), "Equal words are different")
        self.assertEqual(self.word2, self.word3, "Equal words are different")

    def test_word_repr(self):
        self.assertFalse(str(self.word1) == str(self.word2), "Two different words have same representation")
        self.assertTrue(str(self.word1) == str(Word('baby')), "Two same words have different representation")
        self.assertFalse(str(self.word2) == str(self.word3), "Two different words have same representation1")
        self.assertEqual(str(self.word2), '(cow, 1)', "Wrong representation")

    def test_dict_type(self):
        self.assertEqual(type(self.dict1), WordsDict, "Wrong type of the dictionary")
        self.assertEqual(type(WordsDict()), WordsDict, "Wrong type of the dictionary")
        self.assertEqual(type(WordsDict([1,2,3])), WordsDict, "Wrong type of the dictionary")
        self.assertEqual(type(self.dict2), WordsDict, "Wrong type of the dictionary")

    def test_dict_len(self):
        self.assertEqual(len(self.dict1), 0, "Wrong len of the dict")
        self.assertEqual(len(self.dict2), 4, "Wrong len of the dict")
        self.assertEqual(len(self.dict3), 4, "Wrong len of the dict")

    def test_dict_contains(self):
        self.assertTrue('a' in self.dict2, "Wrong contains function")
        self.assertFalse('a' in self.dict1, "Wrong contains function")
        self.assertTrue('a' in self.dict3, "Wrong contains function")
        self.assertFalse('' in self.dict2, "Wrong contains function")
        self.assertTrue(Word('a') in self.dict2, "Wrong contains function")

    def test_dict_append(self):

        a = WordsDict()
        a.append('a')
        b = WordsDict('a')
        for word in a:
            self.assertTrue(word in b, "Words are appended badly")

        a = WordsDict()
        for word in self.dict3:
            a.append(word)
        for word in a:
            self.assertTrue(word in self.dict2, "Words are appended badly")

    def test_dict_get_words(self):
        self.assertEqual(self.dict1.get_first_n_words(100), [], "Wrong words")
        self.assertEqual(self.dict2.get_first_n_words(4), [Word('a'), Word('b'), Word('c'), Word('d')], "Wrong words")
        a = Word('a')
        a.amount = 3
        b = Word('b')
        b.amount = 2
        self.assertEqual(self.dict3.get_first_n_words(2), [a, b], "Wrong words")


if __name__ == "__main__":
    main()


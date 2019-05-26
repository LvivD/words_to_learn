class WordsDict:
    """
    Class for saving and getting word that meets more often.
    """
    def __init__(self, lst=[]):
        """
        Initialization of the dictionary.
        :param lst: the list that should be written to the dictionary.
            (It shouldn't be big, better to add words one by one).
        :type lst: list
        """

        if lst:
            self.lst = [Word(lst[0])]
            self.len = 1
            for elem in lst[1:]:

                i = 0
                while i < self.len - 1 and self.lst[i] != Word(elem):
                    i += 1

                if self.lst[i] == Word(elem):
                    self.lst[i].amount += 1
                else:
                    self.len += 1
                    self.lst.append(Word(elem))
            self.lst.sort(key=lambda x: x.amount, reverse=True)
        else:
            self.lst = []
            self.len = 0

    def __contains__(self, item):
        """
        The contains method.
        :param item: item to find in the dictionary.
        :type item: Word or any other (if other it will be transformed to Word object)
        :return: if item is in dictionary
        :rtype: bool
        """
        if type(item) == Word:
            return item in self.lst
        else:
            return Word(item) in self.lst

    def __len__(self):
        """
        Length method
        :return: number of different words
        :rtype: int
        """
        return self.len

    def append(self, item):
        """
        Method to add words to the dictionary.
        It's the way how the dictionary should be formed.
        :param item: The item that should be added
        :type item: any type
        :return: None
        """
        if Word(item) in self.lst:
            k = 0
            while k < self.len:
                if self.lst[k] == Word(item):
                    self.lst[k].amount += 1
                    i = k
                k += 1
            if i == 0:
                # print("first elem")
                pass
            elif self.lst[i-1].amount < self.lst[i].amount:
                j = i - 1
                while self.lst[j].amount < self.lst[i].amount and j != -1:
                    j -= 1
                self.lst[i], self.lst[j+1] = self.lst[j+1], self.lst[i]
            else:
                # print('correct pos')
                pass
        else:
            self.lst.append(Word(item))
            self.len += 1

    def get_first_n_words(self, n):
        """
        Method to get the list of n Word objects that meet more often .
        :param n: number of objects to return
        :type n: int
        :return: list of Word objects, length of the list is n
        :rtype: list
        """
        return self.lst[:n]

    def get_list_of_n_words(self, n):
        """
        Method to get the list of words that meet more often .
        :param n: number of words to return
        :type n: int
        :return: list, length of the list is n
        :rtype: list
        """
        i = 0
        lst = []
        if n > len(self):
            n = len(self)
        while i < n:

            lst.append(self.lst[i].item)
            i += 1

        return lst

    def __sub__(self, other):
        """
        Method to get the list of words without words that are in other list.
        Raises TypeError if the type of other is not list.

        :param other: list of words that shouldn't be in final list
        :type other: list
        :return: list of words in the dictionary without words from other list.
        :rtype: list
        """
        if type(other) != list:
            print(type(other))
            raise TypeError('cant subtract that type')
        lst = self.get_list_of_n_words(len(self))
        i = 0
        for word in other:
            try:
                i += 1
                lst.remove(word)
            except ValueError:
                # print(word, 'removed')
                pass

        print('length: ', i)
        return lst

    def __iter__(self):
        """
        Method to iterate WordDict.
        :return: word one by one
        :rtype: any type (not Word object)
        """
        for word in self.lst:
            yield word.item


class Word:
    """
    Class to save word and the number of it's repeats in dictionary.
    """
    def __init__(self, item):
        """
        Initialisation of the word.
        :param item: the word itself
        """
        self.item = item
        self.amount = 1

    def __eq__(self, other):
        """
        Equal method. Return True if whe words are the same, does not pay attention to amount attribute.
        :param other: other Word object to compare with
        :return: if two words are the same.
        :rtype: bool
        """
        return self.item == other.item

    def __repr__(self):
        """
        Representation of the word.
        :return: string with the word and it's amount in dictionary.
        :rtype: str
        """
        return "(" + str(self.item)+", " + str(self.amount) + ")"

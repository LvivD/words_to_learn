class WordsDict:
    def __init__(self, lst=[]):
        self.lst = []
        self.len = 0
        for elem in lst:
            if Word(elem) in self.lst:
                i = 0
                while i < self.len:
                    if self.lst[i] == Word(elem):
                        self.lst[i].amount += 1
                    i += 1
            else:
                self.len += 1
                self.lst.append(Word(elem))
        self.lst.sort(key=lambda x: x.amount, reverse=True)

    def __contains__(self, item):
        if type(item) == Word:
            return item in self.lst
        else:
            return Word(item) in self.lst

    def append(self, item):

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
        return self.lst[:n]


class Word:
    def __init__(self, item):
        self.item = item
        self.amount = 1

    def __eq__(self, other):
        return self.item == other.item

    def __repr__(self):
        return "(" + str(self.item)+", " + str(self.amount) + ")"


# obj1 = WordsDict([3, 5, 4, 2, 4, 3, 2, 4])
# print(obj1.lst)
#
# print(2 in obj1)
# print(obj1.lst)
# obj1.append(5)
# print(obj1.lst)
# obj1.append(5)
# print(obj1.lst)
if __name__ == "__main__":
    with open('tests/nyt_data.txt', encoding='utf-8') as file:

        a = file.readlines()
    b = WordsDict()
    for line in a:
        for word in line.split():
            b.append(word.lower())
            # print(b.lst)
            # input()
    print(b.get_first_n_words(30))
    # print(b.lst)
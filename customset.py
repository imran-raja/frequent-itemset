class myCustomSet:
    def __init__(self, *args):
        self._dict = {}
        for arg in args:
            self.myadd(arg)

    def myadd(self, item):
        if isinstance(item, list):
            for i in item:
                self._dict[i] = i
        else:
            self._dict[item] = item


    def myremove(self, item):
        del self._dict[item]

    def __iter__(self):
        return iter(self._dict.copy(  ))

    def __len__(self):
        return len(self._dict)


    def myunion(self, s2):
        temp = myCustomSet()
        for i in self:
            temp.myadd(i)
        for i in s2:
            if not i in self:
                temp.myadd(i)
        return temp

    def mydiff(self, set):
        temp = myCustomSet()
        for i in self:
            temp.myadd(i)
        for i in set:
            if i in temp:
                temp.myremove(i)
        return temp



# a = list((frozenset([1, 2, 3, 4])))
# b = list(frozenset([1, 2, 3, 5, 6]))
# x = Set(a)
# y = Set(b)
# #
# # print x
# z = y.union(x)
# print z

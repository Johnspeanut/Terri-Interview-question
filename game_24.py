class Judge24(object):
    def judge24(self, cards):
        if len(cards) == 1:
            return abs(cards[0] - 24) < 0.1
        for i, a in enumerate(cards):
            for j, b in enumerate(cards):
                if i == j:
                    continue
                keepList = [cards[k]
                            for k in range(len(cards)) if k != i and k != j]
                lookupAdditionList = [a+b, a-b, a*b]
                if b != 0:
                    lookupAdditionList.append(float(a)/b)
                if a != 0:
                    lookupAdditionList.append(float(b)/a)
                for x in lookupAdditionList:
                    if self.judge24(keepList+[x]):
                        return True
        return False

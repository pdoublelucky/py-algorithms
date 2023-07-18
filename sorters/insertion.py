from comparison_based_sorter import ComparisionBasedSorter

class InsertionSorter(ComparisionBasedSorter):
    def __init__(self, collection) -> None:
        super().__init__(collection)

    def _insertion_sort(self):
        for outer_idx in range(1,len(self.datas)):
            for inner_idx in range(outer_idx,0,-1):
                if self._isLess(inner_idx,inner_idx-1):
                    self._exchange(inner_idx,inner_idx-1)

    def sort(self,flag='F'):
        if flag == 'F':
            self._insertion_sort()
        elif flag == 'R':
            pass

if __name__ == "__main__":
    t1 = [5,2,10,-1,12,22,51,19,24,42]
    t2 = "to be or not that is a question"
    s = InsertionSorter(t2)
    s.sort()
    print(s.datas)
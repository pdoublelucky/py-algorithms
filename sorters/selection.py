from comparison_based_sorter import ComparisionBasedSorter

class SelectionSorter(ComparisionBasedSorter):
    def __init__(self, collection) -> None:
        super().__init__(collection)

    def __selection_sort(self):
        for outer_idx,_ in enumerate(self.datas):
            min_idx = outer_idx
            for inner_idx,_ in enumerate(self.datas[outer_idx+1:],outer_idx+1):
                if(self._isLess(inner_idx,min_idx)):
                    min_idx = inner_idx
            self._exchange(outer_idx,min_idx)
    
    def sort(self,flag='F'):
        if flag == 'F':
            self.__selection_sort()
        elif flag == 'R':
            pass
            

if __name__ == "__main__":
    # t1 = [5,2,10,-1,12,22,51,19,24,42]
    t2 = "to be or not that is a question"
    s = SelectionSorter(t2)
    s.sort()
    print(s.datas)
from comparison_based_sorter import ComparisionBasedSorter

class BubbleSorter(ComparisionBasedSorter):

    def __init__(self, collection) -> None:
        super().__init__(collection)
    
    def __bubble_sort(self):
        length = len(self.datas)
        for times in range(length-1):
            swapped = False
            for idx in range(length-times-1):
                if self._isLess(idx+1,idx):
                    swapped = True
                    self._exchange(idx,idx+1)
            if not swapped:
                break

    def sort(self,flag='F'):
        if flag == 'F':
            self.__bubble_sort()
        elif flag == 'R':
            pass

if __name__ == "__main__":
    t1 = [5,2,10,-1,12,22,51,19,24,42]
    t2 = "to be or not that is a question"
    s = BubbleSorter(t1)
    s.sort()
    print(s.datas)
"""
    
"""
import numpy as np

class ComparisionBasedSorter:
    def __init__(self, collection) -> None:
        if isinstance(collection,str):
            collection = list(collection)
        self.__datas = np.array(collection)

    @property
    def datas(self):
        return self.__datas
    
    @datas.setter
    def datas(self,collection):
        raise "There should't reset the collections"

    def _isLess(self, idx_a, idx_b):
        return True if self.datas[idx_a] <= self.datas[idx_b] \
            else False
    
    def _exchange(self, idx_a, idx_b):
        self.datas[idx_a],self.datas[idx_b] = \
        self.datas[idx_b],self.datas[idx_a]
        
    def sort(flag = 'F'):
        pass


    
    def isSorted(self):
        for idx in range(1,len(self.datas)):
            if(self.__isLess(idx,idx-1)):
                return False
        return True


if __name__ == "__main__":
    s = 'abc'
    a = ComparisionBasedSorter(s)
    print(a.isSorted())

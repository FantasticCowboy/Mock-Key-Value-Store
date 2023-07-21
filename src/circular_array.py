# TODO: add in error handlign
class SortedCircularArray():
    def __init__(self):
        self.array = []
    
    def next(self, val : int):        
        return self.array[val+1] if val + 1 < len(self.array) else self.array[0]
    
    def previous(self, val : int): 
        return self.array[val-1] if val != 0 else self.array[-1]
    
    def _find(self, val : int):
        return next(index for index in range(0, len(self.array)) if self.array[index] == val)

    def get_upper_bound(self, val : int):
        if val > self.array[-1]:
            return self.array[0]
        # TODO: not efficient
        upper_bound = -1
        for elt in self.array.reverse():
            if elt > val:
                upper_bound = elt
        return upper_bound

        


    # TODO: not efficient
    def insert(self, val : int):
        self.array.append(val)
        self.array = sorted(self.array)
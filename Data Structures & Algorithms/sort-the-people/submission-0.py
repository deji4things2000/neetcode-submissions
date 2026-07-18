class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        sorth = sorted(zip(names, heights), key = lambda a: a[1], reverse = True)

        res = []
        for k, v in sorth:
            res.append(k)
        return res
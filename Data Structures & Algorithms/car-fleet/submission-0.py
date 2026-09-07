class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        pos = position
        sp = speed

        cars = list(zip(position, speed))
        cars.sort(reverse = True)
        mstack = []

        for p, s in cars:
            time = (target-p)/s

            if not mstack or time > mstack[-1]:
                mstack.append(time)
        return len(mstack)






        
class Solution:
    def cutStringBefore(self, value: str):
            newValue = []
            for i in range(0, len(value)):
                if (value[i] == '-'):
                    return newValue
                else:
                    newValue.append(value[i])
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        cutStringBefore(arriveAlice)
        aliceBefore = cutStringBefore(arriveAlice)
        print(aliceBefore)
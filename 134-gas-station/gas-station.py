class Solution(object):
    def canCompleteCircuit(self,gas,cost):
        if sum(gas) < sum(cost):            # 15 < 16  True
            return -1
        g = start = 0
        for i in range(len(gas)):
            g = g + gas[i] - cost[i]
            if g < 0:
                g = 0
                start= i+1
        return start
    
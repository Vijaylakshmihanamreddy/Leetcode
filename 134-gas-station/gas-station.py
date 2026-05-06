class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        total_tank = 0
        curr_tank = 0
        start = 0

        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]

            # If we can't reach next station
            if curr_tank < 0:
                start = i + 1
                curr_tank = 0

        # Check if solution exists
        return start if total_tank >= 0 else -1
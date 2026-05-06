class Solution(object):
    def longestArithSeqLength(self, nums):
        n = len(nums)
        dp = [{} for _ in range(n)]
        ans = 1

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]

                # if already seen, extend sequence
                dp[i][diff] = dp[j].get(diff, 1) + 1

                ans = max(ans, dp[i][diff])

        return ans
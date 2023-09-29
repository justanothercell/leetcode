class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        m = -1
        n = 10**10
        imax = max(nums)
        max_diff = imax - min(nums)
        for i in range(len(nums)-1):
            if nums[i] == imax:
                imax = max(nums[i+1:])
            if nums[i] < n:
                n = nums[i]
                s = imax - nums[i]
                if s > m:
                    m = s
                    if m == max_diff:
                        break
        return m if m != 0 else -1

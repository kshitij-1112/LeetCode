class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n - 2):
            a = nums[i]

            if a > 0:
                break

            if i and a == nums[i - 1]:
                continue

            l, r = i + 1, n - 1

            while l < r:
                total = a + nums[l] + nums[r]

                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    ans.append([a, nums[l], nums[r]])

                    left_val = nums[l]
                    right_val = nums[r]

                    while l < r and nums[l] == left_val:
                        l += 1

                    while l < r and nums[r] == right_val:
                        r -= 1

        return ans

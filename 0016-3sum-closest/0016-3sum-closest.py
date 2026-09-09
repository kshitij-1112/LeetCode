class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        best = nums[0] + nums[1] + nums[2]
        best_diff = abs(best - target)

        for i in range(n - 2):
            a = nums[i]

            # Skip duplicate a values.
            if i and a == nums[i - 1]:
                continue

            # Smallest possible sum for this i.
            s = a + nums[i + 1] + nums[i + 2]
            if s > target:
                d = s - target
                if d < best_diff:
                    return s
                break

            if s == target:
                return target

            if target - s < best_diff:
                best = s
                best_diff = target - s

            # Largest possible sum for this i.
            s = a + nums[n - 2] + nums[n - 1]
            if s < target:
                d = target - s
                if d < best_diff:
                    best = s
                    best_diff = d
                continue

            if s == target:
                return target

            left = i + 1
            right = n - 1

            while left < right:
                total = a + nums[left] + nums[right]
                d = total - target

                if d < 0:
                    d = -d

                if d < best_diff:
                    best_diff = d
                    best = total

                    if d == 0:
                        return target

                if total < target:
                    left += 1
                else:
                    right -= 1

        return best
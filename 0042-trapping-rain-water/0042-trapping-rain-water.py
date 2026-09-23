class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
            
        l, r = 0, n - 1
        l_max, r_max = height[l], height[r]
        ans = 0
        
        while l < r:
            if l_max < r_max:
                l += 1
                h = height[l]
                if h >= l_max:
                    l_max = h
                else:
                    ans += l_max - h
            else:
                r -= 1
                h = height[r]
                if h >= r_max:
                    r_max = h
                else:
                    ans += r_max - h
                    
        return ans

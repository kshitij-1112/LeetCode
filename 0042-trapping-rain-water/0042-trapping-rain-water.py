class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        if r < 2:
            return 0
            
        l_max = height[l]
        r_max = height[r]
        ans = 0
        
        while l < r:
            if l_max < r_max:
                l += 1
                h = height[l]
                if h > l_max:
                    l_max = h
                else:
                    ans += l_max - h
            else:
                r -= 1
                h = height[r]
                if h > r_max:
                    r_max = h
                else:
                    ans += r_max - h
                    
        return ans
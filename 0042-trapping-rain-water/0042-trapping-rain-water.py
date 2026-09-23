class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        l, r = 0, len(height) - 1
        l_max = height[l]
        r_max = height[r]
        water = 0
        
        while l < r:
            if l_max < r_max:
                l += 1
                lh = height[l]
                if lh >= l_max:
                    l_max = lh
                else:
                    water += l_max - lh
            else:
                r -= 1
                rh = height[r]
                if rh >= r_max:
                    r_max = rh
                else:
                    water += r_max - rh
                    
        return water
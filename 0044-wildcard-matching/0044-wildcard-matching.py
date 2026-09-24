class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)
        s_idx, p_idx = 0, 0
        star_idx = -1
        match_idx = 0
        
        while s_idx < s_len:
            # 1. Direct match or '?' wildcard
            if p_idx < p_len and (p[p_idx] == s[s_idx] or p[p_idx] == '?'):
                s_idx += 1
                p_idx += 1
            
            # 2. Encountered '*', record positions and try matching 0 characters first
            elif p_idx < p_len and p[p_idx] == '*':
                star_idx = p_idx
                match_idx = s_idx
                p_idx += 1
                
            # 3. Mismatch occurred, but we saw a '*' previously. 
            # Backtrack to the '*' and force it to swallow one more character from 's'.
            elif star_idx != -1:
                p_idx = star_idx + 1
                match_idx += 1
                s_idx = match_idx
                
            # 4. If no match and no '*' to fall back on, it's invalid
            else:
                return False
                
        # 5. Check if remaining characters in the pattern are all '*'
        while p_idx < p_len and p[p_idx] == '*':
            p_idx += 1
            
        return p_idx == p_len
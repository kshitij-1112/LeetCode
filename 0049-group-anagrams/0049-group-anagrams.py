from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Using a C-optimized defaultdict
        anagram_map = defaultdict(list)
        
        for s in strs:
            # ''.join(sorted(s)) leverages C-level Timsort, which is extremely 
            # fast for short strings (length <= 100) and avoids Python loop overhead.
            anagram_map[''.join(sorted(s))].append(s)
            
        return list(anagram_map.values())
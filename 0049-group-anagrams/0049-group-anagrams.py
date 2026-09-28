from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Map character frequency tuple -> list of anagrams
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Count frequencies of characters 'a' through 'z'
            count = [0] * 26
            for char in s:
                count[ord(char) - 98 + 1] += 1 # standard optimization or ord(char) - ord('a')
            
            # Use tuple(count) as the key because lists are mutable and unhashable
            anagram_map[tuple(count)].append(s)
            
        return list(anagram_map.values())
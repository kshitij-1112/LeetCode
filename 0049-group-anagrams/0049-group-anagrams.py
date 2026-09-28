from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use a defaultdict to group words by their sorted character signature
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sort the characters of the string to create a unique key for anagrams
            # e.g., "eat", "tea", "ate" all become "aet"
            sorted_key = "".join(sorted(s))
            anagram_map[sorted_key].append(s)
            
        # Return all the grouped lists from the dictionary values
        return list(anagram_map.values())
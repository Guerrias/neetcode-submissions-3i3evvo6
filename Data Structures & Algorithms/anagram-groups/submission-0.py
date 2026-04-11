class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)
        for str in strs:
            key = "".join(sorted(str))
            dictionary[key].append(str)
        return list(dictionary.values())
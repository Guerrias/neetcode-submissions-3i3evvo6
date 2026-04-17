class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {"[":"]", "{":"}", "(":")"}

        for char in s :
            if char in dictionary :
                stack.append(dictionary[char])
            elif not stack or stack.pop() != char : 
                return False
        
        return len(stack) == 0
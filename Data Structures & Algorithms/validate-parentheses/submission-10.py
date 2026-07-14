class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')':'(', '}':'{',']':'['}

        brackets = list(s)

        stack = []
        k = 0

        while k<len(brackets):
            if brackets[k] in pairs.values():
                stack.append(brackets[k])
            else:
                if not stack:
                    return False
                latest = stack.pop(-1)
                if latest != pairs[brackets[k]]:
                    return False
            k = k+1
        
        if stack:
            return False
        else:
            return True
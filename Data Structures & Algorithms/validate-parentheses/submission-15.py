class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')':'(', '}':'{',']':'['}
        opening = {'(','{','['}
        stack = []

        # brackets = list(s)

        # stack = []
        # k = 0

        # while k<len(brackets):
        #     if brackets[k] in pairs.values():
        #         stack.append(brackets[k])
        #     else:
        #         if not stack:
        #             return False
        #         latest = stack.pop(-1)
        #         if latest != pairs[brackets[k]]:
        #             return False
        #     k = k+1

        for bracket in s:
            if bracket in opening:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                if stack.pop() != pairs[bracket]:
                    return False
        
        return len(stack) == 0
        
        # if stack:
        #     return False
        # else:
        #     return True
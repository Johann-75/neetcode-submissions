class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [0 for _ in range(n+1)]
        left, right = n-1, n
        steps[left], steps[right] = 1, 1
        while left >= 0:
            steps[left-1] = steps[left] + steps[right]
            left = left-1
            right = right-1

        return steps[0]

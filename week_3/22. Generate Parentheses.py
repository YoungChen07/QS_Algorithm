# Created by Young Chen at 8/26/2018
# https://leetcode.com/problems/generate-parentheses/solution/
class Solution(object):
    def generateParenthesis(self, N):
        if N == 0: return ['']
        ans = []
        for c in xrange(N):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans

    class Solution(object):
        def generateParenthesis(self, N):
            ans = []

            def backtrack(S='', left=0, right=0):
                if len(S) == 2 * N:
                    ans.append(S)
                    return
                if left < N:
                    backtrack(S + '(', left + 1, right)
                if right < left:
                    backtrack(S + ')', left, right + 1)

            backtrack()
            return ans
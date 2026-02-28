"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

Key Intuition:
    A stack naturally mirrors the nesting structure of brackets.
    Push every opening bracket; on a closing bracket, check that
    the top of the stack is its matching opener.

Complexity (Optimal):
    Time:  O(n)
    Space: O(n)
"""


# ──────────────────────────────────────────────
# Optimal: Stack
# ──────────────────────────────────────────────
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in close_to_open:
                if stack and stack[-1] == close_to_open[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        return not stack


# ──────────────────────────────────────────────
# Alternative: Replace pairs iteratively (fun but slow)
# Time O(n²) · Space O(n)
# ──────────────────────────────────────────────
class SolutionReplace:
    def isValid(self, s: str) -> bool:
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()', '').replace('[]', '').replace('{}', '')
        return s == ''

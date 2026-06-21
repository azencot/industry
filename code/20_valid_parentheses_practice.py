# Given a string s containing just the characters '(', ')', '{', '}', 
# '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
from collections import deque

class Solution(object):
    def isValid(self, s):
    	# this is natural for a deque, because we always need last paren
		stack = deque()

		# rule-of-thumb: if OP, append to q; o.w., pop
		for c in s:
			if c == '(' or c == '{' or c == '[':
				stack.append(c)
			else:
				if not stack:
					return False

				c2 = stack.pop()
				if (c2 == '(' and c != ')') or (c2 == '{' and c != '}') or \
				(c2 == '[' and c != ']'):
					return False

		return len(stack) == 0
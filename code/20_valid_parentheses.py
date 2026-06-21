# Given a string s consisting only of the characters (,),{,},[,], determine whether the input string is valid.
# An input string is considered valid if all of the following conditions hold:
# Every opening bracket is closed by the same type of bracket.
# Brackets are closed in the correct order.
# Every closing bracket has a corresponding opening bracket of the same type.

# a simple solution with a queue: push opening, pop closing and match to opening

def validParentheses(s):
	# s contains only (,),{,},[,]
	queue = []
	for char in s:
		if char == '(' or char == '[' or char == '{':
			queue.append(char)
			continue

		# edge case: closing but no opening
		elif len(queue) == 0:
			return False

		elif char == ')':
			if queue[-1] != '(':
				return False

		elif char == ']':
			if queue[-1] != '[':
				return False

		elif char == '}':
			if queue[-1] != '{':
				return False

		queue.pop()

	if len(queue) > 0:
		return False
	else:
		return True

print(validParentheses("()"))
print(validParentheses("()[]{}"))
print(validParentheses("(]"))
print(validParentheses("([])"))
print(validParentheses("([)]"))

			
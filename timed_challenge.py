"""
Timed Challenge: Balanced Symbols

Check if the brackets in a string are balanced.

Example:
Input: "{[()]}"
Output: True

Input: "{[(])}"
Output: False
"""


def is_balanced(text):
    stack = []

    opening = "([{"
    closing = ")]}"
    matching = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for character in text:
        if character in opening:
            stack.append(character)

        elif character in closing:
            if len(stack) == 0:
                return False

            if stack.pop() != matching[character]:
                return False

    return len(stack) == 0


# A stack is the best choice because brackets must be matched in
# last-in, first-out order. Adding and removing from the stack are
# O(1) operations, so checking the entire string takes O(n) time.


# TESTS

print("Balanced Symbols Tests:")

print(is_balanced("{[()]}"))
print(is_balanced("{[(])}"))
print(is_balanced("()"))
print(is_balanced(""))
print(is_balanced("((("))
print(is_balanced("abc"))
print(is_balanced("([{}])"))
print(is_balanced("([)]"))


"""
Reflection:

For this challenge, I chose a stack because brackets need to be matched
in a last-in, first-out order. When an opening bracket is found, I add it
to the stack. When a closing bracket is found, I compare it to the most
recent opening bracket. If they match, I remove the opening bracket from
the stack. If they do not match, the string is not balanced.

The 30-minute time limit affected my decision because I wanted to use a
data structure that I already understood instead of trying to create
something more complicated. I focused first on getting the main solution
working, and then I added tests for different situations. This helped me
avoid spending too much time on unnecessary features.

One trade-off I made was keeping the solution simple instead of trying to
handle every possible type of input. The function expects a string, which
is what the problem describes. I also used a dictionary to match closing
brackets with their opening brackets because it made the comparisons
easier to read. The main advantage of this approach is that the solution
only needs to go through the string once. Overall, the stack made the
problem easier to organize and gave me an efficient solution that takes
O(n) time.
"""# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!
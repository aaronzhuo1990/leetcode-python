"""
Problem:
    Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

    Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

    Input: "A man, a plan, a canal: Panama"
    Output: true

Example 2:
    Input: "race a car"
    Output: false

Solution:
    see code
"""


class Solution(object):
    def detect_palindrome(self, text):
        if len(text) == 0:
            return True
        filter_str = ''.join(x for x in text.lower() if x.isalpha())  # lowercase text and only keep letters

        start, end = 0, len(filter_str)-1
        while start < end:
            if filter_str[start] != filter_str[end]:
                return False
            start += 1
            end -= 1

        return True


t = u"A man, a plan, a canal: Panama"
s = Solution()
print s.detect_palindrome(t)

t = u"race a car"
print s.detect_palindrome(t)
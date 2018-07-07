# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
# The digits are stored such that the most significant digit is at the head of the list, and each element
# in the array contain a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Examples:
#   Input: [1,2,3]
#   Output: [1,2,4]

#   Input: [4,3,9,9]
#   Output: [4,4,0,0]

# Solution, reverse the list and do the calculation from left to right, and then reverse the list


class Solution(object):
    def plus_one(self, digits):
        """
        :param digits: list[int]
        :return: list[int]
        """
        digits.reverse()
        carry = 0

        for i, d in enumerate(digits[0:], 0):
            digits[i] = (d + 1) % 10
            carry = (d + 1) / 10
            if carry == 0:
                break

        if carry == 1:
            digits.append(1)
        digits.reverse()
        return digits


solution = Solution()
a = [1,2,4]
print(solution.plus_one(a))

a = [1,2,9]
print(solution.plus_one(a))

a = [1,9,9]
print(solution.plus_one(a))

a = [9,9,9]
print(solution.plus_one(a))
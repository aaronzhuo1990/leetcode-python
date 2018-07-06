# Given a sorted array and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order. You may assume no duplicates in the array.
# Here are few examples.
# [1,3,5,6], 5 -> 2
# [1,3,5,6], 2 -> 1
# [1,3,5,6], 7 -> 4
# [1,3,5,6], 0 -> 0


class Solution(object):
    def search_insert_position(self, array, target):
        """
        :param array: list[int]
        :param target: int
        :return: expected position
        """
        num = len(array)
        left = 0
        right = num - 1

        while left <= right:
            mid = (left + right) / 2
            if array[mid] == target:
                return mid
            elif (mid < num-1) and (array[mid] < target <= array[mid+1]):  # edge case: mid points to the last element
                return mid+1
            elif target < array[mid]:
                right = mid - 1
            else:
                left = mid + 1
        if left == num:
            return num
        if right < 0:
            return 0


a = [1, 3, 5, 6]
s = Solution()
print(s.search_insert_position(a, 5))
print(s.search_insert_position(a, 2))
print(s.search_insert_position(a, 7))
print(s.search_insert_position(a, 0))
print(s.search_insert_position(a, 6))



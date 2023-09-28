#!/usr/bin/python3
"""script for finding peak in list of ints, interview prep
"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): a list of integers
    Returns:
    int: peak(s)
    """
    nums = list_of_integers
    if nums == []:
        return None
    length = len(nums)

    start, end = 0, length - 1
    while start < end:
        mid = start + (end - start) // 2
        if nums[mid] > nums [mid - 1] and nums[mid] > nums[mid + 1]:
            return nums[mid]
        if nums[mid - 1] > nums[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return nums[start]

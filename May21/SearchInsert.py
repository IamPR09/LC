"""

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4



"""


# Approach 1

"""
 - loop through each element in the list, keeping track of the index
 - compare :
   - if element = target --> return the index
   - if element > target --> return index-1
   - if element < target --> keep until last element --> index+1


"""


def searchInsert(nums,target):
    for ix,element in enumerate(nums):
        if element==target:
            return ix
        elif element > target:
            return ix
    return ix+1


# T(n) - O(n)
# S(n) - O(1)


# Approach 2

"""
 - l,h --> first element and last element respectively
 - Middle is calculated - which is the mid element of  the list
- compare the target with the mid element
   - if mid = target --> return the index of the mid
   - if mid < target --> return the index of the mid
    - else return mid +1 ix

"""

def searchInsertOpt(nums, target):
    l,h = 0,len(nums)-1
    while l<=h:
        mid = (l+h)//2
        if nums[mid]==target:
            return mid
        if target > nums[mid]:
            l=mid+1
        else:
            h = mid-1
    if nums[mid]>target:
        return mid
    else:
        return mid+1
    

# T(n) - O(logn)
# S(n) - O(1)

# --------------------------------

# Think of what you return ? --> You sure about mid ?

# ----------------------------------
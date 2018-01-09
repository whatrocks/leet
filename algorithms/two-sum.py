def twoSum(nums, target):
    dict = {}
    for i, n in enumerate(nums):
        if n in dict:
            return [dict[n], i]
        else:
            dict[target - n] = i

print("Testing....")
nums1 = [2, 7, 11, 15]
target1 = 9
expected1 = [0,1]
actual1 = twoSum(nums1, target1)
assert expected1 == actual1


nums2 = [3,2,4]
target2 = 6
expected2 = [1,2]
actual2 = twoSum(nums2, target2)
assert expected2 == actual2

print("Testing complete!!")


# easier O(n^2).
# first one to left, then one by one.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, e in enumerate(nums[:-1]):
            for n in range(i+1,len(nums)):
                if nums[i] + nums[n] == target:
                    return [i,n]

        pass
    
    
# faster O(n)
# relation : a = t - b, a as com in dict with idx, 
# if next com found in dict 
# -> a(new) = t - b (com in dict) 
# -> a + b = t 
# -> return [a_idx, b_idx]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i, n in enumerate(nums):
            com = target - n
            if com in diff:
                return [diff[com], i]
            diff[n] = i
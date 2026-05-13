#Brute force - for each element of the array, traverse through the remaining whole array to look for duplicate.
'''
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return True
        return False
'''    
#Better Solution using Sort -> then comparing if nums[i] and nums[i+1] are equal or not.
'''
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
        return False    
'''
#Pythonic Solution - Type casting arr-> set and comparing both the lengths --> Unequal -> Duplicates Present as Set doesn't contain duplicate values.
'''
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums)!=len(set(nums))
'''

#Optimal Solution - Hash Set

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i)
        return False
        

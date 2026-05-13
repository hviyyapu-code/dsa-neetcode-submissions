class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #does neighbourhood comparison.
        temp=0
        for i in range(len(nums)-1):
            curr=nums[i]
            temp=curr
            for j in range(i+1,len(nums)):
                if temp==nums[j]:
                    return True
                else:
                    curr=nums[j]
                    
        return False

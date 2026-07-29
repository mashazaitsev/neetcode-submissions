class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        d={}
        #dictionary will overrite the key if same num appears!
        #use the index in the key instead!

        if len(nums)<=2:
            return sorted(nums)
        for i in range(len(nums)):
            newList=nums[:i]+nums[i+1:]
            d[i]=newList
        res=[]
        for key in d:
            valueList=d[key]
            multiple=1
            for n in valueList:
                multiple*=n
            res.append(multiple)
        return res

        
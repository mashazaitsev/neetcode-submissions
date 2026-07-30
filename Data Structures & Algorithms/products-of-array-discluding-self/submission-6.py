class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix,postfix=[1],[1]
        for i in range(len(nums)-1): #3
            prefix.append(nums[i]*prefix[i])
        for i in range(len(nums)-1,0,-1):
            postfix.append(nums[i]*postfix[abs(i-(len(nums)-1))])
        final=[]
        postfix=postfix[::-1]
        for i in range(len(nums)):
            final.append(prefix[i]*postfix[i])
        return final



        #switch order of postfix

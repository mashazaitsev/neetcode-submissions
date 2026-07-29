class Solution:
    #use .get to get the value of key without crashing if it doesn't exist.
    #FASTER TIME COMPLEXITY INSTEAD OF CALLING .count on list-> use .get on the dict
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        brackets=[[] for i in range (len(nums)+1)]
        mapping={}

        for num in nums:
            mapping[num]=1+mapping.get(num,0)
        for key in mapping:
            timesAppeared=mapping[key]
            brackets[timesAppeared].append(key)
        
        result=[]
        for j in range (len(brackets)-1,0,-1): #don't index out of range.
            #then loop thru every single number in 2nd set of ()
            for n in brackets[j]:
                result.append(n)
                if len(result)==k:
                    return result





        
    
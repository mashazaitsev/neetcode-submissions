class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #duplicate wipes out progress, so use a set.
        nums=set(nums)
        if len(nums)==0:
            return 0
        initializers=[]
        #build up list of initializers
        for num in nums:
            if (num-1) not in nums:
                initializers.append(num)
        
        lengths=set()
        for i in range (len(initializers)):
            seq=[initializers[i]]
            for i in range (len(nums)):
                if seq[-1]+1 in nums:
                    seq.append(seq[-1]+1)
            lengths.add(len(seq))
        return max(lengths)


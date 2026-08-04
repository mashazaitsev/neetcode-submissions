class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        vals={}
        for i in range(len(numbers)):
            vals[i+1]=numbers[i]
        for key in vals:
            for SecKey in vals:
                if vals[key]+vals[SecKey]==target and key!=SecKey:
                    res=[key,SecKey]
                    return sorted(res)
        
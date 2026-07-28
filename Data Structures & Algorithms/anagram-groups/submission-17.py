class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #turn list into string by using join
        strdict={}
        for word in strs:
            sortedList=sorted(list(word))
            sortedWord="".join(sortedList)
            if sortedWord not in strdict:
                strdict[sortedWord]=[word]
            else:
                strdict[sortedWord].append(word)
        res=[]
        for key in strdict:
            listStrings=strdict[key]
            res.append(listStrings)
        return res



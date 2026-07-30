class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        delim='#'
        for word in strs:
            length=f'{len(word)}'
            res+=length+delim+word
        return res
#two things to change:
#integer can be longer than 1 AND length of string changes.
    def decode(self, s: str) -> List[str]:
        encodedstring=s #check if correct
        decoded=[]
        while len(encodedstring)>0:
            iofhash=encodedstring.find('#')
            substring=encodedstring[0:iofhash+1]
            if substring[0:iofhash].isdigit() and ord(substring[iofhash])==35:
                integer=int(substring[0:iofhash])
                currword=encodedstring[iofhash+1:iofhash+integer+1] #the word that follows the delim
                decoded.append(currword)
                encodedstring=encodedstring[iofhash+integer+1:] #this is where i chop off the num+deliminator 
        return decoded



        
            


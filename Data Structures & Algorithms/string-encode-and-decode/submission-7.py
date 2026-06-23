class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for string in strs:
            length=len(string)
            encoded=str(length)+"#"+string
            result=result+encoded
        return result


    def decode(self, s: str) -> List[str]:

        result=[]

        i=0
        j=0

        while i<len(s):
        
            while s[j].isdigit():
                j+=1
            
            length=int(s[i:j])
            i=j
            start=i+1
            end=start+length
           
            string=s[start:end]
           
            
            i=end
            j=i
            result.append(string)
           
           
        
        return result


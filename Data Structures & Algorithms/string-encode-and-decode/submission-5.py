class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for string in strs:
            length=len(string)
            encoded=str(length)+"#"+string
            result=result+encoded
        print(result)
        return result


    def decode(self, s: str) -> List[str]:

        result=[]

        i=0
        j=0

        while len(s)>0:
            while s[i].isdigit():
                i+=1
            
            length=s[:i]#10
            delimiter=s[i:i+1]##
            j=i+1+int(length)

            result.append(s[i+1:j])
            s=s[j:]
        
        return result


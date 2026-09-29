class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res=[]
        result=[]
        word=""


        def backtrack():
            word=''
            
            for string in res:
                word+=string
            if len(word)>len(s):
                return

            if word==s:
                return True
            
            for choice in wordDict:
                res.append(choice)
                if backtrack():
                    return True
                res.pop()
            return False
        return backtrack()
        
        


        
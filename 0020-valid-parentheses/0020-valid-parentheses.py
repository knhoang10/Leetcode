class Solution:
    def isValid(self, s: str) -> bool:
        # Left bracket needs to be closed by the right
        # Keep track of the left bracket
        # Once the right bracket is selected, check the most recent bracket
        brackets = {
            '{': '}',
            '[': ']',
            '(': ')'
        }
        allLeftBracketInS = []
        for i in range(len(s)):
            if s[i] in brackets: # left bracket
                allLeftBracketInS.append(s[i])
            else: # right bracket
                if len(allLeftBracketInS) == 0: # if there is no left bracket then it fails
                    return False
                else:
                    if s[i] == brackets[allLeftBracketInS[-1]]:
                        allLeftBracketInS.pop(-1)
                    else:
                        return False
        if len(allLeftBracketInS) == 0:
            return True
        else:
            return False
                
        
        
        
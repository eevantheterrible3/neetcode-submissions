class Solution:
    def isValid(self, s: str) -> bool:
        closed_to_open = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []

        for c in s:
            if c in closed_to_open:
                if not stack:
                    return False
                
                tmp = stack.pop()
                if closed_to_open[c] != tmp:
                    return False
                
            else:
                stack.append(c)
        
        if stack:
            return False
        else:
            return True

        
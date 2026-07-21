class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for c in s:
            if c == "{" or c == "[" or c == "(":
                stack.append(c)
            elif len(stack) == 0:
                return False
            else:
                a = stack.pop()
                print(f"c = {c}, a = {a}")
                if a == "[" and c != "]":
                    return False
                if a == "{" and c != "}":
                    return False
                if a == "(" and c != ")":
                    return False
        

        return len(stack) == 0
        
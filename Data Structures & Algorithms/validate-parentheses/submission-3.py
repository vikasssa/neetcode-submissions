class Solution:
    def isValid(self, s: str) -> bool:
        record = []

        if len(s) == 1:
            return False

        for ch in s:
            if ch in "({[":
                record.append(ch)
            elif ch == "}":
                if record and record[-1] == "{":
                    record.pop()
                else:
                    return False
            elif ch == "]":
                if record and record[-1] == "[":
                    record.pop()
                else:
                    return False
            elif ch == ")":
                if record and record[-1] == "(":
                    record.pop()
                else:
                    return False
        
        return len(record) == 0
        
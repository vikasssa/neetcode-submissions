class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for item in operations:
            if item == 'C':
                record.pop()
            elif item == 'D':
                x = record[-1]
                record.append(2*int(x))
            elif item == '+':
                x = record[-1]
                y = record[-2]
                record.append(int(x) + int(y))
            else:
                record.append(int(item))
        
        return sum(record)
        
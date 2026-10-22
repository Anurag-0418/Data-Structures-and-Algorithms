class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        count = 0
        str = ""
        while(columnNumber > 26 or count == 0):
            count += 1
            columnNumber -= 1
            q = columnNumber // 26
            r = columnNumber % 26
            str = str + (chr(r+65))
            columnNumber = q
        if q != 0:
            str = str + (chr(q+64))
        return str[::-1]
        
        
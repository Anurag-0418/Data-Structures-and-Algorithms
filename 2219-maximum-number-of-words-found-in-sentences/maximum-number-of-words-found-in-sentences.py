class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        max = 0
        for i in sentences:
            number = i.count(" ")
            if number > max:
                max = number
        return max + 1
        
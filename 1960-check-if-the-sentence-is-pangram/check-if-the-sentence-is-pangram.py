class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = list(string.ascii_lowercase)
        for letter in alphabets:
            if letter not in sentence:
                return False
        return True
        
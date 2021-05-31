class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^A-Za-z0-9]+', '', s).lower()
        print (s)
        if len(s) % 2 == 0:
            iterations = int(len(s) / 2)
            for i in range (0,iterations):
                leftChar = s[iterations -1 - i]
                rightChar = s[iterations + i]
                print("left: ", leftChar, " right: ", rightChar)
                if leftChar != rightChar:
                    return False

        if len(s) % 2 == 1:
            iterations = int((len(s) - 1) / 2)
            print(s[iterations])
            for i in range (0,iterations):
                print("hi")
                leftChar = s[iterations - i]
                rightChar = s[iterations + i]
                print("left: ", leftChar, " right: ", rightChar)
                if leftChar != rightChar:
                    return False
# wip

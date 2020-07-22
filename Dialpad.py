class Solution:
    def Find_comb(self, digits):
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}               
        def backtrack(res, next):
            if len(next) == 0:
                output.append(res)
            else:
                for letter in phone[next[0]]:
                    backtrack(res + letter, next[1:])                  
        output = []
        if digits:
            backtrack("", digits)
        return output

val=Solution()
digits=input()
print(*val.Find_comb(digits))

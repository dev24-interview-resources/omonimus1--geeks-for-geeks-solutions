# https://www.geeksforgeeks.org/problems/find-maximum-number2152/0
class Solution:
    def findMax(self, N):
        numbers = list(N)
        numbers.sort()
        numbers.reverse()
        result = ""
        for digit in numbers:
            result += digit
        return result
        

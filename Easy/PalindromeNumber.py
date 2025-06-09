#My Solution
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        newNumber = []
        number = list(map(int, str(x)))
        print(number)
        i = len(number)
        print(i)
        for j in range(i):
            newNumber.append(number[i-1])
            i-=1
            j += 1
        print(newNumber)

        result = newNumber == number
        return result
test = Solution()
test.isPalindrome(-121)

#More Efficient (No need to convert to str)
# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         if x < 0:
#             return False
            
#         original = x
#         reversed_num = 0
        
#         while x > 0:
#             reversed_num = reversed_num * 10 + x % 10
#             x //= 10
            
#         return original == reversed_num
    
# test = Solution()
# test.isPalindrome(121)
#My Solution
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ROMAN_DICT = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        result = []
        listInt = []
        listRom = list(s)

        #print (listRom)
        for i, value in enumerate(listRom):
            number = ROMAN_DICT[value]
            listInt.insert(i, number)
        
        j = 0
        while j < len(listInt):
            if j+1 < len(listInt) and listInt[j] < listInt[j+1]:
                result.append(listInt[j+1] - listInt[j])
                j+=2
            else:
                result.append(listInt[j])
                j+=1

        #print(listInt)
        #print(result)
        return sum(result)

test = Solution()
test.romanToInt('MCMXCIV')

#More Efficient
# class Solution(object):
#     def romanToInt(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         ROMAN_DICT = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000
#         }
        
#         total = 0
#         prev_value = 0
        
#         # Iterate through string in reverse
#         for char in s[::-1]:
#             curr_value = ROMAN_DICT[char]
#             if curr_value >= prev_value:
#                 total += curr_value
#             else:
#                 total -= curr_value
#             prev_value = curr_value
            
#         return total

# # Test cases
# test = Solution()
# print(test.romanToInt('MCMXCIV'))  # 1994
# print(test.romanToInt('III'))      # 3
# print(test.romanToInt('IX'))       # 9
class Solution(object):
    def romanToInt(self, s):
        list1 = []
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

        for x in s:
            for keys,values in roman.items():
                if x in keys:
                    list1.append(values)


        return sum(list1)

s = "IVI"
obj=Solution()
result=obj.romanToInt(s)
print(result)


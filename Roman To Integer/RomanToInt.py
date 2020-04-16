"""
Busra Yasar
Roman numerals are represented by seven different sysmbols:
1. I->1 2.V->5 3.X->10  4.L->50 5.C->100 6.D->500 7.M->1000
For example, 2 is written as II in Roman numeral, just two one's added together.
12 is written as, XII which is simply X+II. The number 27 is written as XXVII
which is XX+V+II.
Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number 4 is written as
IV. Because the one is before the five we subtract it making four. The same
principle applies to the number ninei which is written as IX. There are six
instance where subtraction is used:
I-> can be placed before V and X to make 4 and 9.
X-> can be placed before L(50) and C(100) to make += and 90.
C-> can be placed before D(500) and M(1000) to make 400 and 900
Given a roman numeral, convert it to an integer. Input is guaranteed to be within
the range from 1 to 3999.
Ex 1: Input: III Output:3
Ex 2: Input: IV Output:4
Ex 3: Input: IX Output:9
Ex 4: Input: LVIII Output:58 Explanation: L:50 V:5 III:3
Ex 5: Input: MCMXCIV Output:1994 Explanation: M:1000 CM:900 XC:90 IV:4
"""
class RomanToInt(object):
    def romanToInt(self, s):
        """
        type s:str
        rtype: int
        """
        #define romans in dictionary
        doubles = {'CM':900, 'CD':400, 'XC':90, 'XL':40, 'IX':9, 'IV':4}
        singles = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5,'I':1}
        integer = 0;
        i = 0;
        while i<len(s):
            if i<len(s)-1 and s[i:i+2] in doubles:
                integer += doubles[s[i:i+2]]
                i+=2
            else:
                integer += singles[s[i]]
                i += 1
        return integer
def main():
    roman = str(input("Enter a roman numeral:"))
    print(RomanToInt().romanToInt(roman))
if __name__ == "__main__":
    main()
"""
Sample inputs: MMMCMLXXXVI, MMM, C

"""

from lib2to3.pygram import Symbols



def intToRoman(num):
    symbols = [
            ("I",1),
            ("IV",4),
            ("V",5),
            ("IX",9),
            ("X",10),
            ("XL",40),
            ("L",50),
            ("XC",90),
            ("C",100),
            ("CD",400),
            ("D",500),
            ("CM",900),
            ("M",1000)
            ]

    roman_str = ""
    for (symbol,value) in symbols[::-1]:
        print(symbol)
        quotient = int(num / value)
        if quotient:
            num -= quotient * value
            roman_str += symbol * quotient

    return roman_str


class Solution(object):
    def isPalindrome(self, x):
        stringify = str(x)
        j = len(stringify)-1
        i = 0
        
        while(i < len(stringify)):
            if(stringify[i] == stringify[j]):
                i += 1
                j -= 1
                
            else:
                return False
        return True
num = 10
value = intToRoman(num)
print(value)
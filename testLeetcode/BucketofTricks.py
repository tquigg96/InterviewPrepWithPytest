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





def breakingRecords(scores):
    answ = [0,0]
    conNumDrum = scores[0]

    for i in range(1, len(scores)):
        if (scores[i] > conNumDrum):
            answ[0] += 1
        if (scores[i] < conNumDrum):
            answ[1] += 1
    print(answ)


import sys

def splitOut(s):
    string = ''
    outString = ''
    if s[0] == 'M':
        string = s[1][:-2]
    else:
        string = s[1]
    
    for j,i in enumerate(string):
        if i.isupper():
            if j==0:
                outString += i.lower()
                continue
            outString += ' ' + i.lower()
        else:
            outString += i
    print(outString)
    
def combine(s):
    string = s[1]
    outString = ''
        
    string = [x.capitalize() for x in string.split(' ')]
    
    if s[0] != 'C':
        string[0] = string[0].lower()
    
    for x in string:
        outString += x
    
    if s[0] == 'M':
        outString += '()'
    print(outString)


inputData = [line.rstrip('\n\r') for line in sys.stdin.readlines()] #getting rid of spaces

for s in inputData:
    s = s.split(';')
    if s[0] == 'S':
        splitOut(s[1:])
    else:
        combine(s[1:])
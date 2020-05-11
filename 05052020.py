'''
May 10 2020
author: Qiangwen Xu
'''


# 151. Reverse Words in a String

belowTwenty = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty"]
belowHundred = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]


def convert(num: int):
    if (num < 20):
        result = belowTwenty[num];
    elif (num < 100):
        if num%10 == 0:
            result = belowHundred[num//10]
        else:
            result = belowHundred[num//10] + " " + convert(num%10)
    elif (num < 1000):
        if num%100 == 0:
            result = convert(num//100) + " Hundred"
        else:
            result = convert(num//100) + " Hundred" + " " + convert(num%100)
    elif (num < 1000000):
        if num%1000 == 0:
            result = convert(num//1000) + " Thousand"
        else:
            result = convert(num//1000) + " Thousand" + " " + convert(num%1000)
    elif (num < 1000000000):
        if num%1000000 == 0:
            result = convert(num//1000000) + " Million"
        else:
            result = convert(num//1000000) + " Million" + " " + convert(num%1000000)
    elif (num >= 1000000000):
        if num%1000000000 == 0:
            result = convert(num//1000000000) + " Billion"
        else:
            result = convert(num//1000000000) + " Billion" + " " + convert(num%1000000000)
    return result

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        else:
            return convert(num).strip()
    
    
    
# 

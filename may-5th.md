# May 5th

## 151. Reverse Words in a String

```python
# python solution 1

belowTwenty = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty"]
belowHundred = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

def convert(num: int):
    if (num < 20):
        result = belowTwenty[num];
    elif (num < 100):
        result = belowHundred[num//10] 
        result = result if (num%10 == 0) else (result + " " + convert(num%10))
    elif (num < 1000):
        result = convert(num//100) + " Hundred"
        result = result if (num%100 == 0) else (result + " " + convert(num%100))
    elif (num < 1000000):
        result = convert(num//1000) + " Thousand"
        result = result if (num%1000 == 0) else (result + " " + convert(num%1000))
    elif (num < 1000000000):
        result = convert(num//1000000) + " Million"
        result = result if num%1000000 == 0 else result + " " + convert(num%1000000)
    elif (num >= 1000000000):
        result = convert(num//1000000000) + " Billion"
        result = result if num%1000000000 == 0 else result + " " + convert(num%1000000000)
    return result

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        else:
            return convert(num).strip()
```




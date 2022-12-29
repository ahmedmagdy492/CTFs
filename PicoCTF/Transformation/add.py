#!/usr/bin/python3

nums = [
    28777,
    25455,
    17236,
    18043,
    12598,
    24418,
    26996,
    29535,
    26990,
    29556,
    13108,
    25695,
    28518,
    24376,
    24421,
    14128,
    13154,
    13368,
    13949,
]

def decimalToBin(val): 
    return bin(val).replace("0b", "")

def binaryToDecimal(n):
    return int(n,2)

result = ""

for n in range(0, len(nums)):
    binary_num = decimalToBin(nums[n])
    size = len(binary_num)
    first_values = binaryToDecimal(binary_num[size-7:])
    char = chr(first_values)
    result += char

str1 = 'pcCF1_isis3do__7346'
str2 = 'ioT{6bt_nt4_f8e0b8}'

result = ""
for i in range(0, len(str1)):
    result += str1[i] + str2[i]

print(result)
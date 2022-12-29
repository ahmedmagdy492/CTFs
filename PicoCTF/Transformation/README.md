''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])


so it was all about getting to know what the code above does and when you understand it you will find yourself stuck cause you will simply figure out that the opposite operation to the code above is just to shift the number by 8 to the right to get to the original number but you miss the next number
but after research you will find out that the bigger number which is the result actually contains the number that you are looking for in its binary representation exectally at the 7 lower bits and walla you got the next char that is missing. at the end combine both of them together and you got the flag 
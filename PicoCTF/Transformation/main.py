#!/usr/bin/python3

flag = ""

with open("enc") as enc:
    flag = ''.join(enc.readlines())

result = ""
for i in range(0, len(flag)):
    result += chr(ord(flag[i]) >> 8)

print(result)















#flag = "\xe7\x81\xa9\xe6\x8d\xaf\xe4\x8d\x94\xe4\x99\xbb\xe3\x84\xb6\xe5\xbd\xa2\xe6\xa5\xb4\xe7\x8d\x9f \xe6\xa5\xae\xe7\x8d\xb4\xe3\x8c\xb4\xe6\x91\x9f\xe6\xbd\xa6\xe5\xbc\xb8\xe5\xbd\xa5\xe3\x9c \xb0\xe3\x8d\xa2\xe3\x90\xb8\xe3\x99\xbd"
    
# the flag length should be 38
# pcCF{1_isis3do__7346}
# ioT{6bt_nt4_f8e0b8}

# name = "my name is ahmed" # 16 chars

# result = ''.join([chr((ord(name[i]) << 8) + ord(name[i + 1])) for i in range(0, len(name), 2)])
# print(len(result))

# for i in range(0, len(result)-1):
#     print(chr(ord(result[i]) >> 8))
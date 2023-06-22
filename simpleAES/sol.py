from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from pwn import unhex 


iv = unhex("813c5def8998acecf96ae0fd8c0af844")
ct = unhex("8ceeab5f2db4424386053833f2bd9144f6d52e23f1c2cb30ca4e6895b9a7f9e5")
for _1 in range(255) :
    for _2 in range(255) :
        key = pad(_1.to_bytes()+_2.to_bytes(), 16)

        cipher = AES.new(key, AES.MODE_CBC, iv)
        flag = cipher.decrypt(pad(ct, 16))
        if(b"ISI" in flag) : print(flag)
# iv = 813c5def8998acecf96ae0fd8c0af844
# 

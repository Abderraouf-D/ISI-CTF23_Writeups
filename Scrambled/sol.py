

x = open("X","rb").read() # contains PNG magic bytes
y = open("Y","rb").read() # IDAT chunx
c = open("C","rb").read() # IDAT chunk
n = open("N","rb").read() #IHDR
_0 = open("0","rb").read()  #IEND
_3 = open("3","rb").read() #IDAT




header = x+n
cpt=0
l=[c,y,_3]
for i in  l  :    
    for j in list(set(l)-set(i))  : 
        for k in list(set(l)-set([i]+[j]))  : 
            open(f"flag{cpt}.png",'wb').write(header+i+j+k+_0)
            cpt+=1




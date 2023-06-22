
from pwn import unhex


#extract data fields from tcp paquets using  :  tshark -r test.pcapng -Y tcp -T fields -e data >output
#decode the output in CyberChef  using FROM Hex (didn't take the effort to script it xd)
#download the file as "unhexed"


#this script cleans up the  file and extract the RGB tuples to create flag.png using PIL library

colors={
    34:2 , 
    32:1,
    31:0
}
#ansi escape code https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
#34 -> blue
#32 -> green
#31 -> red

cap =open("unhexed","rb").read().replace(b'chawala hada sa7bi',b'').split(b'\\033[0m')
res=[]*(len(cap)-1)
tup=[0,0,0]
for i,c in enumerate(cap) : 
    try : 
        tmp = c.replace(b'\\033[0;',b'').split(b'm') 
        tup[colors[int(tmp[0])]]=int(tmp[1])
        if(i%3  == 2 ) : 
            res.append(tuple(tup))
     
    except : pass

#create the image 

"""header = b""
magic = b"\x89\x50\x4e\x47\x0d\x0a\x1a\x0a"
header += magic
ihdr = b"\x00\x00\x00\x0d\x49\x48\x44\x52"
header +=ihdr
sizes = b"\x00\x00\1\xdc\x00\x00\x00\x1b"
header += sizes
bit_length = b"\x08"
color_type = b"\x06"
other = b"\x00\x00\x00"
crc = b"\xd6\x39\x3e\x4d"

header += bit_length + color_type + other + crc
"""

#get the width and height from IHDR header sent in one of the last paquets
from PIL import Image
im = Image.new("RGB", (0x1dc,0x1b))
im.putdata(res)
im.save("flag.png")


 

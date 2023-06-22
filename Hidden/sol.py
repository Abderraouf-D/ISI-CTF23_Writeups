
#decode the morse code from haystack.txt and put it in haystack.dec

q = open("./haystack.dec",'r').read()


q=q.replace('\n','').replace('BREAK','').replace('E','0').replace('T','1')


open('out.qr','w').write(q)


#use this website the generate the qr code from binary https://bahamas10.github.io/binary-to-qrcode/
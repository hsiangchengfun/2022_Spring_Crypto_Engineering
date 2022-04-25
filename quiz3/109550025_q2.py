
freq = [8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.966,0.153,0.772,4.025,2.406,6.749,7.507,1.929,0.095,5.987,6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074]

#===========================================

with open ('./message1.txt', 'r') as cyinput:
    readcypher = cyinput.read()
    
total2=[]

num2 = int(input()) #num means key length

for p in range(len(readcypher)):
    if readcypher[p].isalpha():
        total2.append(readcypher[p])

key=[0]*num2

for q in range(num2):        
    cypher = total2[q:p:num2]


    alpha2 = [0]*26

    tmp=0

    for j in range(26):
            alpha2[j]=cypher.count( chr(ord('A')+j))

   
    maxid=0
    total = 0
    maxx=0
    for tmp in range(26):
        total = 0
        for i in range(26):
            total += (1000*freq[i] + alpha2[(i+tmp)%26])*(1000*freq[i] + alpha2[(i+tmp)%26]-1)
        if(maxx<total): 
            maxid=tmp
            maxx=total

    total = float(maxx / ((1000+len(cypher)) *(1000 + len(cypher)-1)))
    key[q]=maxid

    
# print(key)
keyalpha=[chr(ord('A'))]*num2
for i in range(len(key)):
    keyalpha[i] = chr(ord('A') + key[i])

for i in range(len(key)):
    print(keyalpha[i],end='')



fp=open("109550025_msg1.txt","w")

for i in range(len(readcypher)):
    tt = (ord(  total2[i] ) - (key[i%num2]))
    if tt < (ord('A')):
        tt +=26
    total2[i] = chr( tt ) 
    fp.write(total2[i])

fp.close()

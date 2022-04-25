
# from curses.ascii import isalpha


with open ('./new.txt', 'r') as finput:
    list = finput.read()
    
total=[]  
num = 5 #num means key length
for i in range(len(list)):
    if list[i].isalpha():
        total.append(list[i])
        
list1 = total[0:i:num]


alpha = [0]*26


for j in range(26):
    alpha[j]=list1.count( chr(ord('A')+j))
 





with open ('./message1.txt', 'r') as cyinput:
    readcypher = cyinput.read()
    
total2=[]
num2 = 5 #num means key length
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
            total += (alpha[i] + alpha2[(i+tmp)%26])*(alpha[i] + alpha2[(i+tmp)%26]-1)
        if(maxx<total): 
            maxid=tmp
            maxx=total

    total = float(maxx / (len(list1)+len(cypher)) *((len(list1) + len(cypher)-1)))
    key[q]=maxid
    print(maxid)
    print(total)
    
print(key)
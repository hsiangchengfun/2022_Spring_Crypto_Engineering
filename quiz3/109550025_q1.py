
with open ('./message1.txt', 'r') as finput:
    list = finput.read()
    
total=[]  
num = 5 #num means key length
for i in range(len(list)):
    if list[i]!=" ":
        total.append(list[i])
        
list1 = total[0:i:num]


alpha = [0]*26


for j in range(26):
    alpha[j]=list1.count( chr(ord('A')+j))
 

total = 0
for i in range(26):
    total += alpha[i]*(alpha[i]-1)
    
total = float(total / (len(list1)*(len(list1)-1)))

print(num)
#print(total)


import hashlib

def myMD5(x):
    hashval = hashlib.md5(bytes.fromhex(x))
    ans = hashval.hexdigest()[:4]
    return ans



ipt = input()
ipt = myMD5(ipt)

compare = 98567647293793288615600602462446642048


while(1):
    compare = hex(compare)[2:]
    if(ipt == myMD5(compare)):
        print(ipt,end=" ")
        print(compare)
        break;
    compare = (int)(compare,16)
    compare+=1
emails=["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
hs=set()
temp=['']*len(emails)
i=0
for mail in emails:
        dot=0
        plus=0
        atrate=0
        for ch in mail:
            if ch=='.' and dot!=1 and plus!=1:
                continue
            if ch=='+':
                plus=1
                continue
            if ch=='@':
                atrate=1
                dot=1
                plus=0
            if plus==1:
                continue
            temp[i]=temp[i]+ch
        print(temp[i]+ " ")    
        hs.add(temp[i])
        i=i+1
print(len(hs))
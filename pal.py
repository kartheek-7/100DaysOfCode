#nearest Highest palindrome number to a given number
n=(input("Enter the number: "))
d=len(n)
#for even digits
if d%2==0:
    count=0
    mid=int(d/2)
    for i in range(mid):
        if int(n[mid-1-i])>=int(n[mid+i]):
            count=count+1
        else:
            lsn=str(int(n[0:mid])+1)
            rsn="".join(reversed(lsn))
            #return(lsn+rsn)
            print(lsn+rsn)
            break
            
    if count==mid:
        lsn=n[0:mid]
        rsn="".join(reversed(lsn))
        #return(lsn+rsn)
        print(lsn+rsn)
        
#for odd digits

else:
    count=0
    mid=int(d/2)
    for i in range(mid):
        if int(n[mid-1-i])>=int(n[mid+1+i]):
            count=count+1
        else:
            lsn=str(int(n[0:mid+1])+1)
            rsn="".join(reversed(lsn[0:mid]))
            #return(lsn+rsn)
            print(lsn+rsn)
            break
            
            
    if count==mid:
        lsn=n[0:mid]
        rsn="".join(reversed(lsn))
        print(lsn+n[mid]+rsn)
        
            
            
#nearest Highest palindrome number to a given number

def nhpalindrome(n): 
    d=len(n)
    if d==1:
        if int(n)==9:
            return 11
        else:
            return (int(n)+1)
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
                return(lsn+rsn)
                #print(lsn+rsn)
                break
                
        if count==mid:
            lsn=n[0:mid]
            rsn="".join(reversed(lsn))
            if lsn+rsn==n:
                    return nhpalindrome(str(int(n)+1))
            else:
                return(lsn+rsn)
                #print(lsn+rsn)
            
    #for odd digits

    if d%2==1 and d!=1:
        count=0
        mid=int(d/2)
        for i in range(mid):
            if int(n[mid-1-i])>=int(n[mid+1+i]):
                count=count+1
            else:
                lsn=str(int(n[0:mid+1])+1)
                rsn="".join(reversed(lsn[0:mid]))
                return(lsn+rsn)
                #print(lsn+rsn)
                break
                
                
        if count==mid:
            lsn=n[0:mid]
            rsn="".join(reversed(lsn))
            if lsn+n[mid]+rsn==n:
                    return nhpalindrome(str(int(n)+1))
            else:
                return(lsn+n[mid]+rsn)
                #print(lsn+n[mid]+rsn)
        
     
n=(input("Enter the number: "))
print(f"Nearest Highest palindrome of {n} is: {nhpalindrome(n)}")       
            
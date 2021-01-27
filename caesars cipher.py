q=int(input())

for num in range(q):
    s=input()               #should contain only uppercase
    t=input()              #should contain only upper case

    if len(s)==len(t):
        flag=ord(t[0])-ord(s[0])
        
        for i in range(0,len(s)-1):
       
            diff=ord(t[i])-ord(s[i])
            diff2=ord(t[i+1])-ord(s[i+1])

            if diff<0:
                flag=diff+26

            if diff!=diff2:
                flag=(-1)
                break
    else:
        flag=(-1)
        
    print(flag)



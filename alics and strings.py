str_a=input()
str_b=input()
flag='YES'
if len(str_a)==len(str_b):
    for i in range(0,len(str_a)):
        if str_a[i]>str_b[i]:  #we can not substract from string
            flag='NO'
            break
else:
    flag='NO'
print(flag)

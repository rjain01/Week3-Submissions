#needle in haystack

l=int(input())   #length of needle
n=input()   #needle
hay=input()  #haystack

for i in range(len(hay)):
    if hay[i:i+l]==n:
        print(i

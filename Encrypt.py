list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
c=0
k=t=0
z=""
text=input("Enter plan text ")
text= text.lower()
key=input("Enter The Key ")
for i in range(len(text)):
    if text[t]==' ':
        z= z +' '
        t +=1
    elif k != len(key):
        c=((list.index(text[t]))+list.index(key[k]))%26
        t +=1
        k +=1
        z = z+ list[c]
    else:
        k=0
        c=((list.index(text[t]))+list.index(key[k]))%26
        k+=1
        t+=1
        z = z+ list[c]

print (z)

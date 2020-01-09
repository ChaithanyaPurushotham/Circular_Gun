num=int(input("Enter the number of people"))
lst=[]
lst1=[]
for i in range(1,num+1):
    lst.append(i)
    lst1.append(i)
for j in range(len(lst)):
    k=j
    if(k<len(lst)-1):
        lst.remove(lst[k+1])
        k=k+1
print("**",lst)
def circlegun(lst,lst1):
    while(len(lst)>=2):
        pop=[]
        if((lst[len(lst)-1])==lst1[len(lst1)-1]):
                    pop=lst[len(lst)-1]
                    lst.pop()
                    lst.insert(0,pop)
                    lst1.clear()
                    lst1=lst.copy()
        else:
                    lst1.clear()
                    lst1=lst.copy()
                    
        for j in range(len(lst)):
            if(j<=len(lst)-2):
                lst.remove(lst[j+1])
                j=j+1
                print("***",lst)
    print(lst," is the saver in the",num,"people")
circlegun(lst,lst1)
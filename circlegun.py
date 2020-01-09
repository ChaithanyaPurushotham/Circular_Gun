num=int(input("Enter the num"))
for i in range(1,num):
    k=2**i
    if(k>num):
        break
    else:
        square=k
        print("square= ",square)
saver=2*(num-square)+1
print("saver= ",saver)
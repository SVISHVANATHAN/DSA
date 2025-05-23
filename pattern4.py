n=int(input())
#pattern1
for i in range(1,n+1):
    print("*"*i,end=" ")
#pattern2
print()
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print(" ",end="")
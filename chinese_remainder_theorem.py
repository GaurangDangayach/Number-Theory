k=int(input("Enter the number of eqns:"))
b=[]
n=[]
m=[]
for i in range(k):
    b1,n1=input().split()
    b.append(int(b1))
    n.append(int(n1))
N=1
for i in range(k):
    N=N*n[i]
for i in range(k):
    N1=N//n[i]
    for j in range(1,n[i]):
        if (j*N1)%n[i]==1:
            m.append(j)
            break
ans=0
for i in range(k):
    ans=ans+N//n[i]*b[i]*m[i]
ans=ans%N
print(ans,"( mod",N,")")
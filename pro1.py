a=[]
t=int(input("Enter the no. of test cases:"))
for i in range(t):
    n=int(input("Enter the no. of elements:"))
    k=int(input("Enter the k value:"))
    for j in range(n):
      a[j]=int(input())
    a.sort()
    if k<=a[0]:
        print("0")
    else:
        print(k-a[0])

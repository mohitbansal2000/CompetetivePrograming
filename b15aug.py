n=int(input())
a=list(map(int,input().split()))
a_count=[]
great=len(bin(max(a)))-2

for x in a:
    x_bin= bin(x)[2:]
    one_count=x_bin.count('1')
    a_count.append([great - one_count,one_count])

equivalance_count=0
for i in range(n):
    for j in range(i,n):
        zeroes=0
        ones=0
        for k in a_count[i:j+1]:
            zeroes +=k[0]
            ones+=k[1]
        if zeroes==ones:
            equivalance_count+=1
        
print('0'*(great-(len(bin(equivalance_count))-2))+bin(equivalance_count)[2:])

"""
3
2 7 10

0011

3
2 3 4
010

"""

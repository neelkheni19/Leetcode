nums = list(map(int,input().split()))
target = int(input())
temp = 0
for i in range(len(nums)):
    temp=0
    for j in range(i):
        temp = nums[i]+nums[j]
        if(temp == target):
            print(j,i)
            
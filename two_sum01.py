# two sums array problem
def sum_two(arr,target):
    for i in range(0,len(arr)):
        for j in range (i+1,len(arr)):
            sum=arr[i]+arr[j]
            if sum==target:
                return [i,j]
arr= list(map(int,input("nums:").strip("[]").split(",")))
target=int(input("target:"))
print(sum_two(arr,target))




def four_sum(nums,target):
    ls = []
    for i in range(len(nums)):
        val = nums[i]
        for j in range(len(nums)):
            if i == j:
                continue
            try:
                Sum = val + sum(nums[j:j+3])
                if Sum == target:
                    arr = [val] + nums[j:j+3]
                    if len(arr) == 4:
                        if arr not in ls:
                            ls.append(arr)
            except :
                break
    return ls

def main():
    nums = list(map(int,input().strip().split()))
    target = int(input())
    res = four_sum(nums,target)
    print(res)

if __name__ == '__main__':
    main()
for i in range(int(input())):
    num = int(input())
    nums = [num]
    while 1 not in nums:
        if num % 2 == 0:
            num /= 2
            nums.append(num)
        else:
            num = 3 * num + 1
            nums.append(num)
    print(len(nums))
    
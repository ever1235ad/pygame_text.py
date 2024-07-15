def reset_arr(flag):
    n = len(flag)
    for i in range(n):
        flag[i] = flag[i] * flag[i]
    print(flag)
    for m in range(n-1):
        print(m)
        for i in range(n-m-1):
            print(i)
            print(n-m-1)
            if flag[i] > flag[i+1]:
                flag[i],flag[i+1] = flag[i+1],flag[i]
    return flag

number = [3,1,4,1,5,9,10,2,30]
sorted_numbers = reset_arr(number)
print(sorted_numbers)
#算法训练
'''两数之和'''
'''
arr = [64,3,5,23,42,2,111]
return_arr = []
target = 113
length = len(arr)
for i in range(0,length - 1):
    for j in range(1,length - i):
        if arr[i] + arr[i+j] == target:
            return_arr.append(arr[i])
            return_arr.append(arr[i+j])
print(return_arr)
'''



'''插入数'''
'''
arr_1 = [1,2,5,6]
target = 7
length = len(arr_1)
low = 0
high = length
while(low + 1 < high):
    mid = int((low + high)/2)
    if target < arr_1[mid]:
        high = mid
    else:
        low = mid
arr_1.insert(low + 1,target)
print(arr_1)
'''



'''合并两个有序链表'''
'''
arr_1 = [1,2,5,6]
target_arr = [7,2,5,9]
length_arr1 = len(arr_1)
length_arr2 = len(target_arr)
low = 0
high = length_arr1
for i in target_arr:
    while(low + 1 < high):
        mid = int((low + high)/2)
        if i < arr_1[mid]:
            high = mid
        else:
            low = mid
    arr_1.insert(low + 1,i)
    low = 0
    high = len(arr_1) - 1
print(arr_1)
'''        


'''寻找旋转排序数组中的最小值'''
'''arr = [1,2,3,4,5,6,7,8,9]
length = len(arr)
min = 0
new_arr = []
arr_low = []
arr_high = []
index = int(input(f"请输入旋转点,范围为1--{length}\n"))
arr_low = arr[0:index - 1]
arr_high = arr[index - 1:length]
new_arr = arr_high + arr_low
#new_arr = [*arr_high , *arr_low]
print(new_arr)'''

'''有效字符串'''            #栈数据结构的基本应用 pop()相当于删除栈顶元素(列表末尾)
'''
stack = []
top = 0
input_str = input("请输入字符串\n")
for str in input_str:
    if str == '(':
        stack.append(')')
    if str == '[':
        stack.append(']')
    if str == '{':
        stack.append('}')
    if str == ')':
        top = len(stack) - 1
        if stack[top] == ')':
            stack.pop()
    if str == ']':
        top = len(stack) - 1
        if stack[top] == ']':
            stack.pop()
    if str == ']':
        top = len(stack) - 1
        if stack[top] == '}':
            stack.pop()
if stack == []:
    print("True")
else:
    print("False")
'''


'''两数之和||'''

'''    #参考两数之和|#
arr = [64,3,5,23,42,2,111]
return_arr = []
target = 8
length = len(arr)
for i in range(0,length - 1):
    for j in range(1,length - i):
        if arr[i] + arr[i+j] == target:
            return_arr.append(i + 1)
            return_arr.append(i + j + 1)
print(return_arr)
'''
'''   解法二：双指针    '''
#It is too late,princess. It is time to go to bed. 

'''反转链表'''     #python中链表怎么实现

'''class Listnode():
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next
def reverse_list(head):'''
    
    
    
'''反转字符串'''
'''
str = input("请输入一个字符串\n")
def reverse_str(str):
    str_arr = list(str)
    length = len(str_arr)
    low = 0
    top = length - 1
    while(low < top):
        str_arr[low],str_arr[top] = str_arr[top],str_arr[low]
        low += 1
        top -= 1
    new_str = ''.join(str_arr)
    return new_str
new_str = reverse_str(str)
print(new_str)
'''

'''最长公前缀'''

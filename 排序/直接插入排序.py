def Insert_sort(arr,n):
    i=0
    j=0
    for i in range(2,n):
        if arr[i] < arr[i-1]:
#             复制哨兵
            arr[0] = arr[i]
            j = i-1
            while arr[j]>arr[0]:
                # 当当前元素大于i选中元素时，当前元素向后移动
                arr[j+1] = arr[j]
                j-=1
            arr[j+1] = arr[0]

if __name__ == "__main__":
    arr = [0,3,5,7,16,10,1]
    length = len(arr)
    Insert_sort(arr,length)
    for i in range(1,length):
        print(arr[i],end=" ")

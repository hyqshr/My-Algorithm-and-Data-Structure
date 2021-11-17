
def partition(arr, low, high):
    i = (low -1)         # index of smaller element
    pivot = arr[high]     # pivot

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+ 1
            arr[i], arr[j] = arr[j], arr[i]
            print('swap',arr[i],'with',arr[j])
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print('force swap', arr[i+1], 'with', arr[high])
    print(arr[low:high],'  i + 1 is ',i + 1)
    return (i + 1)

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        print(low,'-',high,'call',pi)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

        print('\n')
if __name__ == '__main__':

    arr = [6,5,4,3,2,1]
    print('Array start as',arr)
    print('\n','*'*50,'\n')
    print(quickSort(arr,0,len(arr) - 1))
    print(arr)
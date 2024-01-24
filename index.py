#Bubble sorting algirithm...................
def bubble_sort(arr):
    lenght_of_arr = len(arr)

    #tranverse through all the array element
    for i in range(lenght_of_arr):
        swapped= False
        for j in range(0, lenght_of_arr - i - 1):
            #tranvese the array from 0 to n-i-1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped=True
        if (swapped == False):
            break

if __name__ == "__main__" :
    print("Enter your array here:")
    arr = list(map(int, input().split()))
    print("----------------------")
    bubble_sort(arr)
    print("sorted array")
    for i in range(len(arr)):
        print("%d " % arr[i], end="")
        






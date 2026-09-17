# Problem: Find the second highest distinct score
# from a list of scores.

if __name__ == '__main__':
    n = int(input("Enter Number of Inputs : "))
    arr = list(map(int, input().split()))
    
    #first we will sort the array using 2 pointer slider 
    #themn we check the highest number
    #then we check whether there is a value same as highest 
    #if there is same value same as value then we - 1 the inedx from right
    #then we check it one more time with highest value 
    #if its not equal to highst value then thats our 2nd highest value 
    #because we had sort the list in ascending order

    length = len(arr)
    swapped = True

    while swapped:
        swapped = False
        left = 0
        right = 1

        while right < length:
            if arr[left] > arr[right]:
                arr[left], arr[right] = arr[right], arr[left]
                swapped = True

            left += 1
            right += 1
            
        print(arr)

    highest = arr[-1]
    right = length - 2

    while arr[right] == highest:
        right -= 1

    print(arr[right])
n = int(input())
words =[]

def bigger_Is_greater(word):
    arr = list(word)
    p = len(word) - 2
    while p >= 0 and arr[p] >= arr[p+1]:
        p -= 1
    if p == -1:
        return "no answer"
    
    bigger_Is_greater = len(word) - 1
    while bigger_Is_greater > p and arr[bigger_Is_greater] <= arr[p]:
        bigger_Is_greater -= 1
    
    arr[p], arr[bigger_Is_greater] = arr[bigger_Is_greater], arr[p]
    arr[p+1:] = sorted(arr[p+1:])
    return "".join(arr)

for i in range(n):
    x = input()
    words.append(x)

for word in words:
    print(bigger_Is_greater(word))
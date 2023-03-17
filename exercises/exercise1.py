words = []

n = int(input())

def func(arr):
    for i in range(n):
        w = input()
        arr.append(w)

def count(arr):
    word_count = {}
    for word in arr:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def output(words):
    print(len(count(words)))
    arr = list(count(words).values())
    for i in arr:
        print(i, end = ' ')

func(words)
output(words)

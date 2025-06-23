
lst = [1,2,3,2,3,4,3,2,5,4,3,5,3,1,3,1,3,2,3,1,2]

def most_common(lst):
    freq = {}
    for i in lst:
        freq[i] = freq.get(i, 0) + 1
    return max(freq, key=freq.get)

print(most_common(lst))


from collections import Counter

def most_frequent(lst):
    return Counter(lst).most_common(1)[0][0]
print(most_frequent(lst))















import timeit

print(timeit.timeit('most_common(lst)', globals=globals(), number=1000))
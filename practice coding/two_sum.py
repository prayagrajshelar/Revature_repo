lst = [1,2,3,4,5,6,7,8,2,3,2,5,3]
target = 7
def pairs_target(lst,target):
    seen=set()
    for n in lst:
        if target-n in seen:
            return (target-n,n)
        seen.add(n)
    return None
print(pairs_target(lst,target))
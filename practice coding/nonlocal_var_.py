# def outer():
#     count = 0
#     def inner():
#         count+=1
#         print(count)
#     inner()
#     inner()
# outer()


# With NonLocal

def outer():
    count = 0
    def inner():
        nonlocal count
        count+=1
        print(count)
    inner()
    inner()
outer()

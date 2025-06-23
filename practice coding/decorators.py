def pre_post(func):
    def wrapper_func():
        print(f"Pre Task before {func.__name__} call")
        func()
        print(f"Post Task after {func.__name__} call")

    return wrapper_func

@pre_post
def main_task():
    print("Main Task")

main_task()
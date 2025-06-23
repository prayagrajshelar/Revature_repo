class lessMarks(Exception):
    pass

def user_marks(marks):
    if marks < 35:
        raise lessMarks("You are fail")
    else:
        print("You are pass")

try:
    marks = int(input("Enter your marks: "))
    user_marks(marks)
except lessMarks as e:
    print(f"Custom Exception: {e}")
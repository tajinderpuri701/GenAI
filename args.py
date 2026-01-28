def average_marks(*args):
    valid_marks = [mark for mark in args if mark >= 0]
    
    if not valid_marks:
        return 0
    return sum(valid_marks) / len(valid_marks)
print(average_marks(85, 90, -5, 70)) 
print(average_marks(-1, -2, -3))      
print(average_marks())                


def filter_details(**kwargs):
    for key, value in kwargs.items():
        if isinstance(value, str):
            print(f"{key} = {value}")
filter_details(name="karan", age=30, city="bathinda")



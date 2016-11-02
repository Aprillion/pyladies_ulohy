def empty_function():
    pass

def do_something():
    print("inside function do_something")
    
def return_something():
    return "inside function return_something"

def rectangle_cicumference(width, height):
    return 2 * (width + height)
    
print("main script")
x = return_something()
do_something()
print(rectangle_cicumference(4, 2))
print("the end")















#Local Variables:
# print(a)  # This would raise an error since 'local_var' is not accessible outside the function

# commit "Global Variables:"

a = "I am global"

def f():
    global a
    a = "Modified globally"
    print(a)

f()
print(a)
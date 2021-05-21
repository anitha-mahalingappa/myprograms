
def my_add(arg1,arg2):
    add = arg1+arg2
    print(add)
    return add
def my_sub(arg3,arg4):
    sub = arg3-arg4
    print(sub)
    return sub
#main prog
my_num1 = int(input(" enter the number : "))
my_num2 = int(input(" enter the number : "))
var1 = my_add(my_num1,my_num2)
var2 = my_sub(my_num1,my_num2)
print(var1,var2)
def print_params(a=1, b=25, c= True):                #*args  ** kwargs
    print(a,b,c)

print_params()
def print_params(b=25):
    print(b)

print_params()
def print_params(c=[1,2,3]):
    print(c)


print_params()

def print_params(a,b,c):
    print(a,b,c)

values_list = [20,30,40]
print_params(*values_list)

def print_params(a,b,c):
    print(a, b, c)

values_dict = {'a':12,'b':36,'c':44}
print_params(**values_dict)

def print_params(**kwargs):
    print(kwargs)

values_dict = {'a':12,'b':36,'c':44}
print_params(**values_dict)

def print_params(a,b,c):
    print(a,b,c)

values_list_2 = [54,32,'"str"42']
print_params(*values_list_2)
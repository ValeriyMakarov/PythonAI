
def print_type(*value):
    if len(value)==1 and type(value[0]) in [list, dict, set]:
        print(type(value[0]))
    else:
        print(type(value))

if __name__ == '__main__':
    print_type(1,2,3)
    print_type([1,2,3])
    print_type({1,2,3})
    print_type({1:1,2:2,3:3})


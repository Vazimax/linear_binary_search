def linear_search(list,target):
    for i in list :
        if i == target:
            return i
    return None

def verify(index):
    if index is not None:
        print(f'The target is {index}')
    else :
        print("The target not found in the list")

numbers = [ x for x in range(0,99999999)]
res = linear_search(numbers,450)

verify(res)


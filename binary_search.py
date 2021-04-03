def binary_search(list,target):
    first = 0
    last = len(list) - 1 

    while first <= last :
        midpoint = (first + last)//2

        if list[midpoint] == target :
            return f"The target is {midpoint}"
        elif list[midpoint] < target :
            first = midpoint + 1 
        else :
            last = midpoint - 1 

    return None

def verify(index):
    if index is None:
        print("The target not found in the list")
        
    else :
        print(f"The target is {index}")

numbers = [ x for x in range(0,99999999)]
res = binary_search(numbers,450)

verify(res)


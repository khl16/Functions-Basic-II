1.
def  countDown(num):
    newList = []
    for X in range(num, -1, -1):
        newList.append(X)
    return newList
print(countDown(5))

2.
def print_and_return(list):
    print(list[0])
    return list[1]
print (print_and_return([3,77]))

3.
def first_plus_length(list):
    print(list[0])
    return len(list)
print(first_plus_length([55,46,2]))

4.
def values_greater_than_second(list):
    if len(list)<2:
        return False
    newList = []
    # greaterThan = list[1]
    for val in list:
        if val>list[1]:
            newList.append(val)
    print(len(newList))    
    return newList
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([5,0,3,2,1,4]))
print(values_greater_than_second([1]))
print(values_greater_than_second([]))

5.
def length_and_value(size,value):
    newList = []
    for X in range(size):
        newList.append(value)
    return newList
print(length_and_value(3,8))
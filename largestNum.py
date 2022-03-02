
def find_larget(numbers):
    num=0
    for i in numbers:
        if i>num:
            num=i
    return num

print(find_larget([7,17,13,19,5]));
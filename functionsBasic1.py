#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# predict: console will print 5, correct

#2
def number_of_military_branches():
    return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# predict: console will give error since number of days is not defined, correct

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# predict: console will return 5 but not 10, because this was done first, correct

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# predict: console will showing both 5 and 10, incorrect:shows only 5

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# predict: console will simply print 5, incorrect

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# predict: Values passed thru the function are 3+5. Console will print 8, Incorrect

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# Console will print 25 as a string, correct

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# predict: 100 and 10 will be printed, but not 7, correct

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# predict: function returns 7 and 14 only, incorrect

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# predict: return 8 only, code stops here and does not return 10, correct

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# predict: 500 is printed 3 times, the function returns nothing, incorrect

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# predict: 500, 300, 500, 500, incorrect

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# predict: 500, 500, 300, incorrect

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# predict: Nothing because the function returns nothing, incorrect

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# predict: 1,3,5,10, correct
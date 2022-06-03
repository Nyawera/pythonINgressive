
from calendar import week
import numbers
from re import X
from traceback import FrameSummary


daysinweek = [1,2,3,4,5,6,7,8,9,10]
for i in daysinweek:
    if i > 5:
        print(i)

daysinweek = [5,3,4,4,5,6,7,8,99]    
daysinweek.sort()
print(daysinweek)

daysinweek = [1,23,4,67,90,5,34]
daysinweek.insert(2,15)
print(daysinweek)

daysinweek = [3,5,6,7,9]
daysinweek.append(23)
print(daysinweek)

daysinweek = [1,1,1,2,3,5,6,7,7,7]
print(daysinweek.count(1))

fruits = ["orange","mango","orange"]
print(fruits.remove("orange"))

numbers = [4,5,6,7,8]
print(numbers.remove(7))

prime_numbers = [2, 3, 5, 7, 9, 11]

# remove 9 from the list
prime_numbers.remove(9)

prime_numbers = [2, 3, 5, 7, 9, 11]

# remove 9 from the list
prime_numbers.remove(9)

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


daysinweek = [2,3,4,6]
daysinweek.remove(6)
print(daysinweek)

cars = ["Nissan","subaru","Mercedez","IBM"]
cars.remove("Nissan")
print(cars)

colors = ["red","blue","orange"]
colors.reverse()
print(colors)

gender = ["Male","female"]
gender.reverse()
print(gender)

# Names = ["Tut","Nyawera","Lham"]
# X.pop(2)
# print(X)

fruits = ['apple', 'banana', 'cherry']

x = fruits.pop(1)

print(x)

names = ["Tut","Nyawera","Lham"]
a = names.pop(2)
print(a)



# while loops

number = 1

while number <= 50:
    if number % 2 == 0:  # prints even numbers only
        print(number)
    number = number + 1

list = []

while len(list) < 5:
    new_name = input("Please add a new name: ").strip().capitalize()
    list.append(new_name)

print("Sorry. This list is full")
print(list)
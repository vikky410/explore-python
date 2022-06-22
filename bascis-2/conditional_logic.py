# Ternary operator
# is_friend = True
# can_message = "message allowed" if is_friend else "message not allowed"
# print(can_message)
#
# for i in can_message:
#     print(i)
#
# for i in (1, 2, 3):
#     for (j) in (4, 5, 6):
#         pass
#
# print(i)
# print(j)
#
# user = {
#     "name": "Golem",
#     "age": 507,
#     "can_swim": False
# }
#
# # items, values, keys
# for i in user.values():
#     print(i)

# my_list = [1, 2, 3, 4, 5]
#
# counter = 0
# for i in my_list:
#     counter += i
#
# print(counter)

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

for row in picture:
    for pixel in row:
        if pixel == 0:
            print(" ", end="")  # default to new line end = \n
        else:
            print("*", end="")
    print('')  # need a new line after row iteration


# find duplicates
some_list = ['a', 'b', 'c', 'd', 'b', 'm', 'n', 'n']


duplicates = []

for i in some_list:
    if some_list.count(i) > 1 and i not in duplicates:
        duplicates.append(i)

print(duplicates)

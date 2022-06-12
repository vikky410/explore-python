# List
amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]
# print(amazon_cart[0:2])

# pass by reference
amazon_cart2 = amazon_cart
amazon_cart2[0] = 'Gum'
# both variable got latest value
print(amazon_cart2)
print(amazon_cart)

# copy value into another variable
amazon_cart3 = amazon_cart[:]
amazon_cart3[0] = 'Watch'
print(amazon_cart)
print(amazon_cart3)

# action on list
# len()

# add
#   append() // add value in end of list, modify in place doesn't copy list
#   insert(index, value) // modify in place doesn't copy list
#   extend()


# removing
#   pop(index)
#   remove(value)

matrix_ex = [
    [0, 1, 2],
    [3, 4, 5]
]

print(f'length of matrix: {len(matrix_ex)}')
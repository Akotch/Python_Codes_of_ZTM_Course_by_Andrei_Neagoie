# What is the output of this code?
# Before you click RUN, guess the output of each print statement!

new_list = ['a', 'b', 'c']

print(new_list[1])   # Output: 'b'  (Index 1 corresponds to 'b')

print(new_list[-2])  # Output: 'b'  (Negative index -2 corresponds to 'b')

print(new_list[1:3])
# Output: ['b', 'c']  (Slice from index 1 to 2, excluding 3)

new_list[0] = 'z'

print(new_list)      # Output: ['z', 'b', 'c']  (Element at index 0 is changed)


my_list = [1, 2, 3]

bonus = my_list + [5]  # Creates a new list [1, 2, 3, 5]

my_list[0] = 'z'       # Modifies the original list my_list

print(my_list)         # Output: ['z', 2, 3]  (Only my_list is modified)

print(bonus)           # Output: [1, 2, 3, 5]  (bonus remains unchanged)

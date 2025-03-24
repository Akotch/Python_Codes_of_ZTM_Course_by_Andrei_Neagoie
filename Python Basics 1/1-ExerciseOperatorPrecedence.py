# In Python, operator precedence (preference rule) follows this order:
#
# 1. Parentheses () – Operations inside parentheses are executed first.
# 2. Exponentiation ** – Evaluated next (right to left).
# 3. Multiplication *, Division /, Floor Division //, and Modulus % – Evaluated from left to right.
# 4. Addition + and Subtraction - – Evaluated last, from left to right.
#
# When operators have the same precedence, Python evaluates them from left to right,
# except for exponentiation (**), which is right to left.

# Guess the output of each expression before running the code

# (5 + 4) * 10 / 2
# Step 1: 5 + 4 = 9
# Step 2: 9 * 10 = 90
# Step 3: 90 / 2 = 45.0 (Division in Python 3 results in a float)
print((5 + 4) * 10 / 2)  # Output: 45.0

# ((5 + 4) * 10) / 2
# Step 1: 5 + 4 = 9
# Step 2: 9 * 10 = 90
# Step 3: 90 / 2 = 45.0 (Same as the previous one, just different grouping)
print(((5 + 4) * 10) / 2)  # Output: 45.0

# (5 + 4) * (10 / 2)
# Step 1: 5 + 4 = 9
# Step 2: 10 / 2 = 5.0 (Division results in float)
# Step 3: 9 * 5.0 = 45.0
print((5 + 4) * (10 / 2))  # Output: 45.0

# 5 + (4 * 10) / 2
# Step 1: 4 * 10 = 40
# Step 2: 40 / 2 = 20.0 (Division results in float)
# Step 3: 5 + 20.0 = 25.0
print(5 + (4 * 10) / 2)  # Output: 25.0

# 5 + 4 * 10 // 2
# Step 1: 4 * 10 = 40
# Step 2: 40 // 2 = 20 (Integer division '//' results in an integer)
# Step 3: 5 + 20 = 25
print(5 + 4 * 10 // 2)  # Output: 25

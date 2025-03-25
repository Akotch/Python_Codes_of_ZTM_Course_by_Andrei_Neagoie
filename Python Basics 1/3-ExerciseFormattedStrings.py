# 1. What would be the output of the below 4 print statements?
# Try to answer these before you click RUN!

# Using .format() without position numbers
print("Hello {}, your balance is {}.".format("Cindy", 50))
# "Cindy" replaces the first `{}`, and `50` replaces the second `{}`.
# Output: Hello Cindy, your balance is 50.

# Using .format() with positional arguments (index-based)
print("Hello {0}, your balance is {1}.".format("Cindy", 50))
# `{0}` refers to "Cindy" (first argument), `{1}` refers to `50` (second argument).
# Output: Hello Cindy, your balance is 50.

# Using .format() with named placeholders
print("Hello {name}, your balance is {amount}.".format(
    name="Cindy", amount=50))
# `{name}` is replaced with "Cindy", `{amount}` is replaced with `50`.
# Output: Hello Cindy, your balance is 50.

# Mixing positional and named arguments
print("Hello {0}, your balance is {amount}.".format("Cindy", amount=50))
# `{0}` takes "Cindy" (first argument), `{amount}` takes `50` from the named argument.
# Output: Hello Cindy, your balance is 50.

# 2. How would you write this using an f-string?

name = 'Cindy'
amount = 50

print(f"Hello {name}, your balance is {amount}.")
# Using f-string, which is more readable and efficient.
# Output: Hello Cindy, your balance is 50.

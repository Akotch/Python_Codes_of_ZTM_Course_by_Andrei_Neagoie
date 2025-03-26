python = 'I am PYHTON'

print(python[1:4])
# ' am'  -> Characters from index 1 to 3 ('a', 'm', and space)

print(python[1:])    # ' am PYHTON' -> Everything from index 1 to the end

print(python[:])     # 'I am PYHTON' -> Full string (same as python[0:])

print(python[1:100])
# ' am PYHTON' -> Since the string is shorter than 100, it stops at the last character

print(python[-1])    # 'N' -> Last character of the string

print(python[-4])    # 'H' -> Fourth character from the end

print(python[:-3])   # 'I am PYH' -> Everything except the last 3 characters

print(python[-3:])   # 'TON' -> Last 3 characters of the string

print(python[::-1])  # 'NOTHYP ma I' -> Reversed string

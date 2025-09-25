def split_string(s, delimiter):
    tokens = s.split(delimiter)
    for token in tokens:
        print(token)

print("Test 1:")
split_string("That's my house,\" I said.", " ")
print("\n")
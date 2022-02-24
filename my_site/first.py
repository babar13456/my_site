example_2 = (49, 80, 78, 49)

another = list(example_2)

another.insert(2, "New")
another.append("Hello")

example_2 = tuple(another)

print(example_2)
import random

random_integer = random.randint(1, 10)
print(random_integer)

# 0.000000 - 0.999999...
random_float = random.random()
print(random_float)

random_to_five = random_float * 5
print(random_to_five)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

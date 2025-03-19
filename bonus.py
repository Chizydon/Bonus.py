# Using map, write a program that add 0.01 bonus to this salary
salary = [2000, 4000, 6000, 8000]
bonus = list(map(lambda x:x + 0.01, salary))
print (bonus)
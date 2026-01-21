#for value in range(1,21):
    #print(value)

#for value in range(1,1000000):
    #print(value)

numbers = list(range(1,1000000))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#for value in range(1,21,2):
    #print(value)

multiples_of_three = list(range(3,31,3))
for number in multiples_of_three:
    print(number)

cubes = [value ** 3 for value in range(1,11)]
print(cubes)
for cube in cubes:
    print(cube)


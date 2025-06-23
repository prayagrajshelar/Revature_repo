import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0][0] = 99

print("Original:", original)
print("Shallow:", shallow)
print("Deep:   ", deep)

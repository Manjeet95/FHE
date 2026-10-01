# Representing a polynomial using a Python list

p = [3, 4, 5, 1]
q = [1, 6, 3, 9]

# Ordinary Addition
result_add = []

for i in range(len(p)):
    result_add.append(p[i] + q[i])

# Ordinary Multiplication
result_mult = [0] * (len(p) + len(q) - 1)

for i in range(len(p)):
    for j in range(len(q)):
        result_mult[i + j] += p[i] * q[j]

print("Ordinary addition:")
print("p =", p)
print("q =", q)
print("p + q =", result_add)

print("\nOrdinary multiplication:")
print("p * q =", result_mult)

# Representing a polynomial using a Python list

# Coefficient modulus
m = int(input("\nEnter the coefficient modulus: "))

p = [3, 4, 5, 1]
q = [1, 6, 3, 9]

# Ordinary Addition
result_add = []

for i in range(len(p)):
    result_add.append((p[i] + q[i]) % m)

# Ordinary Multiplication
result_mult = [0] * (len(p) + len(q) - 1)

for i in range(len(p)):
    for j in range(len(q)):
        result_mult[i + j] += p[i] * q[j]

for i in range(len(result_mult)):
    result_mult[i] = result_mult[i] % m

print("Ordinary addition:")
print("p =", p)
print("q =", q)
print("p + q =", result_add)

print("\nOrdinary multiplication:")
print("p * q =", result_mult)

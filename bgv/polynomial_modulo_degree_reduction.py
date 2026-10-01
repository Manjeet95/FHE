# Representing a polynomial using a Python list

n = int(input("Enter ring dimension n: "))
m = int(input("Enter modulus m: "))

p_values = input(f"Enter {n} coefficients: ")
q_values = input(f"Enter {n}  coefficients: ")

p = list(map(int, p_values.split()))
q = list(map(int, q_values.split()))

#p = [3, 4, 5, 1]
#q = [1, 6, 3, 9]

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

# Degree Reduction After Multiplication

result_red_mult = [0] * n
for i in range(len(result_mult)):
	if i < n:
		result_red_mult[i] = result_mult[i]
	else:
		result_red_mult[i-n] = result_mult[i-n] - result_mult[i]

print("\nMultiplication after polynomial reduction:")
print("p * q mod (x ^ n + 1) = ", result_red_mult) 


# Coefficient Reduction After Degree Reduction of Multiplication

result_coeff_red_mult = [0] * n
for i in range(n):
	result_coeff_red_mult[i] = result_red_mult[i] % m

print("\nMultiplication after polynomial and coefficients reduction:")
print("p * q mod (x ^ n + 1)) mod m = ", result_coeff_red_mult) 

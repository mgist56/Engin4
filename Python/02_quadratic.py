#Quadratic Solver
#Meg Gist

print("Quadratic Solver")

def solve(a, b, c):
    d = b ** 2 - 4 * a * c # this calculates the discriminant
    roots = []

    if d < 0: # if the discriminant is negative, there are no real roots
        roots = ["There are no", "real roots"]
    else:
        roots = [round((-b + math.sqrt(d)) / 2 * a, 2), round((-b - math.sqrt(d)) / 2 * a, 2)] # this line finds both roots and adds them to a list

    return roots

print("Enter the coefficients for ax^2 + bx + c = 0")

a = input("a value: ")
b = input("b value: ")
c = input("c value: ")
print(solve(a,b,c)[0], solve(a,b,c)[1])

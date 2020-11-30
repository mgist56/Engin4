#Quadratic Solver
#Meg Gist

from math import sqrt

def solve(a, b, c):
        a = int(a)
        b = int(b)
        c = int(c)

        disc = ((b**2) - (4*a*c))
        if 0 > disc:
                return "none"
        roots = []
        for i in range(2):
                root1 = round((-b + sqrt((b**2) - (2*a))),2)
                root2 = round((-b + sqrt((b**2) + (2*a))),2)
                root = [root1,root2]
                if root not in roots:
                        roots.append(root)
    return roots

print("Enter the coefficients where ax^2 + bx + c = 0:")
ain = input()
bin = input()
cin = input()

if solve(ain,bin,cin)  == "none":
        print("There are no real roots")

if len(solve(ain,bin,cin)) == 1:

elif len(solve(ain,bin,cin)) == 2:
        print("There are two real roots at", solve[0], "and", solve[1])

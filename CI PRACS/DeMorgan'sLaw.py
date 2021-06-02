X = {"Ayush": 0.2, "Sumit": 0.3, "Nikhil": 0.6, "Sarvar": 0.6, "Akash": 0.5}

Y = {"Ayush": 0.9, "Sumit": 0.9, "Nikhil": 0.4, "Sarvar": 0.5, "Akash": 0.4}

Z = {"Ayush": 0.4, "Sumit": 0.3, "Nikhil": 0.6, "Sarvar": 0.7, "Akash": 0.2}


def Union(A, B):
    U = dict()
    for a, b in zip(A, B):
        if A[a] > B[b]:
            U[a] = A[a]
        else:
            U[b] = B[b]
    return U


def Intersection(A, B):
    I = dict()
    for a, b in zip(A, B):
        if A[a] < B[b]:
            I[a] = A[a]
        else:
            I[b] = B[b]
    return I


def Complement(A):
    C = dict()
    for a in A:
        C[a] = 1 - A[a]
    return C


print("DeMorgan's Law (X U Y)' = X' ∩ Y' is", Complement(Union(X, Y)) == Intersection(Complement(X), Complement(Y)))
print("DeMorgan's Law (X ∩ Y)' = X' U Y' is", Complement(Intersection(X, Y)) == Union(Complement(X), Complement(Y)))

print("\nIdempotency Law X U X = X is", Union(X, X) == X)
print("Idempotency Law X ∩ X = X is", Intersection(X, X) == X)

print("\nCommutativity Law X U Y = X is", Union(X, Y) == Union(Y, X))
print("Commutativity Law 2 is", Intersection(X, Y) == Intersection(Y, X))

print("\nAssociativity Law 1 is", Union(Union(X, Y), Z) == Union(X, Union(Y, Z)))
print("Associativity Law 2 is", Intersection(Intersection(X, Y), Z) == Intersection(X, Intersection(Y, Z)))

print("\nAbsorption Law 1 is", Union(X, Intersection(X, Y)) == X)
print("Absorption Law 2 is", Intersection(X, Union(X, Y)) == X)

print("\nDistributivity Law 1 is", Union(X, Intersection(Y, Z)) == Intersection(Union(X, Y), Union(X, Z)))
print("Distributivity Law 2 is", Intersection(X, Union(Y, Z)) == Union(Intersection(X, Y), Intersection(X, Z)))

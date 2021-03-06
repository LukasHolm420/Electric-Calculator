import math

def main():
    goal = input("Please enter the variable to isolate:\n(W, V, A, R)\n\n:> ")
    if goal == "W":
        find_w()
    elif goal == "V":
        find_v()
    elif goal == "A":
        find_a()
    elif goal == "R":
        find_r()

def find_w():
    print("please choose a set of known variables:\n")
    print("1: V and R")
    print("2: R and A")
    print("3: A and V")
    known = float(input("\n\n:> "))
    if known == 1:
        V = float(input("Enter V: "))
        R = float(input("Enter R: "))
        print("\nusing the formula P = U^2 / Ohm")
        print("\nW = ")
        print(V ** 2 / R)
        end()
    if known == 2:
        R = float(input("Enter R: "))
        A = float(input("Enter A: "))
        print("\nusing the formula P = Ohm * I^2")
        print("\nW = ")
        print(R * A ** 2)
        end()
    if known == 3:
        A = float(input("Enter A: "))
        V = float(input("Enter V: "))
        print("\nusing the formula P = U * I")
        print("\nW = ")
        print(V * A)
        end()


def find_v():
    print("please choose a set of known variables:\n")
    print("1: R and A")
    print("2: A and W")
    print("3: W and R")
    known = float(input("\n\n:> "))
    if known == 1:
        R = float(input("Enter R: "))
        A = float(input("Enter A: "))
        print("\nusing the formula U = Ohm * I")
        print("\nV = ")
        print(R * A)
        end()
    if known == 2:
        A = float(input("Enter A: "))
        W = float(input("Enter W: "))
        print("\nusing the formula U = P / I")
        print("\nV = ")
        print(W / A)
        end()
    if known == 3:
        W = float(input("Enter W: "))
        R = float(input("Enter R: "))
        print("\nusing the formula U = sqrt(P * Ohm)")
        print("\nV = ")
        print(math.sqrt(W * R))
        end()


def find_a():
    print("please choose a set of known variables:\n")
    print("1: W and R")
    print("2: W and V")
    print("3: V and R")
    known = float(input("\n\n:> "))
    if known == 1:
        W = float(input("Enter W: "))
        R = float(input("Enter R: "))
        print("\nusing the formula I = sqrt(P / Ohm) ")
        print("\nA = ")
        print(math.sqrt(W/R))
        end()
    if known == 2:
        W = float(input("Enter W: "))
        V = float(input("Enter V: "))
        print("\nusing the formula I = P / U")
        print("\nA = ")
        print(W / V)
        end()
    if known == 3:
        V = float(input("Enter V: "))
        R = float(input("Enter R: "))
        print("\nusing the formula I = U / Ohm")
        print("\nA = ")
        print(V / R)
        end()


def find_r():
    print("please choose a set of known variables:\n")
    print("1: V and A")
    print("2: V and W")
    print("3: W and A")
    known = float(input("\n\n:> "))
    if known == 1:
        V = float(input("Enter V: "))
        A = float(input("Enter A: "))
        print("\nusing the formula Ohm = U / I")
        print("\nR = ")
        print(V / A)
        end()
    if known == 2:
        A = float(input("Enter A: "))
        W = float(input("Enter W: "))
        print("\nusing the formula Ohm = U^2 / P")
        print("\nR = ")
        print(W ** 2 / A)
        end()
    if known == 3:
        W = float(input("Enter W: "))
        A = float(input("Enter A: "))
        print("\nusing the formula Ohm = P / I^2")
        print("\nR = ")
        print(W / A ** 2)
        end()

def end():
    print("\ncontinue...")
    input()
    print("\n\n\n")
    main()


if __name__ == "__main__":
    main()

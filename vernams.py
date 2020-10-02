m = input("Enter your first string:")
k = input("Enter your second string:")
from operator import xor
def XOR_E(m, k):
    print(xor(bool(m), bool(k)))

def c(m, k):
    c1 = input("c1 = ")
    c2 = input("c2 = ")
    xc = xor(bool(c1), bool(c2))
    print(xc)
    m1 = input("m1 = ")
    m2 = input("m2 = ")
    xm = xor(xor(bool(m1), bool(k)), xor(bool(m2), bool(k)))
    print(xm)
    mx = xor(bool(m1), bool(m2))
    if xm == mx:
        print("so key can be used only once.")
    else:
        print("Umm?")

if __name__ == '__main__':
    XOR_E(m, k)
    c(m, k)

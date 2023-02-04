import inflect
p = inflect.engine()
myl = []
while True:
    try:
        nome = input("Name: ")
        myl.append(nome)
    except EOFError:
        print()
        break

conj = p.join(myl)
print("Adieu, adieu, to " + conj)
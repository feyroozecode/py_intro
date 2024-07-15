def est_premier(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for nombre in range(1, 101):
    if est_premier(nombre):
        print(nombre, "est un nombre premier")

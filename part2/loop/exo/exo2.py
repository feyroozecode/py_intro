def suite_fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

# Générer la suite de Fibonacci jusqu'à 1000
suite_fibonacci(1000)

def is_prime(n):
    """Проверяет, является ли число простым."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

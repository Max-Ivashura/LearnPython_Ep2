from is_prime import is_prime

def test_prime_numbers():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True

def test_non_prime_numbers():
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(6) == False
    assert is_prime(8) == False
    assert is_prime(9) == False

def test_negative_numbers_and_zero():
    assert is_prime(-1) == False
    assert is_prime(0) == False
    assert is_prime(-10) == False

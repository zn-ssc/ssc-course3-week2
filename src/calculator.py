def multiply_positive_numbers(a, b):
    """Multiplies two numbers but only if both are positive integers."""
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("Boolean values are not allowed")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")

    if a <= 0 or b <= 0:
        raise ValueError("Both numbers must be positive")

    return a * b

"""Simple module for Fibonacci calculation."""


def fib(n: int) -> int:
    """Return the nth Fibonacci number using recursion.

    Args:
        n: Index of the Fibonacci sequence (0-based).

    Returns:
        The nth Fibonacci number.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    # simple demonstration
    for i in range(10):
        print(f"fib({i}) = {fib(i)}")

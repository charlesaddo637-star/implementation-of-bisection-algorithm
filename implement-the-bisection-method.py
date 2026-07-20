** start of main.py **

def square_root_bisection(number, tolerance=1e-7, max_iterations=100):
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")

    if number == 0:
        print("The square root of 0 is 0")
        return 0
    if number == 1:
        print("The square root of 1 is 1")
        return 1

    low, high = 0, max(1, number)
    iterations = 0

    while iterations < max_iterations:
        mid = (low + high) / 2
        square = mid * mid

        # ✅ Refined convergence: check interval width directly
        if (high - low) <= tolerance:
            print(f"The square root of {number} is approximately {mid}")
            return mid

        if square < number:
            low = mid
        else:
            high = mid

        iterations += 1

    print(f"Failed to converge within {max_iterations} iterations")
    return None


** end of main.py **


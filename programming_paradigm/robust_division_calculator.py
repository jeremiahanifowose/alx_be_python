# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Perform division safely, handling invalid inputs and division by zero."""
    try:
        numerator = float(numerator)
        denominator = float(denominator)

        if denominator == 0:
            return "Error: Cannot divide by zero."

        result = numerator / denominator
        return f"The result of the division is {result}"

    except ValueError:
        return "Error: Please enter numeric values only."

# main.py
from robust_division_calculator import safe_divide

def main():
    print("=== Robust Division Calculator ===")
    while True:
        numerator = input("Enter numerator (or 'q' to quit): ").strip()
        if numerator.lower() == 'q':
            print("Goodbye!")
            break

        denominator = input("Enter denominator: ").strip()

        result = safe_divide(numerator, denominator)
        print(result)
        print()  # blank line for readability


if __name__ == "__main__":
    main()

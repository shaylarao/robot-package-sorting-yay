import math

def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    Determines the correct stack for a package based on its volume and mass,
    according to Thoughtful's robotic automation rules.

    Args:
        width: The package width in centimeters (cm).
        height: The package height in centimeters (cm).
        length: The package length in centimeters (cm).
        mass: The package mass in kilograms (kg).

    Returns:
        A string indicating the destination stack: "STANDARD", "SPECIAL", or "REJECTED".
    """
    # 1. Calculate Volume
    volume = width * height * length

    # 2. Determine Bulky Status
    # A package is 'bulky' if:
    # a) Volume >= 1,000,000 cm³ OR
    # b) Any dimension >= 150 cm
    is_bulky = (
        volume >= 1_000_000 or
        width >= 150 or
        height >= 150 or
        length >= 150
    )

    # 3. Determine Heavy Status
    # A package is 'heavy' when its mass is >= 20 kg.
    is_heavy = mass >= 20

    # 4. Dispatch Logic (Uses a ternary operator as requested for LLM implementation)
    # Rules:
    # - REJECTED: Both heavy AND bulky
    # - STANDARD: Neither heavy NOR bulky
    # - SPECIAL: Either heavy OR bulky (but not both)

    if is_bulky and is_heavy:
        stack = "REJECTED"
    else:
        # If it is either bulky OR heavy (but not both), it is SPECIAL. Otherwise, it is STANDARD.
        stack = "SPECIAL" if (is_bulky or is_heavy) else "STANDARD"

    return stack

# --- User Input Handler ---

def get_input_value(prompt: str) -> float:
    """Helper function to safely get and validate numerical input from the user."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Input must be a positive number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def main():
    """Handles user input and runs the sorting logic."""
    print("--- Thoughtful Package Dispatch Simulator ---")

    # Get dimensions and mass from the user
    width = get_input_value("Enter package width (cm): ")
    height = get_input_value("Enter package height (cm): ")
    length = get_input_value("Enter package length (cm): ")
    mass = get_input_value("Enter package mass (kg): ")

    # Calculate and display the result
    destination = sort(width, height, length, mass)
    print(f"\nPackage Details: {width}x{height}x{length} cm, {mass} kg")
    print(f"Destination Stack: {destination}")

# --- Test Coverage ---

def run_tests():
    """Runs a series of tests to validate the sorting logic."""
    print("\n--- Running Unit Tests for Sorting Logic ---")

    test_cases = [
        # Case 1: Standard (Not bulky, not heavy)
        (10, 10, 10, 5, "STANDARD", "Small, light package"),
        # Case 2: Bulky only (Large volume)
        (100, 100, 100, 5, "SPECIAL", "Volume (1M) is exactly the bulky limit"),
        # Case 3: Bulky only (Large dimension)
        (160, 10, 10, 5, "SPECIAL", "One dimension is over 150 cm"),
        # Case 4: Heavy only
        (10, 10, 10, 25, "SPECIAL", "Mass (25kg) is over 20kg limit"),
        # Case 5: REJECTED (Heavy AND Bulky by volume)
        (100, 100, 100, 30, "REJECTED", "Both heavy and bulky by volume"),
        # Case 6: REJECTED (Heavy AND Bulky by dimension)
        (160, 50, 50, 30, "REJECTED", "Both heavy and bulky by dimension"),
        # Case 7: Edge Case - Exactly the limits
        (100, 100, 100, 20, "REJECTED", "Exactly at both limits (Bulky by Volume, Heavy by Mass)"),
        # Case 8: Just under heavy limit
        (1, 1, 1, 19.9, "STANDARD", "Just under heavy limit (not bulky)"),
        # Case 9: Large volume, slightly under 1M, should still be STANDARD if dimensions allow
        (99, 99, 99, 10, "STANDARD", "Volume just under 1M (970299)"),
        # Case 10: Dimension just under 150, should be STANDARD if volume is low
        (149.9, 1, 1, 10, "STANDARD", "Dimension just under 150 (not bulky/heavy)"),
        # Case 11: Bulky only (Large dimension, small mass)
        (150, 1, 1, 1, "SPECIAL", "Exactly at 150cm dimension limit"),
    ]

    passed_count = 0
    for w, h, l, m, expected, description in test_cases:
        result = sort(w, h, l, m)
        is_passed = result == expected
        print(f"Test: {description} (W:{w}, H:{h}, L:{l}, M:{m}kg)")
        print(f"  -> Result: {result}, Expected: {expected} | {'PASS' if is_passed else 'FAIL'}")
        if is_passed:
            passed_count += 1
    
    print(f"\n--- Test Summary: {passed_count}/{len(test_cases)} tests passed. ---")


# Run the main input handler or the tests
if __name__ == "__main__":
    main()
    run_tests()

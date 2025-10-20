# robot-package-sorting-yay
Robot Package Sorting

This Python solution implements the robotic sorting logic for Thoughtful's factory based on the following criteria:
Sort the packages using the following criteria:
- A package is **bulky** if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or when one of its dimensions is greater or equal to 150 cm.
- A package is **heavy** when its mass is greater or equal to 20 kg.

How To Run:
You need Python 3 installed.

Execution:
1. Save the code as thoughtful_sort_logic.py
2. Run the script from your terminal: python thoughtful_sort_logic.py
3. The program will first prompt you to enter the width, height, length (in cm), and mass (in kg) for the package you wish to test.
4. After the interactive test, the script automatically executes the embedded unit tests for logic validation.




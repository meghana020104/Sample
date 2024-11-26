
print("Enter up to 10 numbers. Type 'done' to stop.")

numbers = []

for i in range(10):
    user_input = input(f"Enter number {i + 1}: ")
    if user_input.lower() == "done":  # Stop if user types 'done'
        break
    try:
        numbers.append(float(user_input))
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if numbers:
    print(f"The maximum number is: {max(numbers)}")
else:
    print("No numbers were entered.")


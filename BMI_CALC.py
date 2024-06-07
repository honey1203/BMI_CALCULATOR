def calculate_bmi(weight, height):
    """Calculate BMI given weight in kg and height in meters."""
    return weight / (height ** 2)

def classify_bmi(bmi):
    """Classify BMI into categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def get_valid_input(prompt, min_value, max_value):
    """Prompt the user for input and validate it."""
    while True:
        try:
            value = float(input(prompt))
            if value < min_value or value > max_value:
                raise ValueError
            return value
        except ValueError:
            print(f"Please enter a valid number between {min_value} and {max_value}.")

def main():
    print("Welcome to the BMI Calculator!")
    weight = get_valid_input("Enter your weight in kilograms (e.g., 70): ", 10, 300)
    height = get_valid_input("Enter your height in fit (e.g., 1.75): ", 1.5 , 7.3)
    
    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)
    
    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"Your BMI category is: {category}")

if __name__ == "__main__":
    main()


def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight 🟡 (Time to eat some healthy carbs!)"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight 🟢 (Great job! Maintain your lifestyle.)"
    elif 25 <= bmi < 29.9:
        return "Overweight 🟡 (Consider a bit more physical activity.)"
    else:
        return "Obese 🔴 (Please consult a health professional for advice.)"

def main():
    print("=" * 45)
    print("      Oasis Infobyte - Python Task 2     ")
    print("             BMI Calculator              ")
    print("=" * 45)

    while True:
        try:
            weight = float(input("Enter your weight in Kilograms (kg): "))
            if weight <= 0:
                print("Weight must be greater than zero.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    while True:
        try:
            height = float(input("Enter your height in Meters (m) (e.g., 1.75): "))
            if height <= 0:
                print("Height must be greater than zero.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print("\n" + "-" * 45)
    print(f"Your BMI Score is: {bmi:.2f}")
    print(f"Category: {category}")
    print("-" * 45)

if __name__ == "__main__":
    main()
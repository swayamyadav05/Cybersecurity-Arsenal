from src.password_checker import evaluate_password_strength, generate_feedback


def main():
    # Main function to execute the password checker tool.
    password = input("Enter a password to check its strength: ")
    strength_score, strength_level = evaluate_password_strength(password)
    feedback = generate_feedback(password)

    print(f"Password Strength: {strength_level}")
    if feedback:
        print("Suggestions to improve password strength:")
        print(feedback)


if __name__ == "__main__":
    main()

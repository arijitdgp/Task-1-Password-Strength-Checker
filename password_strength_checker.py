import re
import getpass


def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters (12 or more is preferable).")

    # Character-type checks
    checks = [
        (r"[A-Z]", "Add at least one uppercase letter (A-Z)."),
        (r"[a-z]", "Add at least one lowercase letter (a-z)."),
        (r"[0-9]", "Include at least one number (0-9)."),
        (r"[^A-Za-z0-9]", "Include at least one special character."),
    ]

    for pattern, message in checks:
        if re.search(pattern, password):
            score += 1
        else:
            feedback.append(message)

    # Strength classification
    if score >= 6:
        strength = "Strong"
    elif score >= 4:
        strength = "Moderate"
    else:
        strength = "Weak"

    print("\n========== Password Strength Report ==========")
    print(f"Password Strength: {strength}")
    print(f"Score: {score}/6")

    if feedback:
        print("\nSuggestions to improve your password:")
        for suggestion in feedback:
            print(f"- {suggestion}")
    else:
        print("\nExcellent! Your password meets all the basic checks.")

    print("==============================================")

    return strength


if __name__ == "__main__":
    print("Welcome to Password Strength Checker")
    password = getpass.getpass("Enter your password: ")
    check_password_strength(password)

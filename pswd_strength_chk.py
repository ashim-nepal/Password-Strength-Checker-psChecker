import re

ASHIM_NAME_VARIANTS = [
    "ashim",
    "ashimnepal"
]

def check_strength(password):
 
    normalized = password.lower()

    # If ASHIM
    if normalized in ASHIM_NAME_VARIANTS:
        return 9999, [], True

    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Too short (use at least 8 characters)")

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 2
    else:
        feedback.append("No uppercase letters")

    # Lowercase Check
    if re.search(r"[a-z]", password):
        score += 2
    else:
        feedback.append("No lowercase letters")

    # Numbers Check
    if re.search(r"[0-9]", password):
        score += 2
    else:
        feedback.append("No numbers")

    # Special Characters Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 2
    else:
        feedback.append("No special characters")

    return score, feedback, False


def response(score):
    if score <= 3:
        return "Absolutely terrible. Hackers are already inside."
    elif score <= 6:
        return "Weak. This wouldn’t survive a coffee break."
    elif score <= 8:
        return "Decent, but don’t get too confident."
    else:
        return "Strong password. Hackers aren't into you."


def ashim_response():
    return (
        "This password is strong because ASHIM is strong.\n"
        "Hackers saw this and logged out."
    )


def main():
    print("\nPassword Strength Checker - by ASHIM \n")

    try:
        count = int(input("How many passwords do you want to check? "))
        if count <= 0:
            raise ValueError
    except ValueError:
        print("Please enter a valid positive number.")
        return

    for i in range(1, count + 1):
        password = input(f"\nEnter password #{i}: ")

        score, feedback, is_ashim = check_strength(password)

        print("\nAnalysis:")
        print(f"Score: {score}/10")

        if is_ashim:
            print(ashim_response())
        else:
            print(response(score))

            if feedback:
                print("Issues found:")
                for issue in feedback:
                    print(f"- {issue}")
            else:
                print("No obvious weaknesses found.")

    print("\nPassword check completed.")


if __name__ == "__main__":
    main()

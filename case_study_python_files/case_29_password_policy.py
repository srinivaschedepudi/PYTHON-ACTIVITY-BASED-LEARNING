"""Case 29: Password policy validation engine."""

PASSWORDS = ["Campus123", "short7A", "password9A", "StrongPass8"]
PROHIBITED_WORDS = ["password", "admin"]


def validate_password(password):
    failures = []
    has_upper = False
    has_lower = False
    has_digit = False
    has_repeated_neighbor = False

    if len(password) < 8:
        failures.append("must contain at least 8 characters")
    for index, character in enumerate(password):
        if character.isupper():
            has_upper = True
        if character.islower():
            has_lower = True
        if character.isdigit():
            has_digit = True
        if index > 0 and character == password[index - 1]:
            has_repeated_neighbor = True
    if not has_upper:
        failures.append("must include an uppercase letter")
    if not has_lower:
        failures.append("must include a lowercase letter")
    if not has_digit:
        failures.append("must include a digit")
    if has_repeated_neighbor:
        failures.append("must not contain identical adjacent characters")
    lower_password = password.lower()
    for word in PROHIBITED_WORDS:
        if word in lower_password:
            failures.append(f"must not contain prohibited text '{word}'")

    return failures


def main():
    print("PASSWORD POLICY CHECK")
    for password in PASSWORDS:
        failures = validate_password(password)
        if failures:
            print(f"{password}: INVALID")
            for reason in failures:
                print(f"  - {reason}")
        else:
            print(f"{password}: VALID")


if __name__ == "__main__":
    main()

import re

def validate_password(password):
    errors = []

    if len(password) < 8:
        errors.append("Password must contain at least 8 characters")

    if not re.search(r"[A-Z]", password):
        errors.append("Missing uppercase letter")

    if not re.search(r"[a-z]", password):
        errors.append("Missing lowercase letter")

    if not re.search(r"[0-9]", password):
        errors.append("Missing digit")

    if not re.search(r"[^A-Za-z0-9]", password):
        errors.append("Missing special character")

    if re.search(r"(.)\1{2,}", password):
        errors.append(
            "Three or more consecutive repeated characters found"
        )

    prohibited = ["password", "admin", "1234"]

    for word in prohibited:
        if word in password.lower():
            errors.append(
                f"Contains prohibited substring: {word}"
            )

    return errors

password = input("Enter password: ")

errors = validate_password(password)

print("\n--- Password Validation Report ---")

if not errors:
    print("Password Status: VALID")
    print("All password policy conditions are satisfied.")
else:
    print("Password Status: INVALID")
    print("Failed Conditions:")

    for error in errors:
        print("-", error)


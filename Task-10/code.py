
import re

def validate_email(email):
    errors = []

    if email.count("@") == 0:
        errors.append("Missing @ symbol")
        return errors

    if email.count("@") > 1:
        errors.append("Multiple @ symbols found")
        return errors

    username, domain_part = email.split("@")

    if not username:
        errors.append("Missing username")
    elif username.startswith(".") or username.endswith("."):
        errors.append("Invalid username separator")
    elif ".." in username:
        errors.append("Consecutive dots in username")
    elif not re.fullmatch(r"[A-Za-z0-9_.]+", username):
        errors.append("Invalid characters in username")

    if not domain_part:
        errors.append("Missing domain")
        return errors

    if "." not in domain_part:
        errors.append("Missing domain extension")
        return errors

    domain, extension = domain_part.rsplit(".", 1)

    if not domain:
        errors.append("Missing domain name")
    elif domain.startswith("-") or domain.endswith("-"):
        errors.append("Invalid domain separator")
    elif not re.fullmatch(r"[A-Za-z0-9-]+", domain):
        errors.append("Invalid characters in domain")

    if not extension:
        errors.append("Missing extension")
    elif not re.fullmatch(r"[A-Za-z]{2,6}", extension):
        errors.append("Invalid extension format")

    return errors


def validate_registration(reg_id):
    pattern = r"[A-Z]{3}[0-9]{4}[0-9]{3}"

    if not reg_id:
        return ["Registration ID is missing"]

    if len(reg_id) != 10:
        return ["Registration ID must contain 10 characters"]

    if not re.fullmatch(pattern, reg_id):
        return ["Invalid registration ID format"]

    return []


email = input("Enter student email: ").strip()
reg_id = input("Enter registration ID: ").strip()

email_errors = validate_email(email)
reg_errors = validate_registration(reg_id)

print("\n--- Validation Results ---")

if email_errors:
    print("Email: INVALID")
    for error in email_errors:
        print("-", error)
else:
    print("Email: VALID")

if reg_errors:
    print("Registration ID: INVALID")
    for error in reg_errors:
        print("-", error)
else:
    print("Registration ID: VALID")


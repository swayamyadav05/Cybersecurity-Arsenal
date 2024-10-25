import re


def check_length(password):
    """Check if password meets the minimum length requirement (at least 8 characters)."""
    return len(password) >= 8


def check_uppercase(password):
    """Check if password contains at least one uppercase letter."""
    return bool(re.search(r"[A-Z]", password))


def check_lowercase(password):
    """Check if password contains at least one lowercase letter."""
    return bool(re.search(r"[a-z]", password))


def check_digit(password):
    """Check if password contains at least one digit."""
    return bool(re.search(r"\d", password))


def check_special_char(password):
    """Check if password contains at least one special character."""
    return bool(re.search(r"[!@#$%^&*()_\-+={}\[\]:;<>,.?~`]", password))


def evaluate_password_strength(password):
    """
    Evaluate the password strength based on several criteria.

    Args:
        password (str): Password string to be evaluated.

    Returns:
        tuple: (strength_score, strength_level) where strength_score is an integer
               representing criteria met, and strength_level is a descriptive string.
    """
    criteria_met = sum(
        [
            check_length(password),
            check_uppercase(password),
            check_lowercase(password),
            check_digit(password),
            check_special_char(password),
        ]
    )

    strength_levels = {
        5: "Very Strong",
        4: "Strong",
        3: "Moderate",
        2: "Weak",
        1: "Very Weak",
    }

    return criteria_met, strength_levels.get(criteria_met, "Very Weak")


def generate_feedback(password):
    """
    Generate feedback based on missing criteria to improve password strength.

    Args:
        password (str): Password string to evaluate for feedback.

    Returns:
        str: Feedback string with suggestions to improve password strength.
    """
    feedback = []
    if not check_length(password):
        feedback.append("Increase the length to at least 8 characters.")
    if not check_uppercase(password):
        feedback.append("Add at least one uppercase letter.")
    if not check_lowercase(password):
        feedback.append("Add at least one lowercase letter.")
    if not check_digit(password):
        feedback.append("Include at least one number.")
    if not check_special_char(password):
        feedback.append("Use at least one special character (e.g., !@#$%^&*()).")

    return " ".join(feedback) if feedback else "No improvements needed."

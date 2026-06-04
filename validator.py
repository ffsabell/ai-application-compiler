def validate_schema(config):

    errors = []

    required_sections = [
        "intent",
        "architecture",
        "database",
        "api",
        "ui",
        "auth"
    ]

    for section in required_sections:

        if section not in config:
            errors.append(
                f"{section} missing"
            )

    return errors
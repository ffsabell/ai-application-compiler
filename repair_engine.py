def repair_schema(config, errors):

    repairs = []

    if "auth missing" in errors:

        config["auth"] = {
            "roles": {
                "Admin": {
                    "permissions": ["all"]
                }
            }
        }

        repairs.append(
            "Default auth created"
        )

    return config, repairs
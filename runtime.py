def simulate_runtime(config):

    status = True

    required = [
        "database",
        "api",
        "ui",
        "auth"
    ]

    for item in required:

        if item not in config:
            status = False

    return {
        "status":
            "SUCCESS"
            if status
            else
            "FAILED"
    }
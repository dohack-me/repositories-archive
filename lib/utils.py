def clean(value):
    value = "".join(char.lower() for char in value if char.isalnum() or char in ["-", "_"])
    return value


def get_image_name(repository: str, category: str, challenge: str):
    return f"{clean(repository)}/{clean(category)}/{clean(challenge)}"


def print_line():
    print("-----------------------------------------------------------------------------------------------------------")

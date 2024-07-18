# Functions with Outputs


def format_name(first, last):
    """Take a first and last name to format it a capitalized version of a name."""
    return f"{first.title()} {last.title()}"


formatted_name = format_name("mIKe", "joHnSoN")
print(formatted_name)

import datetime
import platform

with open("README.md", "wt") as f:
    print("# Linus\n", file=f)
    print("That's me.\n", file=f)
    print("## Meta info\n", file=f)
    print(f"Python version: {platform.python_version()}\n", file=f)
    print(f"Date: {datetime.datetime.now()}", file=f)

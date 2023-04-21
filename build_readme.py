import datetime
import platform
import github

# fetch latest commit message
try:
    client = github.Github()
    user = client.get_user("linnnus")
    user_events = user.get_events()
    first_push = next(filter(lambda e: e.type == "PushEvent" and e.payload["commits"], user_events))
    first_commit_msg = first_push.payload["commits"][0]["message"]
except Exception as e:
    print("HALÅÅÅÅ:", repr(e))
    first_commit_msg = "<not found>"

# fetch info for meta section
computer = platform.uname().node
python_version = platform.python_version()
build_time = datetime.datetime.now()

content = f"""# linnnus

i am linus. that's me.

my latest commit is

```
{first_commit_msg}
```

## Meta

This README was automatically generated on `{computer}` using Python
`{python_version}` at `{build_time}`.
"""

with open("README.md", "wt") as f:
    f.write(content)

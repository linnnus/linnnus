# linnnus

i am linus. that's me.

my latest commit is

```
launchd+targets/darwin: Escape XML in plists

This patch updates all usage of toPlist such that it escapes any strings
in the final output.

The motication for this change is to avoid confusion when end-users of
home-manager's APIs are not aware that the option values they set end up
being passed un-escaped to XML files.

BREAKING CHANGE: Consumers doing manual escaping will now be doubly escaped.
```

## Meta

This README was automatically generated on `pkrvm0wrmc9nc7o` using Python
`3.10.18` at `2025-08-15 05:41:43.228534`.

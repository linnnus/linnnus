# linnnus

i am linus. that's me.

my latest commit is

```
lib.generators.toPlist: escape XML syntax in strings & keys

Before this patch, code like this would break generate invalid XML:

    lib.generators.toPlist {} "ab<cd"

That's obviously bad, since the call to toPlist often happens through
indirection, as is the case in e.g. the nix-darwin project. A user might
not realize that they have to escape the strings.

This patch adds the argument 'escape' to lib.generators.plist and emits
a warning if it is not set to true. In a future release, this behavior
should become the default.

I have also added a note for future maintainers, in case I forget to
actually remove the deprecated functionality in a future release.
```

## Meta

This README was automatically generated on `fv-az732-114` using Python
`3.10.15` at `2024-12-24 05:36:17.436863`.

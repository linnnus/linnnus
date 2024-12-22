# linnnus

i am linus. that's me.

my latest commit is

```
Don't use multiple shebang arguments without /usr/bin/env -S in examples

Another platform difference: Linux passes all arguments after the
interpreter in the shebang as a single string argument, while Darwin
passes them as separate arguments.

Normally, /usr/bin/env -S is used to work around this, but in this case
it's easier to just remove the superfluous flag. I don't think -lm is
actually necessary.
```

## Meta

This README was automatically generated on `fv-az837-43` using Python
`3.10.15` at `2024-12-22 05:34:25.923991`.

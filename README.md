# linnnus

i am linus. that's me.

my latest commit is

```
Fix relative includes with -I

Since we're passing the source file to CC over stdin, #include paths are
resolved relative to CWD rather the location of the source file.

This is pretty unintuitive, so to mitigate it, this patch adds the
directory of the source file to the include path with -I.

I also use i++ pattern to avoid fucking up.
```

## Meta

This README was automatically generated on `fv-az1456-311` using Python
`3.10.15` at `2024-11-23 05:37:44.443513`.

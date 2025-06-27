# linnnus

i am linus. that's me.

my latest commit is

```
libutil: Add custom PeekSort implementation

Unlike std::sort and std::stable_sort, this implementation
does not lead to out-of-bounds memory reads or other undefined
behavior when the predicate is not strict weak ordering.

This makes it possible to use this function in libexpr for
builtins.sort, where an incorrectly implemented comparator
in the user nix code currently can crash and burn the evaluator
by invoking C++ UB.
```

## Meta

This README was automatically generated on `pkrvmdyo8zrnvmk` using Python
`3.10.18` at `2025-06-27 05:42:19.958614`.

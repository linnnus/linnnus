# linnnus

i am linus. that's me.

my latest commit is

```
Fix deep overrides

An override like

  inputs.foo.inputs.bar.inputs.nixpkgs.follows = "nixpkgs";

implicitly set `inputs.foo.inputs.bar` to `flake:bar`, which led to an
unexpected error like

  error: cannot find flake 'flake:bar' in the flake registries

We now no longer create a parent override (like for `foo.bar` in the
example above) if it doesn't set an explicit ref or follows
attribute. We only recursively apply its child overrides.

Fixes https://github.com/NixOS/nix/issues/8325, https://github.com/DeterminateSystems/nix-src/issues/95, https://github.com/NixOS/nix/issues/12083, https://github.com/NixOS/nix/issues/5790.
```

## Meta

This README was automatically generated on `pkrvm4h0tjkhlvh` using Python
`3.10.18` at `2025-07-13 05:42:01.029143`.

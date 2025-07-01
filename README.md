# linnnus

i am linus. that's me.

my latest commit is

```
feat(nix)!: Add overlays to flake

This patch adds overlays for easier consumption by downstream flakes. It
now exports an `overlays` attribute, and the `packages` output is
derived from this.

In this process I also removed flake-utils as it was getting in the way.
Doing overlays using flake-utils requires som ugly merging, and it's
like 4 lines to get the subset of behavior I was using from that whole
ass dependency.

BREAKING CHANGE: Plugin is moved to `vimPlugins.dark-notify`.
BREAKING CHANGE: The `apps` output has been removed.
```

## Meta

This README was automatically generated on `pkrvmdyo8zrnvmk` using Python
`3.10.18` at `2025-07-01 05:43:28.758157`.

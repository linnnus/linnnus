# linnnus

i am linus. that's me.

my latest commit is

```
Use unstable nixpkgs if available

I didn't realize this in e1c7ef8 but since we now *only* export
a NixOS module there's no need for the 'nixpkgs' and 'flake-utils'
inputs. This also presents a bit of a challenge, since the code requires
a pretty recent version of Deno, one which is only found in the unstable
branch. Since my main NixOS config is based on nixpkgs stable, that's a
problem.

To work around this I just check if my custom NixOS unstable overlay is
available. That's a horrible hack but I don't know how I'd do it
otherwise. Perhaps we ought to add an assertion about the minimum
version of Deno, since the error message is quite obscure (type-checking
fails).
```

## Meta

This README was automatically generated on `fv-az801-135` using Python
`3.10.13` at `2023-12-31 05:32:00.778352`.

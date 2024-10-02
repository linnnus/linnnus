# linnnus

i am linus. that's me.

my latest commit is

```
Fix lazy socket initialization

Okay so the whole point of socket initialization is that we don't have
to start up the service until someone actually interacts with the
socket.

This was broken becuase we added a Wants= dependency between
multi-user.taget and push-notification-api.service, causing the serice
to be started on boot.

On systemd dependencies: https://www.freedesktop.org/software/systemd/man/latest/systemd.unit.html#Wants=
On socket initialization: https://0pointer.de/blog/projects/socket-activation.html
```

## Meta

This README was automatically generated on `fv-az849-341` using Python
`3.10.15` at `2024-10-02 05:37:11.101694`.

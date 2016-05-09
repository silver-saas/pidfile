# Pidfile

TODO: fill in build status and coverage images

A module for interacting with pidfiles.

A common pattern when writing server software is to write a pidfile at system startup.
This is just a file containing the PID of the server process. It can be used by monitoring
tools as well as in aiding debugging.

The standard usage is:

```python
import pidfile
...
pidfile.write_pidfile('server.pid') # Somewhere during initialization
```

The single function will write the PID of the current process to 'server.pid' and will take care
of removing the file at server shutdown (assuming a decent shutdown procedure, but otherwise the
process is hands-off).

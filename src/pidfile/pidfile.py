"""Functions for interacting with a pidfile."""

import atexit
import os


def write_pidfile(pidfile_path):
    """Write a pidfile for the current process.

    Will also remove the pidfile at process exit-time.

    Args:
      pidfile_path: the path where the PID should be written.

    Returns:
      Nothing

    Throws:
      IOError: if the pidfile could not be written.
    """

    pidfile = open(pidfile_path, 'w')
    pidfile.write(str(os.getpid()))
    pidfile.close()
    atexit.register(_remove_pidfile, pidfile_path)


def _remove_pidfile(pidfile_path):
    try:
        os.remove(pidfile_path)
    except Exception as e:
        pass

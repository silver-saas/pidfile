import os
import shutil
import subprocess
import tempfile
import unittest

import pidfile


class PidfileTest(unittest.TestCase):
    def test_pidfile_contains_pid(self):
        """The written pidfile actually contains the current process' pid."""

        tmp_dir = tempfile.mkdtemp()

        try:
            pid_path = os.path.join(tmp_dir, 'pid.pid')
            pidfile.write_pidfile(pid_path)

            with open(pid_path) as pid_file:
                pid = int(pid_file.read())
                self.assertEqual(pid, os.getpid())
        finally:
            shutil.rmtree(tmp_dir)

    def test_remove_pidfile(self):
        """The pidfile is removed after the process exists."""

        tmp_dir = tempfile.mkdtemp()

        try:
            pid_path = os.path.join(tmp_dir, 'pid.pid')

            with open(pid_path, 'w') as pid_file:
                pid_file.write('123')

            # Import the actual module, cause _remove_pidfile is not otherwise visible through
            # regular import, on account of it not being in __all__.
            import pidfile.pidfile as pidfile_x

            self.assertTrue(os.path.exists(pid_path))
            pidfile_x._remove_pidfile(pid_path)
            self.assertFalse(os.path.exists(pid_path))
        finally:
            shutil.rmtree(tmp_dir)

    def test_remove_pidfile_with_failure(self):
        """The pidfile is removed after the process exists, even when it fails."""

        tmp_dir = tempfile.mkdtemp()

        try:
            pid_path = os.path.join(tmp_dir, 'pid.pid')
            
            # Import the actual module, cause _remove_pidfile is not otherwise visible through
            # regular import, on account of it not being in __all__.
            import pidfile.pidfile as pidfile_x

            self.assertFalse(os.path.exists(pid_path))
            pidfile_x._remove_pidfile(pid_path) # Nothing else should happen.
            self.assertFalse(os.path.exists(pid_path))
        finally:
            shutil.rmtree(tmp_dir)

class PidfileIntegrationTest(unittest.TestCase):
    def test_clears_pidfile_at_shutdown(self):
        """Integration tests of a program using the pidfile module."""

        tmp_dir = tempfile.mkdtemp()

        try:
            pid_path = os.path.join(tmp_dir, 'pid.pid')
            self.assertFalse(os.path.exists(pid_path))
            test_program = 'import pidfile; pidfile.write_pidfile(\'{0}\')'.format(pid_path)
            subprocess.check_call(['python', '-c', test_program])
            self.assertFalse(os.path.exists(pid_path))
        finally:
            shutil.rmtree(tmp_dir)


if __name__ == '__main__':
    unittest.main()

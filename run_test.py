# from __future__ import print_function
# can't be used sicne https://github.com/conda/conda-build/issues/643

from contextlib import contextmanager
import ast
import glob
import os
import subprocess
import sys
import traceback

import six

try:
    raw_input
except NameError:
    raw_input = input

try:
    import auto
except ImportError:
    sys.path.insert(0, os.path.join(os.environ['AUTO_DIR'], 'python'))
    import auto

class NonExistingError(Exception):
    pass

try:
    from Tkinter import TclError
except ImportError:
    try:
        from tkinter import TclError
    except ImportError:
        TclError = NonExistingError

PYTHON_DEMO = os.path.join(os.environ['AUTO_DIR'], 'demos', 'python')


@contextmanager
def nowait():
    """
    Replace stdin to emulate a user hitting RET all the time.
    """
    true_stdin = sys.stdin
    proc = subprocess.Popen(['yes'], stdout=subprocess.PIPE)
    try:
        sys.stdin = proc.stdout
        yield
    finally:
        sys.stdin = true_stdin

        proc.stdout.close()
        proc.terminate()


def execdemo(__code):
    six.exec_(__code, vars(auto), {})


def rundemo(name):
    path = os.path.join(PYTHON_DEMO, name)
    with open(path, 'rt') as file:
        code = file.read()
    try:
        ast.parse(code)
    except SyntaxError:
        traceback.print_exc(1)
        six.print_('Skip', name)
        return
    execdemo(code)


def test_smoke():
    with nowait():
        for name in glob.glob(os.path.join(PYTHON_DEMO, 'demo*.auto')):
            six.print_()
            six.print_('Run:', name)
            try:
                rundemo(name)
            except TclError:
                # Assuming that it is thrown in plot at the end of demo.
                traceback.print_exc()
                print('Ignoring...')


if __name__ == '__main__':
    test_smoke()
    print('****** SUCCESS ******')

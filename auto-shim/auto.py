import os
import sys


def _guess_conda_prefix():
    try:
        return os.environ['CONDA_PREFIX']
    except KeyError:
        # Assume:
        # this_file = ${CONDA_PREFIX}/lib/python2.7/site-packages/auto.py'
        this_file = os.path.abspath(__file__)

        CONDA_PREFIX = this_file
        for _ in range(4):
            CONDA_PREFIX = os.path.dirname(CONDA_PREFIX)
    return CONDA_PREFIX


def _guess_auto_dir():
    try:
        return os.environ['AUTO_DIR']
    except KeyError:
        pass

    CONDA_PREFIX = _guess_conda_prefix()
    return os.path.join(CONDA_PREFIX, 'opt', 'auto', '07p')


def _guess_auto_python_dir():
    return os.path.join(_guess_auto_dir(), 'python')


try:
    import AUTOclui
except ImportError:
    sys.path.insert(0, _guess_auto_python_dir())
    import AUTOclui
del AUTOclui


from AUTOclui import *

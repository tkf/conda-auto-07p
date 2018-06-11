import os
import sys


def _conda_prefix_candidates():
    try:
        yield os.environ['CONDA_PREFIX']
    except KeyError:
        pass

    # Assume:
    # this_file = ${CONDA_PREFIX}/lib/python2.7/site-packages/auto.py'
    this_file = os.path.abspath(__file__)

    CONDA_PREFIX = this_file
    for _ in range(4):
        CONDA_PREFIX = os.path.dirname(CONDA_PREFIX)
    yield CONDA_PREFIX

    # Assume:
    # sys.executable = ${CONDA_PREFIX}/bin/python
    yield os.path.dirname(os.path.dirname(sys.executable))


def _guess_auto_dir():
    try:
        return os.environ['AUTO_DIR']
    except KeyError:
        pass

    for CONDA_PREFIX in _conda_prefix_candidates():
        # See: [[../build.sh::/opt/auto/07p]]
        AUTO_DIR = os.path.join(CONDA_PREFIX, 'opt', 'auto', '07p')
        if os.path.exists(AUTO_DIR):
            return AUTO_DIR

    raise RuntimeError('Cannot determine $AUTO_DIR')


def _guess_auto_python_dir():
    return os.path.join(_guess_auto_dir(), 'python')


try:
    import AUTOclui
except ImportError:
    sys.path.insert(0, _guess_auto_python_dir())
    import AUTOclui
del AUTOclui


from AUTOclui import *

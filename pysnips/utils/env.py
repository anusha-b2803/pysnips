# pysnips/utils/env.py

import sys

def is_notebook() -> bool:
    """
    Detects if the code is running in a Jupyter/IPython environment.
    """
    try:
        from IPython import get_ipython
        if 'IPKernelApp' in sys.modules:
            return True
        if get_ipython() is not None:
            return True
    except ImportError:
        pass
    return False

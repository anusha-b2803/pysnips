from .generator import TemplateEngine
from .registry import SNIPPETS

__version__ = "0.1.3"

def get(command: str, **placeholders):
    """
    Retrieves and renders a code snippet.
    """
    return TemplateEngine.render(command, **placeholders)

def list_snippets():
    """
    Returns a dictionary of all available snippets.
    """
    return {cmd: info["description"] for cmd, info in SNIPPETS.items()}

def load_ipython_extension(ip):
    """
    Hook for IPython's %load_ext pysnips
    """
    from .ipython_ext import load_ipython_extension as load
    load(ip)

def enable_magic():
    """
    Manually enables pysnips magic in the current IPython session.
    """
    try:
        from IPython import get_ipython
        ip = get_ipython()
        if ip:
            load_ipython_extension(ip)
            print("pysnips magic enabled!")
        else:
            print("Not in an IPython environment.")
    except ImportError:
        print("IPython not found.")

__all__ = ["get", "list_snippets", "enable_magic", "__version__"]

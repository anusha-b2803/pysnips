# pysnips/utils/export.py

import re
import json
import os
import platform
from ..registry import SNIPPETS

def to_vscode_snippets():
    """
    Converts all snippets to VS Code JSON format.
    """
    vscode_snippets = {}
    
    for cmd, info in SNIPPETS.items():
        template = info["template"]
        description = info["description"]
        
        # Find all unique placeholders
        # Use a regex that handles optional spaces: {{ name }} or {{name}}
        placeholders = re.findall(r"{{\s*(.*?)\s*}}", template)
        unique_phs = []
        for ph in placeholders:
            if ph not in unique_phs:
                unique_phs.append(ph)
        
        vscode_body = template
        for i, ph in enumerate(unique_phs, 1):
            # Replace {{ph}} and {{ ph }} with ${i:ph}
            pattern = rf"{{{{\s*{re.escape(ph)}\s*}}}}"
            vscode_body = re.sub(pattern, f"${{{i}:{ph}}}", vscode_body)

        scope = "python"

        vscode_snippets[f"pysnips-{cmd}"] = {
            "prefix": cmd,
            "body": vscode_body.splitlines(),
            "description": description,
            "scope": scope
        }
        
    return vscode_snippets

def get_vscode_path():
    """
    Returns the path to VS Code user snippets directory.
    """
    if platform.system() == "Windows":
        path = os.path.expandvars(r"%APPDATA%\Code\User\snippets")
    elif platform.system() == "Darwin":
        path = os.path.expanduser("~/Library/Application Support/Code/User/snippets")
    else:
        path = os.path.expanduser("~/.config/Code/User/snippets")
    
    return path

def install_vscode():
    """
    Installs pysnips.code-snippets into VS Code.
    """
    snippets = to_vscode_snippets()
    path = get_vscode_path()
    
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except Exception as e:
            return False, f"Could not create directory {path}: {e}"
            
    file_path = os.path.join(path, "pysnips.code-snippets")
    
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(snippets, f, indent=4)
        return True, file_path
    except Exception as e:
        return False, str(e)

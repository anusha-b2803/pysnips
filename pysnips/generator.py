# pysnips/generator.py

import re
from .registry import SNIPPETS

class TemplateEngine:
    @staticmethod
    def render(command: str, **placeholders) -> str:
        """
        Renders a template by replacing placeholders in the form {{name}}.
        """
        if command not in SNIPPETS:
            raise ValueError(f"Command '{command}' not found in registry.")
        
        template = SNIPPETS[command]["template"]
        
        # Replace placeholders
        rendered = template
        for key, value in placeholders.items():
            pattern = rf"{{{{\s*{key}\s*}}}}"
            rendered = re.sub(pattern, str(value), rendered)
        
        return rendered

    @staticmethod
    def get_placeholders(command: str) -> list:
        """
        Extracts all placeholder names from a template.
        """
        if command not in SNIPPETS:
            return []
        
        template = SNIPPETS[command]["template"]
        return re.findall(r"{{\s*(.*?)\s*}}", template)

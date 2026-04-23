# pysnips/generator.py

import re
from .registry import SNIPPETS
from .utils.env import is_notebook

class Snippet(str):
    """
    A string wrapper that provides rich representation in Jupyter Notebooks.
    """
    def __repr__(self):
        return super().__repr__()

    def _repr_markdown_(self):
        """
        Returns a markdown code block for syntax highlighting in Notebooks.
        """
        return f"```python\n{self}\n```"

    def show(self):
        """
        Explicitly prints or displays the snippet based on environment.
        """
        if is_notebook():
            try:
                from IPython.display import display, Markdown
                display(Markdown(self._repr_markdown_()))
            except ImportError:
                print(self)
        else:
            print(self)

class TemplateEngine:
    @staticmethod
    def render(command: str, **placeholders) -> Snippet:
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
        
        return Snippet(rendered)

    @staticmethod
    def get_placeholders(command: str) -> list:
        """
        Extracts all placeholder names from a template.
        """
        if command not in SNIPPETS:
            return []
        
        template = SNIPPETS[command]["template"]
        return re.findall(r"{{\s*(.*?)\s*}}", template)

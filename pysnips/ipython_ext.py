# pysnips/ipython_ext.py

from .generator import TemplateEngine
from .registry import SNIPPETS

def snippet_transformer(lines):
    """
    IPython input transformer that expands snippet keywords.
    """
    if not lines:
        return lines
    
    # Only transform if it's a single line or starts with a snippet command
    # and doesn't look like valid complex python (to avoid false positives)
    # We strip empty lines to see the real content
    non_empty_lines = [l for l in lines if l.strip()]
    if len(non_empty_lines) != 1:
        return lines
        
    line = non_empty_lines[0].strip()
    parts = line.split()
    if not parts:
        return lines
        
    command = parts[0]
    
    if command in SNIPPETS:
        # Check if all other parts are valid key=value pairs
        placeholders = {}
        is_valid_command = True
        for part in parts[1:]:
            if '=' in part:
                k, v = part.split('=', 1)
                placeholders[k] = v
            else:
                # If there's extra stuff that isn't a placeholder, it's probably real code
                is_valid_command = False
                break
        
        if not is_valid_command:
            return lines

        try:
            rendered = TemplateEngine.render(command, **placeholders)
            # Return the rendered snippet as the new input
            return [l + '\n' for l in rendered.splitlines()]
        except:
            return lines
            
    return lines

def load_ipython_extension(ip):
    """
    Registers the snippet transformer with IPython.
    """
    # Register as a 'cleanup' transformer to run early
    if hasattr(ip, 'input_transformers_post'):
        ip.input_transformers_post.append(snippet_transformer)
    
    # Also add a magic command as a fallback/alternative
    @ip.register_magic_function(magic_kind='line', name='snip')
    def snip_magic(line):
        parts = line.split()
        if not parts:
            print("Usage: %snip <command> [key=value ...]")
            return
        
        cmd = parts[0]
        placeholders = {}
        for part in parts[1:]:
            if '=' in part:
                k, v = part.split('=', 1)
                placeholders[k] = v
        
        try:
            rendered = TemplateEngine.render(cmd, **placeholders)
            # Inject into the next cell
            ip.set_next_input(rendered, replace=False)
        except Exception as e:
            print(f"Error: {e}")

def unload_ipython_extension(ip):
    if hasattr(ip, 'input_transformers_post'):
        if snippet_transformer in ip.input_transformers_post:
            ip.input_transformers_post.remove(snippet_transformer)

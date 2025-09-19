from typing import Dict


def theme(request) -> Dict[str, object]:
    """Inject the active Theme into all templates.

    Safe if migrations aren't applied yet.
    """
    try:
        from .models import Theme  # local import to avoid early import
        t = Theme.get_theme()
    except Exception:
        t = None
    return {"theme": t}


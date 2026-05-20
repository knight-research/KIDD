_context = {}


def set_context(context):
    global _context
    _context = context


def sync_context(target):
    target.update(_context)


def update_context(source, names):
    for name in names:
        if name in source:
            _context[name] = source[name]
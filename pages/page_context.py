_context = {}


def set_context(context):
    global _context
    _context = context


def sync_context(target):
    target.update(_context)
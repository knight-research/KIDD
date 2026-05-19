import importlib


def _public_symbols(module_name):
    module = importlib.import_module(module_name)
    return {
        name: value
        for name, value in vars(module).items()
        if not name.startswith("_")
    }


def load_platform_symbols(sys_win, sys_linux, sys_pi):
    symbols = {}

    if sys_win:
        symbols.update(_public_symbols("import_win"))
    elif sys_linux:
        symbols.update(_public_symbols("import_linux"))
        if sys_pi:
            symbols.update(_public_symbols("import_pi"))

    return symbols
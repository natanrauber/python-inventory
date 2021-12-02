import os


def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')

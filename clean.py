from win32com.shell import shell, shellcon

def empty(confirm=True, show_progress=True, sound=True):
    shell.SHEmptyRecycleBin(None, None, 0)   
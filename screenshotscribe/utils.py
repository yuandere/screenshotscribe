import datetime
import os
import platform
import subprocess


def get_readable_time(ctime):
    readable = datetime.datetime.fromtimestamp(ctime)
    return readable.strftime('%m/%d/%Y %H:%M:%S')


def open_file(path):
    if platform.system() == 'Darwin':
        subprocess.call(('open', path))
    elif platform.system() == 'Windows':
        os.startfile(path)
    else:
        subprocess.call(('xdg-open', path))

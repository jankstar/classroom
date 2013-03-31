#!/usr/bin/env python
import os
import sys
sys.path.append(r'/Applications/eclipse/plugins/org.python.pydev_2.7.0.2013012902/pysrc')
sys.path.append(r'/Users/jan/python/Django-1.4.3/django')

import pydevd
pydevd.patch_django_autoreload(patch_remote_debugger=True, patch_show_console=False)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

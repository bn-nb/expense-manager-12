#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import subprocess
import atexit

# Global variable to store Tmole process
tmole_process = None

def start_tmole():
    global tmole_process
    tmole_process = subprocess.Popen(['./docs/tmole', '8000'])
    # Register the cleanup function to be called on exit
    atexit.register(stop_tmole)


def stop_tmole():
    global tmole_process
    if tmole_process:
        tmole_process.terminate()
        tmole_process.wait()  # Ensure the process has terminated


def main():
    """Run administrative tasks."""

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djp.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    start_tmole()

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

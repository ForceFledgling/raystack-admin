#!/usr/bin/env python
"""Raystack's command-line utility for administrative tasks."""
import os
import sys

# Add parent directory to path to find raystack
parent_dir = os.path.abspath('..')
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Add raystack src to path
raystack_src = os.path.abspath(os.path.join(parent_dir, 'raystack', 'src'))
if raystack_src not in sys.path:
    sys.path.insert(0, raystack_src)


def main():
    """Run administrative tasks."""
    os.environ.setdefault('RAYSTACK_SETTINGS_MODULE', 'config.settings')
    try:
        from raystack.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Raystack. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()



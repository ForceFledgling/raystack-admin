import os
import sys

# Add parent directory to path to find raystack
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Add raystack src to path
raystack_src = os.path.abspath(os.path.join(parent_dir, 'raystack', 'src'))
if raystack_src not in sys.path:
    sys.path.insert(0, raystack_src)

os.environ.setdefault('RAYSTACK_SETTINGS_MODULE', 'config.settings')

from raystack import Raystack

app = Raystack()

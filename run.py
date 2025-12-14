#!/usr/bin/env python
"""Run the raystack-admin application."""
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

os.environ.setdefault('RAYSTACK_SETTINGS_MODULE', 'config.settings')

if __name__ == '__main__':
    import uvicorn
    from core import app
    
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

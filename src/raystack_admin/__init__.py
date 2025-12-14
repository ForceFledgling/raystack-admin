import os
from raystack.compat import APIRouter, RedirectResponse, Request

from .urls import router as urls_router
from .auth import router as auth_router

from raystack.middlewares import PermissionMiddleware


router = APIRouter()

# Add /admin redirect route BEFORE mounting urls_router
# In Starlette, routes are checked in the order they are added to the routes list
# So we need to add this route first, before the Mount("/admin", ...) below
@router.get("/admin")
async def admin_redirect(request: Request):
    """Redirect /admin to /admin/"""
    return RedirectResponse(url="/admin/", status_code=301)

# Mount urls_router with /admin prefix
router.include_router(urls_router, prefix="/admin", tags=["restricted"])

# Include auth router (users, groups, accounts)
router.include_router(auth_router)


def get_template_dir():
    """Возвращает путь к директории с шаблонами админки."""
    return os.path.join(os.path.dirname(__file__), "templates")


# Export auth models and utilities for convenience
from .auth.users.models import UserModel, User, UserCreate
from .auth.groups.models import GroupModel, Group

__all__ = [
    'router',
    'UserModel', 'User', 'UserCreate',
    'GroupModel', 'Group',
    'get_template_dir',
]

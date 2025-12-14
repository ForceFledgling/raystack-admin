"""
Raystack built-in authentication (users, groups, accounts).
"""

from raystack.compat import APIRouter

from raystack_admin.auth.users import api as users_api
from raystack_admin.auth.groups import api as groups_api
from raystack_admin.auth.accounts import urls as accounts_urls
from raystack_admin.auth.accounts import api as accounts_api

# Import models for convenience
from raystack_admin.auth.users.models import UserModel, User, UserCreate
from raystack_admin.auth.groups.models import GroupModel, Group

__all__ = [
    'UserModel', 'User', 'UserCreate',
    'GroupModel', 'Group',
    'router'
]

router = APIRouter()

# Connect user routes
if hasattr(users_api, 'router'):
    router.include_router(users_api.router, prefix="/users", tags=["users"])
# Connect group routes
if hasattr(groups_api, 'router'):
    router.include_router(groups_api.router, prefix="/groups", tags=["groups"])
# Connect account routes (registration, authentication, password change)
if hasattr(accounts_urls, 'router'):
    router.include_router(accounts_urls.router, prefix="/accounts", tags=["accounts"])
# Connect account routes (login/logout)
if hasattr(accounts_api, 'router'):
    router.include_router(accounts_api.router, prefix="/accounts", tags=["accounts"])

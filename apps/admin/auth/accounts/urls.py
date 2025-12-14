import os

from raystack.compat import APIRouter, Request, Depends, HTTPException, status
from raystack.compat import HTMLResponse, RedirectResponse

# from raystack.conf import settings
from raystack.shortcuts import render_template
from apps.admin.auth.users.forms import UserCreateForm, UserUpdateForm
from apps.admin.auth.users.models import UserModel
from apps.admin.auth.groups.models import GroupModel
from apps.admin.auth.accounts.forms import LoginForm
from apps.admin.auth.accounts.utils import hash_password, generate_jwt, check_password
from apps.admin.auth.accounts.utils import get_current_user, get_current_active_user
from apps.admin.auth.accounts.utils import get_current_active_superuser
from apps.admin.auth.accounts.utils import get_current_user_from_token
from apps.admin.auth.accounts.utils import get_current_active_user_from_token
from apps.admin.auth.accounts.utils import get_current_active_superuser_from_token
from apps.admin.auth.accounts.utils import get_current_user_from_cookie
from apps.admin.auth.accounts.utils import get_current_active_user_from_cookie
from apps.admin.auth.accounts.utils import get_current_active_superuser_from_cookie
from apps.admin.auth.accounts.utils import get_current_user_from_header
from apps.admin.auth.accounts.utils import get_current_active_user_from_header
from apps.admin.auth.accounts.utils import get_current_active_superuser_from_header
from apps.admin.auth.accounts.utils import get_current_user_from_query
from apps.admin.auth.accounts.utils import get_current_active_user_from_query
from apps.admin.auth.accounts.utils import get_current_active_superuser_from_query
from apps.admin.auth.accounts.utils import get_current_user_from_body
from apps.admin.auth.accounts.utils import get_current_active_user_from_body
from apps.admin.auth.accounts.utils import get_current_active_superuser_from_body
import jwt
from jwt import PyJWTError as JWTError

from raystack.compat import OAuth2PasswordBearer


router = APIRouter()


def url_for(endpoint, **kwargs):
    """
    Function for generating URL based on endpoint and additional parameters.
    In this case, the endpoint is ignored as we only use the filename.
    """
    if not kwargs:
        return f"/{endpoint}"
    
    path = f"/{endpoint}"
    for key, value in kwargs.items():
        path += f"/{value}"
    
    return path


@router.get("/login", response_model=None)
async def test(request: Request):    
    return render_template(request=request, template_name="accounts/login.html", context={
        "url_for": url_for,
        "parent": "home",
        "segment": "test",
        "config": request.app.settings,
    })

@router.post("/login", response_model=None)
async def login_post(request: Request):
    form = await request.form()
    email = form.get("email")
    password = form.get("password")

    user = await UserModel.objects.filter(email=email).first()

    if user and await check_password(password, user.password_hash):
        # Generate JWT token
        token = generate_jwt(user.id)
        
        response = RedirectResponse(url="/admin/", status_code=303)
        response.set_cookie(key="jwt", value=token, httponly=True) # Secure cookie
        return response
    else:
        return RedirectResponse(url="/accounts/login?error=invalid_credentials", status_code=303)


@router.get("/register", response_model=None)
async def test(request: Request):
    return render_template(request=request, template_name="accounts/register.html", context={
        "url_for": url_for,
        "parent": "home",
        "segment": "test",
        "config": request.app.settings,
    })

@router.get("/password_change", response_model=None)
async def test(request: Request):    
    return render_template(request=request, template_name="accounts/password_change.html", context={
        "url_for": url_for,
        "parent": "/",
        "segment": "test",
        "config": request.app.settings,
    })
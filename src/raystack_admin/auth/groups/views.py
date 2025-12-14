import os
from raystack.compat import APIRouter, Request, Depends, HTTPException, status
from raystack.shortcuts import render_template
from raystack_admin.auth.groups.forms import GroupCreateForm, GroupUpdateForm
from raystack_admin.auth.groups.models import GroupModel
from raystack_admin.auth.users.models import UserModel
import jwt
from jwt import PyJWTError as JWTError
from datetime import timedelta, datetime
# from .utils import hash_password, generate_jwt, check_password

from starlette.responses import JSONResponse, \
    PlainTextResponse, \
    RedirectResponse, \
    StreamingResponse, \
    FileResponse, \
    HTMLResponse

from raystack.compat import OAuth2PasswordBearer

router = APIRouter()

        # Create table when starting application
@router.on_event("startup")
async def create_tables():
    GroupModel.create_table()
    owners_group = await GroupModel.objects.filter(name="Owners").first()  # type: ignore
    if not owners_group:
        GroupModel.objects.create(name="Owners")

        # (Commented examples of models and endpoints left for history)

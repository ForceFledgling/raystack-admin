from raystack.compat import APIRouter

router = APIRouter()

# Import admin router
from apps.admin import router as admin_router

router.include_router(admin_router)



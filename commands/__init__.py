from aiogram import Router

from .admin import router as admin_router
from .admin_panel import router as admin_panel_router
from .basic import router as basic_router
from .start import router as start_router

router = Router()

router.include_routers(start_router, basic_router, admin_router, admin_panel_router)

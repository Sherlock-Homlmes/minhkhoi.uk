from routes import authentication
from routes.system import transactions
from routes.users import clubs, matches, users

from .conf import app

for module in (
    transactions,
    authentication, users,
    clubs, matches
):
    app.include_router(module.router, prefix="/api")

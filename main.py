from fastapi import Depends, FastAPI
from routers import academic_records_router, users_router, visa_details_router, authentication_router, users_router, basic_information_router

from dependencies import get_db
from internal import admin

app = FastAPI(
    title="International Students Tracker",
    description='For managing student data and more',
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Joachim Kuleafenu",
        "email": "kuleafenujoachim@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
    },
)


app.include_router(users_router.router)
app.include_router(academic_records_router.router)
app.include_router(visa_details_router.router)
app.include_router(authentication_router.router)
app.include_router(users_router.router)
app.include_router(basic_information_router.router)

# app.include_router(
#     admin.router,
#     prefix="/admin",
#     tags=["admin"],
#     dependencies=[Depends(get_token_header)],
#     responses={418: {"description": "I'm a teapot"}},
# )


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
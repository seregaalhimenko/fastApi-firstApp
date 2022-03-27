from fastapi import FastAPI
from fastapi.responses import RedirectResponse

# from .models import Base
# from .core.db import engine

from app.routers import questions as ques_router
from app.routers import choices as choices_router
from app.routers import resalt as res_router


# Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(ques_router.router)
app.include_router(choices_router.router)
app.include_router(res_router.router)



@app.get("/", response_class=RedirectResponse)
def index():
    return "/docs/"
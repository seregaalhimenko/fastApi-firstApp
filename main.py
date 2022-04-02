from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.routers import questions as ques_router
from app.routers import choices as choices_router
from app.routers import result as res_router


app = FastAPI(
    version="1"
)

app.include_router(ques_router.router)
app.include_router(choices_router.router)
app.include_router(res_router.router)


@app.get("/", response_class=RedirectResponse)
def index():
    return "/docs/"

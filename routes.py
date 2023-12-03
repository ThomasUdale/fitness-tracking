from fastapi import APIRouter, Request
from jinja2_fragments.fastapi import Jinja2Blocks


templates = Jinja2Blocks(directory="./templates")
router = APIRouter()

@router.get("/")
def index(request: Request):
    return templates.TemplateResponse(
        "main.html", 
        {
            "request": request,
            "page_title":"Main"
        }
    )


@router.get("/clicked")
def button_press(request: Request):
    return templates.TemplateResponse(
        "template_parts/button_clicked.html", 
        {
            "request": request,
        }
    )

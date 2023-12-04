from fastapi import APIRouter, Request
from jinja2_fragments.fastapi import Jinja2Blocks
from db import DatabaseManager
from pydantic import BaseModel

DB_PATH = "fitness.db"

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

@router.get("/get-activities")
def load_activities(request: Request):
    db_manager = DatabaseManager(DB_PATH)
    activities = db_manager.get_activities()
    return templates.TemplateResponse(
        "activities/activity-list.html", 
        {
            "request": request,
            "activities":activities,
        }
    )


@router.post("/add_activity")
async def add_activity(request: Request):
    form = await request.form()

    db_manager = DatabaseManager(DB_PATH)
    db_manager.add_activity(
        form['date'],
        form['sport'],
        form['duration'],
        form['distance'],
        form['avg_power'],
        form['avg_speed'],
        form['avg_hr'],
    )


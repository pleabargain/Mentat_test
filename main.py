from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from uuid import uuid4
import models
import schemas
from database import engine, SessionLocal
models.Base.metadata.create_all(bind=engine)
app = FastAPI()
templates = Jinja2Templates(directory="templates")
@app.post("/submit/", response_model=schemas.UserResponse)
async def submit_form(name: str = Form(...), age: int = Form(...), f: str = Form(...)):
    db = SessionLocal()
    user_id = str(uuid4())
    user_data = models.User(id=user_id, name=name, age=age, favorite_pet=favorite_pet)
    db.add(user_data)
    db.commit()
    db.refresh(user_data)
    db.close()
    return user_data
@app.get("/greet/{user_id}", response_class=HTMLResponse)
async def read_greet(request: Request, user_id: str):
    db = SessionLocal()
    user_data = db.query(models.User).filter(models.User.id == user_+     db.close()
    return templates.TemplateResponse("greeting.html", {"request": request, "name": user_data.name, "age": user_data.age, "favorite_pet": user_data.favorite_pet})
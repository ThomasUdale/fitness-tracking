from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes import router
import subprocess
from contextlib import asynccontextmanager
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Context manager for FastAPI app. It will run all code before `yield`
    on app startup, and will run code after `yeld` on app shutdown.
    """

    try:
        subprocess.run([
            "tailwindcss",
            "-i",
            "./static/src/input.css",
            "-o",
            "./static/css/main.css",
            "--minify"
        ])
    except Exception as e:
        print(f"Error running tailwindcss: {e}")

    yield

app = FastAPI(lifespan=lifespan)

app.include_router(router)
app.mount("/static", StaticFiles(directory="./static"), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000) 

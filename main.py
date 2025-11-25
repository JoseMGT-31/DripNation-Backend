from fastapi import FastAPI
from routes import user, product, support
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Mount images directory to serve uploaded files
images_dir = os.path.join(os.getcwd(), "images")
os.makedirs(images_dir, exist_ok=True)
app.mount("/images", StaticFiles(directory=images_dir), name="images")

app.include_router(user.router)
app.include_router(product.router)
app.include_router(support.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://ec2-44-214-169-188.compute-1.amazonaws.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
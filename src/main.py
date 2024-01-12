from fastapi import FastAPI

from api import customers

app = FastAPI()


app.include_router(customers.router, prefix="/customers", tags=["customers"])

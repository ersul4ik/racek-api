from fastapi import FastAPI

from api.customer.router import router as customer_api
from api.guide.router import router as guide_api


app = FastAPI(title='Racek API')


app.include_router(customer_api)
app.include_router(guide_api)

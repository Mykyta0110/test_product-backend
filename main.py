import uvicorn
from fastapi import FastAPI
from fastapi.routing import APIRouter
import settings
from api.handlers import product_router
from fastapi.middleware.cors import CORSMiddleware


app =  FastAPI(title="products-backend")

main_api_router = APIRouter()

main_api_router.include_router(product_router, prefix="/product", tags=["product"])


app.include_router(main_api_router)

origins = [
    "https://test-product-frontend.onrender.com/"
    
]



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":  
    # run app on the host and port
    uvicorn.run(app, host="0.0.0.0", port=settings.APP_PORT)
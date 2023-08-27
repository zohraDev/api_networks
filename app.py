from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from db.database import SessionLocal
from utils.utils import get_gps_coordinate_from_address, get_response

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api_networks_test/")
async def api_networks(address: str, db: Session = Depends(get_db)):
    if not address:
        raise HTTPException(status_code=404, detail=f"address parameter missing")

    try:
        long, lat = get_gps_coordinate_from_address(address)

    except HTTPException as err:
        raise HTTPException(status_code=err.status_code, detail=f"Http Error: {err.detail}")

    datas = get_response(db, lat, long)
    if not datas and long and lat:
        raise HTTPException(status_code=404, detail=f"There is no network information available at this address: {address}")

    return datas
from sqlalchemy.orm import Session
from . import models

def get_coin(db: Session):
    return db.query(models.coins.open_time, models.coins.close, models.coins.coin).all()

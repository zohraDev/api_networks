from sqlalchemy.orm import Session

from db import models, schemas


def create_operator(db: Session, operator: schemas.Operators):
    db_operator = models.Operators(code=operator.code, name=operator.name)
    db.add(db_operator)
    db.commit()
    db.refresh(db_operator)
    return db_operator


def create_network_offer(db: Session, network_offer: schemas.NetWorkOffers):
    db_network = models.NetWorkOffers(
        code=network_offer.code,
        long=network_offer.long,
        lat=network_offer.lat,
        g2_offer=network_offer.g2_offer,
        g3_offer=network_offer.g3_offer,
        g4_offer=network_offer.g4_offer
    )
    db.add(db_network)
    db.commit()
    db.refresh(db_network)
    db.close()
    return db_network


def get_network_offer_by_coordinate(db: Session, coordinate: dict):

    return db.query(models.NetWorkOffers).filter(
        models.NetWorkOffers.long == coordinate["long"] and models.NetWorkOffers.lat == coordinate["lat"]
    ).all()


def get_operator_by_code(db: Session, code: int):
    return db.query(models.Operators).filter(models.Operators.code == code).all()





from sqlalchemy.orm import Session

from db import models, schemas


def create_operator(db: Session, operator: schemas.Operators):
    """
    This function create a new row in the Operator table
    """
    db_operator = models.Operators(code=operator.code, name=operator.name)
    db.add(db_operator)
    db.commit()
    db.refresh(db_operator)
    return db_operator


def create_network_offer(db: Session, network_offer: schemas.NetWorkOffers):
    """
       This function create a new row in the NetWorkOffers table
    """
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
    """
    This function get the element from the NetWorkOffers table which coordinates are
    matching with those given in the 'coordinate' variable
    :param db: session of the database
    :param coordinate: coordinate (longitude, latitude)
    :return: NetWorkOffers
    """

    return db.query(models.NetWorkOffers).filter(
        models.NetWorkOffers.long == coordinate["long"] and models.NetWorkOffers.lat == coordinate["lat"]
    ).all()


def get_operator_by_code(db: Session, code: int):
    """
    This function get an element from the 'Operators' table
    which operator code is matching with the one given in the 'code' variable
    :param db: session of database
    :param code: code of the operator
    :return: operator
    """
    return db.query(models.Operators).filter(models.Operators.code == code).all()





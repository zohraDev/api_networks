import os
import pathlib
import csv

from db import schemas, models
from db import crud
from db.database import SessionLocal, engine
from utils.utils import lamber93_to_gps

models.Base.metadata.create_all(bind=engine)


def fill_operator_table():
    """
    fill the table operator
    """
    db = SessionLocal()
    data = {"orange": 20801, "SFR": 20810, "Free": 20815, "Bouygue": 20820}

    for name, code in data.items():
        try:
            operator = schemas.Operators(name=name, code=code)
            crud.create_operator(db, operator)
        except Exception as ex:
            print(f"Operator {name} - {code} cannot be process.\n{str(ex)}")
            continue
    print(f"Data loading into the 'operators' is complete")


def fill_network_offers_table():
    """
       fill the table Networkoffers
       """
    db = SessionLocal()
    try:
        with open(f"{os.path.join(pathlib.Path(__file__).parent.resolve(), 'Sites_mobiles.csv')}", 'r') as csvfile:
            # create the object of csv.reader()

            csv_file_reader = csv.reader(csvfile, delimiter=';')
            # skip the header
            next(csv_file_reader, None)
            for line, row in enumerate(csv_file_reader):

                try:
                    long, lat = lamber93_to_gps(row[1], row[2])
                    network_offer = schemas.NetWorkOffers(
                        code=row[0],
                        long=format(long, '.2f'),
                        lat=format(lat, '.2f'),
                        g2_offer=row[3],
                        g3_offer=row[4],
                        g4_offer=row[5]

                    )
                    crud.create_network_offer(db, network_offer)
                except Exception as ex:
                    print(f"Line {line+2} cannot be process.")
                    print(str(ex))
                    continue
    except FileNotFoundError:
        print("File not found. Check the path variable and filename")
        exit()
    print(f"Data loading into the 'networkoffers' is complete")


fill_operator_table()
fill_network_offers_table()

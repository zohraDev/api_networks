from pyproj import Transformer
import requests

from db.crud import get_network_offer_by_coordinate, get_operator_by_code


def lamber93_to_gps(x, y):
    """
    :param x:
    :param y:
    :return:
    """
    # 4326 WGS 84 (GPS)
    # 2154 RGF93 / Lambert-93
    transformer = Transformer.from_crs("EPSG:2154", "EPSG:4326", always_xy=True)
    # long, lat

    return transformer.transform(x, y)


def get_gps_coordinate_from_address(address):
    """
    This function get the coordinate(long, lat) of the given address,
    using API: https://adresse.data.gouv.fr
    for information about the above API, visit :https://adresse.data.gouv.fr/api-doc/adresse
    :param address:
    :return: coordinate (longitude, latitude)
    """

    url = f"https://api-adresse.data.gouv.fr/search/?q={address}"

    res = requests.get(url)
    long, lat = res.json()['features'][0]['geometry']['coordinates']

    return format(long, '.2f'), format(lat, '.2f')


#
def get_response(db, lat, long):
    data = {
        "lat": lat,
        "long": long
    }
    network_offers = get_network_offer_by_coordinate(db, data)
    datas = {}
    for el in network_offers:
        operator = get_operator_by_code(db, el.code)

        datas.update(
            {
                f"{operator[0].name}": {
                    "G2": True if el.g2_offer else False,
                    "G3": True if el.g3_offer else False,
                    "G4": True if el.g4_offer else False,

                }
            }
        )

    return datas

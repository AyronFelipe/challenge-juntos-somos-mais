import collections
from typing import Dict, List

from accounts.models.user import User
from .models import Phone

REGIONS = [
    # SUL
    {"region": "sul", "state": "santa catarina"},
    {"region": "sul", "state": "rio grande do sul"},
    {"region": "sul", "state": "paraná"},
    # SUDESTE
    {"region": "sudeste", "state": "são paulo"},
    {"region": "sudeste", "state": "minas gerais"},
    {"region": "sudeste", "state": "espírito santo"},
    {"region": "sudeste", "state": "rio de janeiro"},
    # NORTE
    {"region": "norte", "state": "acre"},
    {"region": "norte", "state": "rondônia"},
    {"region": "norte", "state": "amazonas"},
    {"region": "norte", "state": "roraima"},
    {"region": "norte", "state": "pará"},
    {"region": "norte", "state": "amapá"},
    {"region": "norte", "state": "tocantins"},
    # CENTRO-OESTE
    {"region": "centro-oeste", "state": "mato grosso"},
    {"region": "centro-oeste", "state": "mato grosso do sul"},
    {"region": "centro-oeste", "state": "goiás"},
    {"region": "centro-oeste", "state": "distrito federal"},
    # NORDESTE
    {"region": "nordeste", "state": "maranhão"},
    {"region": "nordeste", "state": "piauí"},
    {"region": "nordeste", "state": "ceará"},
    {"region": "nordeste", "state": "rio grande do norte"},
    {"region": "nordeste", "state": "paraíba"},
    {"region": "nordeste", "state": "pernambuco"},
    {"region": "nordeste", "state": "alagoas"},
    {"region": "nordeste", "state": "sergipe"},
    {"region": "nordeste", "state": "bahia"},
]


def handle_region(state: str) -> str:

    for item in REGIONS:
        if item.get("state") == state:
            return item.get("region")


def flatten(dictionary, parent_key="", sep="__"):

    items = []
    for key, value in dictionary.items():
        if "gender" in key:
            key = "gender"
        new_key = parent_key + sep + key if parent_key else key
        if isinstance(value, collections.MutableMapping):
            items.extend(flatten(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)


def handle_pagination(
    results: List,
    page_number: int,
    page_size: int,
    type: str = None,
    region: str = None,
) -> Dict:

    start: int = (page_number * page_size) - page_size
    end: int = page_number * page_size

    pagination = slice(start, end)

    items: List[Dict] = []

    for result in results:
        dictionary = flatten(result)
        if type and not region:
            itemType = User.check_type(
                dictionary.get("location__coordinates__latitude"),
                dictionary.get("location__coordinates__longitude"),
            )
            if type == itemType:
                items.append(dictionary)
        elif region and not type:
            itemRegion = handle_region(dictionary.get("location__state"))
            if region == itemRegion:
                items.append(dictionary)
        elif region and type:
            itemType = User.check_type(
                dictionary.get("location__coordinates__latitude"),
                dictionary.get("location__coordinates__longitude"),
            )
            itemRegion = handle_region(dictionary.get("location__state"))
            if region == itemRegion and type == itemType:
                items.append(dictionary)
        else:
            items.append(dictionary)

    users: List[Dict] = handle_info(items[pagination])

    return {
        "pageNumber": page_number,
        "pageSize": page_size,
        "totalCount": len(results),
        "users": users,
    }


def handle_info(items: List[Dict]) -> List[Dict]:
    res: List[Dict] = []
    for item in items:
        res.append(
            {
                "type": User.check_type(
                    item.get("location__coordinates__latitude"),
                    item.get("location__coordinates__longitude"),
                ),
                "gender": item.get("gender")[0],
                "name": {
                    "title": item.get("name__title"),
                    "first": item.get("name__first"),
                    "last": item.get("name__last"),
                },
                "location": {
                    "region": handle_region(item.get("location__state")),
                    "street": item.get("location__street"),
                    "city": item.get("location__city"),
                    "state": item.get("location__state"),
                    "postcode": item.get("location__postcode"),
                    "coordinates": {
                        "latitude": item.get("location__coordinates__latitude"),
                        "longitude": item.get("location__coordinates__longitude"),
                    },
                    "timezone": {
                        "offset": item.get("location__timezone__offset"),
                        "description": item.get("location__timezone__description"),
                    },
                },
                "email": item.get("email"),
                "birthday": item.get("dob__date"),
                "registered": item.get("registered__date"),
                "telephoneNumbers": [Phone.transform(item.get("phone"))],
                "mobileNumbers": [Phone.transform(item.get("cell"))],
                "picture": {
                    "large": item.get("picture__large"),
                    "medium": item.get("picture__medium"),
                    "thumbnail": item.get("picture__thumbnail"),
                },
                "nationality": "BR",
            }
        )
    return res

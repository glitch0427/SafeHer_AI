import requests

OVERPASS_URLS = [
    "https://overpass-api.de/api/interpreter",
    #"https://overpass.kumi.systems/api/interpreter",
    #"https://lz4.overpass-api.de/api/interpreter",
]


def _query_overpass(query):
    for url in OVERPASS_URLS:
        try:
            response = requests.post(
                url,
                data=query,
                timeout=5
            )

            if response.status_code == 200:
                return response.json()

        except Exception:
            pass

    return None


def get_nearby_places(lat, lon, radius=3000):

    query = f"""
    [out:json][timeout:5];

    (
      node["amenity"="police"](around:{radius},{lat},{lon});
      way["amenity"="police"](around:{radius},{lat},{lon});
      relation["amenity"="police"](around:{radius},{lat},{lon});

      node["amenity"="hospital"](around:{radius},{lat},{lon});
      way["amenity"="hospital"](around:{radius},{lat},{lon});
      relation["amenity"="hospital"](around:{radius},{lat},{lon});
    );

    out center;
    """

    data = _query_overpass(query)

    if not data:
        return [], []

    police = []
    hospitals = []

    for element in data["elements"]:

        tags = element.get("tags", {})

        lat_value = element.get(
            "lat",
            element.get("center", {}).get("lat")
        )

        lon_value = element.get(
            "lon",
            element.get("center", {}).get("lon")
        )

        if lat_value is None or lon_value is None:
            continue

        item = {
            "name": tags.get("name", "Unknown"),
            "lat": lat_value,
            "lon": lon_value
        }

        if tags.get("amenity") == "police":
            police.append(item)

        elif tags.get("amenity") == "hospital":
            hospitals.append(item)
    
    police = sorted(
        police,
        key=lambda x: x["name"]
    )

    hospitals = sorted(
        hospitals,
        key=lambda x: x["name"]
    )

    return police, hospitals


if __name__ == "__main__":

    police, hospitals = get_nearby_places(
        28.6139,
        77.2090
    )

    print("Police")

    for p in police:
        print(p)

    print()

    print("Hospitals")

    for h in hospitals:
        print(h)
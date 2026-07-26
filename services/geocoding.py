import requests

HEADERS = {
    "User-Agent": "SafeHerAI/1.0"
}


def get_coordinates(place: str):
    """
    Convert place name into latitude and longitude
    using OpenStreetMap Nominatim API.
    """

    if not place:
        return None

    url = "https://nominatim.openstreetmap.org/search"

    params = {
        "q": place,
        "format": "json",
        "limit": 1
    }

    try:
        response = requests.get(
            url,
            params=params,
            headers=HEADERS,
            timeout=15
        )

        response.raise_for_status()

        data = response.json()

        if not data:
            return None

        latitude = float(data[0]["lat"])
        longitude = float(data[0]["lon"])

        return latitude, longitude

    except Exception as e:
        print(f"Geocoding Error: {e}")
        return None


if __name__ == "__main__":

    place = input("Enter location: ")

    coordinates = get_coordinates(place)

    if coordinates:
        print(f"\nLatitude : {coordinates[0]}")
        print(f"Longitude: {coordinates[1]}")
    else:
        print("Location not found.")
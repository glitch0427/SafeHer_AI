import requests


def get_route(source_coords, destination_coords):
    """
    Returns:
    distance (km)
    duration (minutes)
    route_coordinates (for map)
    """

    if not source_coords or not destination_coords:
        return None

    lat1, lon1 = source_coords
    lat2, lon2 = destination_coords

    url = (
        f"https://router.project-osrm.org/route/v1/driving/"
        f"{lon1},{lat1};{lon2},{lat2}"
        "?overview=full&geometries=geojson"
    )

    try:
        response = requests.get(url, timeout=20)
        response.raise_for_status()

        data = response.json()

        if data["code"] != "Ok":
            return None

        route = data["routes"][0]

        distance = round(route["distance"] / 1000, 2)
        duration = round(route["duration"] / 60, 1)

        geometry = route["geometry"]["coordinates"]

        # Convert [lon, lat] → [lat, lon]
        route_points = [(lat, lon) for lon, lat in geometry]

        return {
            "distance": distance,
            "duration": duration,
            "route_points": route_points
        }

    except Exception as e:
        print("Routing Error:", e)
        return None


if __name__ == "__main__":

    src = (28.6139, 77.2090)   # Delhi

    dst = (28.5355, 77.3910)   # Noida

    result = get_route(src, dst)

    print(result)
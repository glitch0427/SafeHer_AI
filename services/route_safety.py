from services.nearby_places import get_nearby_places

def analyze_route(route_points):
    segments = []

    sample_points = route_points[::25]

    for lat, lon in sample_points:

        police, hospitals = get_nearby_places(
            lat,
            lon,
            radius=3000
        )

        score = len(police) + len(hospitals)

        if score >= 4:
            color = "green"
        elif score >= 2:
            color = "orange"
        else:
            color = "red"

        segments.append({
            "lat": lat,
            "lon": lon,
            "color": color,
            "police": police,
            "hospitals": hospitals
        })

    return segments
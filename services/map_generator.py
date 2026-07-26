import folium
from folium.plugins import Fullscreen


def create_map(
    source_coords,
    destination_coords,
    route,
    police=None,
    hospitals=None,
    segments=None
):
    """
    Creates an interactive Folium map.

    Parameters
    ----------
    source_coords : (lat, lon)
    destination_coords : (lat, lon)
    route : dict
        {
            "distance": ...,
            "duration": ...,
            "route_points": [...]
        }

    police : list (optional)
    hospitals : list (optional)

    Returns
    -------
    folium.Map
    """

    center = [
        (source_coords[0] + destination_coords[0]) / 2,
        (source_coords[1] + destination_coords[1]) / 2,
    ]

    m = folium.Map(
        location=center,
        zoom_start=13,
        control_scale=True
    )

    # Fullscreen Button
    Fullscreen().add_to(m)

    # Source
    folium.Marker(
        location=source_coords,
        tooltip="Source",
        popup="Source",
        icon=folium.Icon(
            color="green",
            icon="play"
        )
    ).add_to(m)

    # Destination
    folium.Marker(
        location=destination_coords,
        tooltip="Destination",
        popup="Destination",
        icon=folium.Icon(
            color="red",
            icon="flag"
        )
    ).add_to(m)

    # Route
    if route and "route_points" in route:

        folium.PolyLine(
            route["route_points"],
            weight=5,
            color="#3B82F6",
            opacity=0.6
        ).add_to(m)

    if segments:

        for segment in segments:

            folium.CircleMarker(
                location=[segment["lat"], segment["lon"]],
                radius=8,
                color=segment["color"],
                fill=True,
                fill_color=segment["color"],
                fill_opacity=0.9,
                popup=f"""
    <b>Safety Zone</b><br>
    Police: {len(segment["police"])}<br>
    Hospitals: {len(segment["hospitals"])}
    """
            ).add_to(m)

    # Police Markers (if coordinates are available)
    if police:
        for station in police:

            if isinstance(station, dict):

                if "lat" in station and "lon" in station:

                    folium.Marker(
                        location=[
                            station["lat"],
                            station["lon"]
                        ],
                        tooltip=station.get(
                            "name",
                            "Police Station"
                        ),
                        popup=station.get(
                            "name",
                            "Police Station"
                        ),
                        icon=folium.Icon(
                            color="blue",
                            icon="shield"
                        )
                    ).add_to(m)

    # Hospital Markers
    if hospitals:
        for hospital in hospitals:

            if isinstance(hospital, dict):

                if "lat" in hospital and "lon" in hospital:

                    folium.Marker(
                        location=[
                            hospital["lat"],
                            hospital["lon"]
                        ],
                        tooltip=hospital.get(
                            "name",
                            "Hospital"
                        ),
                        popup=hospital.get(
                            "name",
                            "Hospital"
                        ),
                        icon=folium.Icon(
                            color="purple",
                            icon="plus"
                        )
                    ).add_to(m)

    folium.LayerControl().add_to(m)

    return m
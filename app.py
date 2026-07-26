import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from streamlit_folium import st_folium

from services.geocoding import get_coordinates
from services.routing import get_route
from services.nearby_places import get_nearby_places
from services.map_generator import create_map
from services.safety_score import calculate_safety_score, get_risk_level
from services.openai_ai import get_safety_advice
from services.sos import send_sos

st.set_page_config(
    page_title="SafeHer AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>

.stApp{
    background:#0F172A;
}

.block-container{
padding-top:4rem;
padding-bottom:2rem;
}

.title{
font-size:48px;
font-weight:700;
color:#3B82F6;
text-align:center;
padding-top:20px;
padding-bottom:8px;
margin-top:15px;
margin-bottom:10px;
line-height:1.4;
word-break:break-word;
overflow:visible;
}

.subtitle{
font-size:18px;
color:#6B7280;
text-align:center;
margin-bottom:20px;
}

[data-testid="stMetric"]{
    background:#1E293B;
    border:1px solid #334155;
    border-radius:15px;
    padding:18px;
    color:white;
    box-shadow:0 4px 12px rgba(0,0,0,0.35);
}

[data-testid="stMetricLabel"]{
    color:#CBD5E1 !important;
    font-weight:600;
}

[data-testid="stMetricValue"]{
    color:white !important;
    font-size:28px;
    font-weight:700;
}

.stButton>button{
width:100%;
height:52px;
border-radius:10px;
font-size:18px;
font-weight:bold;
background:#2563EB;
color:white;
}

.stButton>button:hover{
background:#1D4ED8;
color:white;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
"""
<div class="title">
🛡️ SafeHer AI
</div>

<div class="subtitle">
AI Powered Women's Safety Route Assistant
</div>
""",
unsafe_allow_html=True
)

st.divider()

input1, input2 = st.columns(2)

with input1:

    source = st.text_input(
        "📍 Source",
        placeholder="Enter source location"
    )

with input2:

    destination = st.text_input(
        "🎯 Destination",
        placeholder="Enter destination location"
    )

travel_time = st.radio(
    "Travel Time",
    ["Day", "Night"],
    horizontal=True
)

phone_number = st.text_input(
    "📱 Emergency WhatsApp Number",
    placeholder="+91 XXXXXXXXXX"
)

analyze = st.button(
    "🔍 Analyze Route"
)
if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False

if analyze:
    st.session_state.analysis_done = True

if st.session_state.analysis_done:

    if not source or not destination:

        st.error("Please enter both source and destination.")

        st.stop()

    with st.spinner("📍 Locating places..."):

        source_coords = get_coordinates(source)
        destination_coords = get_coordinates(destination)

    if source_coords is None or destination_coords is None:

        st.error("Unable to locate one or both locations.")

        st.stop()

    with st.spinner("🛣️ Calculating safest route..."):

        route = get_route(
            source_coords,
            destination_coords
        )

    if route is None:

        st.error("Unable to calculate route.")

        st.stop()   

    police, hospitals = get_nearby_places(
        source_coords[0],
        source_coords[1]
    )

    score = calculate_safety_score(
        route["distance"],
        travel_time,
        len(police),
        len(hospitals)
    )

    risk = get_risk_level(score)

    left, right = st.columns([1,2])
    
    with left:

        st.subheader("📊 Journey Summary")

        c1, c2 = st.columns(2)

        with c1:
            st.metric(
                "🛣️ Distance",
                f"{route['distance']} km"
            )

        with c2:
            st.metric(
                "⏱️ Duration",
                f"{route['duration']} min"
            )

        st.metric(
            "⭐ Safety Score",
            f"{score}/100"
        )

        st.metric(
            "🚦 Risk Level",
            risk
        )

        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=score,
                title={"text": "Safety Score"},
                gauge={
                    "axis": {"range": [0, 100]},
                    "bar": {"color": "green"},
                    "steps": [
                        {"range": [0, 40], "color": "#ff4d4d"},
                        {"range": [40, 70], "color": "#ffd54f"},
                        {"range": [70, 100], "color": "#4caf50"},
                     ],
                },
              )
        )

        st.plotly_chart(fig, use_container_width=True)

        st.progress(score / 100)

        st.markdown("---")

        st.subheader("👮 Nearby Police Stations")

        if police:

            for station in police[:5]:

                st.success(f"👮 {station['name']}")

        else:

            st.warning(
                "No nearby police stations found."
            )

        st.markdown("---")

        st.subheader("🏥 Nearby Hospitals")

        if hospitals:

            for hospital in hospitals[:5]:

                st.info(f"🏥 {hospital['name']}")

        else:

            st.warning(
                "No nearby hospitals found."
            )

    with right:

        st.subheader("🗺️ Interactive Route Map")

        route_map = create_map(
            source_coords,
            destination_coords,
            route,
            police,
            hospitals,
        )

        st_folium(
            route_map,
            width=None,
            height=650,
            returned_objects=[]
        )

        st.markdown("---")

        st.subheader("📋 Route Details")

        detail1, detail2 = st.columns(2)

        with detail1:

            st.write("**📍 Source**")
            st.write(source)

            st.write("**🌞 Travel Time**")
            st.write(travel_time)

        with detail2:

            st.write("**🎯 Destination**")
            st.write(destination)

            st.write("**⭐ Safety Score**")
            st.write(f"{score}/100")
            st.markdown("---")

    st.subheader("🤖 AI Safety Analysis")

    with st.spinner("Analyzing route using OpenAI..."):

        try:

            ai_report = get_safety_advice(
                source=source,
                destination=destination,
                travel_time=travel_time,
                score=score
            )

            st.success(ai_report)

        except Exception as e:

            st.error(f"AI Analysis Error: {e}")

    st.markdown("---")

    st.subheader("💡 Smart Safety Recommendations")

    recommendations = []

    if travel_time == "Night":
        recommendations.append(
            "🌙 Prefer well-lit roads and avoid isolated areas."
        )

    if score < 60:
        recommendations.append(
            "🚨 Consider choosing another route if possible."
        )

    if len(police) == 0:
        recommendations.append(
            "👮 No nearby police stations detected."
        )

    if len(hospitals) == 0:
        recommendations.append(
            "🏥 No nearby hospitals detected."
        )

    recommendations.extend([
        "📱 Keep your phone charged.",
        "📍 Share your live location with family or friends.",
        "🚕 Use trusted transport services.",
        "☎️ Save emergency numbers before travelling."
    ])

    for tip in recommendations:
        st.info(tip)

    st.markdown("---")

    st.subheader("🚨 Emergency SOS")

    sos_col1, sos_col2 = st.columns(2)

    with sos_col1:

        if st.button(
            "🚨 Send WhatsApp SOS",
            use_container_width=True
        ):

            if not phone_number:

                st.error(
                    "Please enter an emergency WhatsApp number."
                )

            else:

                send_sos(
                    phone_number,
                    source,
                    destination
                )

                st.success(
                    "WhatsApp opened successfully."
                )

    with sos_col2:

        st.write("**Emergency Contact**")
        st.code(
            phone_number if phone_number else "Not Entered"
        )

    st.markdown("---")

    st.caption(
        "🛡️ SafeHer AI • Built using Streamlit, OSRM, OpenStreetMap and Gemini AI"
    )

    st.markdown("---")

    st.subheader("📈 Route Safety Summary")

    summary = []

    if score >= 80:
        summary.append("🟢 This route is considered relatively safe.")

    elif score >= 60:
        summary.append("🟡 Travel with caution.")

    else:
        summary.append("🔴 High-risk route detected.")

    if travel_time == "Night":
        summary.append("🌙 Night travel increases risk.")

    if len(police) > 0:
        summary.append(f"👮 {len(police)} police station(s) nearby.")

    if len(hospitals) > 0:
        summary.append(f"🏥 {len(hospitals)} hospital(s) nearby.")

    for item in summary:
        st.write(item)

    st.markdown("---")

    st.subheader("📞 Emergency Numbers")

    emergency = {
        "Police": "112",
        "Women Helpline": "181",
        "Ambulance": "108"
    }

    emergency_df = pd.DataFrame(
        emergency.items(),
        columns=["Service", "Number"]
    )

    st.dataframe(
        emergency_df,
        hide_index=True,
        use_container_width=True
    )

    st.markdown("---")

    st.success("✅ Route analysis completed successfully.")

else:

    st.info(
        "Enter source and destination, then click **Analyze Route**."
    )

st.markdown(
"""
---
<center>

### 🛡️ SafeHer AI

AI Powered Women's Safety Assistant

Built using

Streamlit ❤️ | OpenAI 🤖 | OpenStreetMap 🗺️ | OSRM 🚗

</center>
""",
unsafe_allow_html=True
)